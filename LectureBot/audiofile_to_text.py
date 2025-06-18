
import speech_recognition as sr
import whisper

class AudioFileToText:

    def __init__(self,filepath):
        self.filepath = filepath
        self.model = whisper.load_model("base")

    def transcribe(self):
        """
        Description: breaks the audio into chunks and transcribes into text
        :return: result or None
        """
        try:
            result = self.model.transcribe(self.filepath,fp16=False)
            return result['text']
        except Exception as e:
            print(f'an error occured {e}')
            return None

