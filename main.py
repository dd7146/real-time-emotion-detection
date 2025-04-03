from video_processor import VideoProcessor
from audio_processor import AudioProcessor
from frontend import Frontend

if __name__ == "__main__":
    try:
        video_proc = VideoProcessor()
        audio_proc = AudioProcessor()
        app = Frontend(video_proc, audio_proc)
    except Exception as e:
        print(f"Error initializing application: {e}")