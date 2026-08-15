# 🏦 ATM Video Anomaly Detection System

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)

An intelligent Machine Learning web application designed to automatically detect suspicious or abnormal behavior in ATM surveillance videos. Built with a **Convolutional Neural Network (CNN)** and deployed using a dynamic **Flask** web interface.

*(Add your GIF/Video demo here!)*
<!-- Example: ![Demo](demo.gif) -->

## 🚀 Key Features

* **Deep Learning Vision:** Utilizes a custom CNN model to extract features from video frames and classify them as `Normal` or `Abnormal`.
* **Automated Frame Extraction:** Processes video uploads in real-time, extracting chronological frames using OpenCV for model prediction.
* **Instant Threat Alerts:** Automatically dispatches an emergency email notification via `yagmail` to administrators if an anomaly is detected.
* **Dynamic Analytics:** Displays visual prediction graphs and metrics to the user.
* **Secure Authentication:** Built-in User Registration and Login system using Excel/Pandas for localized credential management.

## 🧠 Model Architecture
The AI backend was trained using TensorFlow/Keras on a dataset of ATM surveillance footage. 
* Frames are extracted and preprocessed to a uniform `128x128x3` resolution.
* The model weights are saved in a highly optimized `HDF5` format for rapid inference in a production environment.
* Predictions are made on a frame-by-frame basis, and a final classification is determined using statistical mode aggregation.

## 🛠️ Technology Stack
* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask, Pandas
* **Machine Learning:** TensorFlow, Keras, Numpy
* **Computer Vision:** OpenCV (cv2)
* **Automation:** Yagmail (SMTP automation)

## 💻 How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/swapnilpatil3/ATM-Anomaly-Project.git
   ```

2. **Navigate to the Application Directory**
   ```bash
   cd ATM-Anomaly-Project/VideoAnomlyDetection_FE
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Application**
   ```bash
   python app.py
   ```
   The application will be live at `http://127.0.0.1:5003`

## 📬 Contact / Portfolio
Developed by Swapnil Patil.
* [LinkedIn](https://www.linkedin.com/in/) *(Add your link here!)*
* [Portfolio](https://) *(Add your link here!)*
