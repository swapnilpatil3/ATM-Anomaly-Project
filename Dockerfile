FROM python:3.11-slim

# Install system dependencies (required for OpenCV)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /code

# Copy the requirements file
COPY VideoAnomlyDetection_FE/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set up a new user (Hugging Face requires apps to run as a non-root user)
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR /code/VideoAnomlyDetection_FE

# Expose port 7860
EXPOSE 7860
ENV PORT=7860

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "--workers", "1", "--threads", "8", "--timeout", "0", "app:app"]
