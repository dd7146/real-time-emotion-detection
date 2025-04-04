# Real-Time Emotion Detector

This project is a Python-based application that detects emotions in real-time using both video and audio feeds. It uses a webcam to capture live video, processes facial expressions to detect emotions, and analyzes audio input to infer emotional states. The application features a simple GUI built with Tkinter to display the video feed and detected emotions.

## Features
- **Video Emotion Detection**: Uses the `deepface` library to analyze facial expressions and detect emotions (e.g., happy, sad, angry, neutral).
- **Audio Emotion Detection**: Performs basic audio analysis using `librosa` to infer emotions (e.g., happy, angry, neutral) based on audio features like energy and MFCC.
- **Live Feed Display**: Displays the webcam feed with a bounding box around detected faces and the corresponding emotion label.
- **GUI**: A Tkinter-based interface shows the video feed and both video and audio emotion results in real-time.
- **Start/Stop Control**: A button to start or stop the emotion detection process.

## Project Structure
emotion_detector/
├── main.py           # Main application logic
├── frontend.py       # GUI using Tkinter
├── video_processor.py # Video feed and emotion detection with deepface
├── audio_processor.py # Audio feed and basic emotion detection
├── requirements.txt  # Dependencies
└── README.md         # Project documentation


## Prerequisites
- **Python**: Version 3.11 or 3.12 (3.11 recommended for better compatibility).
- **Webcam**: A working webcam for video input.
- **Microphone**: A working microphone for audio input.
- **Operating System**: Tested on Windows (should work on macOS/Linux with minor adjustments).

## Setup Instructions

### 1. Clone or Download the Project
- Download the project files to your local machine (e.g., `C:\Users\Deepayan\Desktop\emotion_detector`).

### 2. Set Up a Virtual Environment
1. Open a Command Prompt.
2. Navigate to the project directory:
   ```bash
   cd C:\Users\Deepayan\Desktop\emotion_detector

Create a virtual environment
C:\Users\Deepayan\AppData\Local\Programs\Python\Python311\python -m venv venv


Activate virtual environment
venv\Scripts\activate

Install Dependencies
opencv-python
deepface
librosa
numpy
tk
sounddevice
pillow
tf-keras

pip install -r requirements.txt

Run the application
python main.py
