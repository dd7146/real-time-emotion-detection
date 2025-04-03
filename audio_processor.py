import librosa
import sounddevice as sd
import numpy as np
from threading import Thread

class AudioProcessor:
    def __init__(self):
        self.fs = 44100  # Sample rate
        self.recording = False
        self.audio_data = []
        
    def start_recording(self):
        self.recording = True
        self.audio_data = []
        Thread(target=self._record).start()
        
    def _record(self):
        while self.recording:
            data = sd.rec(int(1 * self.fs), samplerate=self.fs, channels=1)
            sd.wait()
            self.audio_data.append(data)
            
    def stop_recording(self):
        self.recording = False
        
    def get_emotion(self):
        if not self.audio_data:
            return "No audio"
        
        # Combine recorded chunks
        audio = np.concatenate(self.audio_data, axis=0).flatten()
        
        # Extract features
        mfcc = np.mean(librosa.feature.mfcc(y=audio, sr=self.fs, n_mfcc=13), axis=1)
        energy = np.mean(librosa.feature.rms(y=audio))
        
        # Simple threshold-based emotion detection
        if energy > 0.1:
            return "Angry" if np.mean(mfcc) < -10 else "Happy"
        return "Neutral"