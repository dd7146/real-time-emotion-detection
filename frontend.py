import tkinter as tk
from PIL import Image, ImageTk
import cv2

class Frontend:
    def __init__(self, video_processor, audio_processor):
        self.root = tk.Tk()
        self.root.title("Real-Time Emotion Detector")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.video_processor = video_processor
        self.audio_processor = audio_processor
        
        # Video display
        self.video_label = tk.Label(self.root)
        self.video_label.pack()
        
        # Emotion labels
        self.video_emotion = tk.Label(self.root, text="Video Emotion: Neutral")
        self.video_emotion.pack()
        self.audio_emotion = tk.Label(self.root, text="Audio Emotion: Neutral")
        self.audio_emotion.pack()
        
        # Start/Stop button
        self.btn = tk.Button(self.root, text="Start", command=self.toggle_recording)
        self.btn.pack()
        
        self.running = False
        self.update()
        self.root.mainloop()
        
    def toggle_recording(self):
        if not self.running:
            self.running = True
            self.audio_processor.start_recording()
            self.btn.config(text="Stop")
        else:
            self.running = False
            self.audio_processor.stop_recording()
            self.btn.config(text="Start")
            
    def update(self):
        if self.running:
            frame, v_emotion = self.video_processor.get_frame()
            if frame is not None:
                # Convert frame to RGB and display
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
                
                self.video_emotion.config(text=f"Video Emotion: {v_emotion}")
                a_emotion = self.audio_processor.get_emotion()
                self.audio_emotion.config(text=f"Audio Emotion: {a_emotion}")
        
        self.root.after(10, self.update)
        
    def on_closing(self):
        self.video_processor.release()
        self.audio_processor.stop_recording()
        self.root.destroy()