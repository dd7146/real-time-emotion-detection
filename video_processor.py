import cv2
from deepface import DeepFace
import numpy as np

class VideoProcessor:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # 0 for default webcam
        if not self.cap.isOpened():
            raise Exception("Could not open webcam")
        
    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None, "Camera not available"
        
        # Detect emotions using DeepFace
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
        except Exception as e:
            print(f"Emotion detection error: {e}")
            emotion = "Neutral"
        
        # Draw rectangle around face and label emotion
        try:
            faces = DeepFace.extract_faces(frame, enforce_detection=False)
            for face in faces:
                x, y, w, h = face['facial_area']['x'], face['facial_area']['y'], face['facial_area']['w'], face['facial_area']['h']
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, emotion, (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        except Exception as e:
            print(f"Face detection error: {e}")
        
        return frame, emotion
    
    def release(self):
        self.cap.release()