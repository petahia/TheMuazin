import speech_recognition as sr
from logger import Logger
logger = Logger.get_logger()


class STT:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_wav(self,wav_file):
        with sr.AudioFile(f'{wav_file}') as source:
            audio = self.recognizer.record(source)
        try:
            text = self.recognizer.recognize_google(audio)
            logger.info(f"Transcription: {text}")
            return text
        except sr.UnknownValueError:
            logger.error("Could not understand audio")
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service; {e}")