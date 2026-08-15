import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"
from tensorflow.keras.models import model_from_json
from pathlib import Path
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
from glob import glob

f = Path("model/model_structure.json")
model_structure = f.read_text()
model = model_from_json(model_structure)
model.load_weights("model/model_weights.h5")

def test_video(path):
    print("Testing:", path)
    os.makedirs('static/temp', exist_ok=True)
    files = glob('static/temp/*')
    for f in files: os.remove(f)
    
    cap = cv2.VideoCapture(path)   
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if count % 30 == 0:
                cv2.imwrite(f'static/temp/frame_{count}.jpg', frame)
            count += 1
        else:
            break
    cap.release()

    images = glob("static/temp/*.jpg")
    prediction_images = []
    for img_path in images:
        img = image.load_img(img_path, target_size=(128, 128, 3))
        img = image.img_to_array(img) / 255.0
        prediction_images.append(img)

    prediction_images = np.array(prediction_images)
    if len(prediction_images) == 0: return "No frames"
    y_pred = model.predict(prediction_images, batch_size=1, verbose=0)
    print("Raw predictions:", y_pred)
    y_predict = [int(np.argmax(pred)) for pred in y_pred]
    print("Argmax predictions:", y_predict)
    from statistics import mode
    try:
        class_label = {0:'Abnormal', 1:'Normal'}[mode(y_predict)]
        print("Final:", class_label)
    except:
        print("Final: Error calculating mode")

print("--- Testing u_input videos ---")
for v in glob("../ATM vedio_anamoly_segregation/u_input/*.mp4"):
    test_video(v)
