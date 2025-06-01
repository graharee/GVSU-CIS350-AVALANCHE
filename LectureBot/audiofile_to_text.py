
import speech_recognition as sr

class AudioFileToText:

    def __init__(self,filepath):
        self.filepath = filepath
        self.r = sr.Recognizer()
        self.audio_file = sr.AudioFile(filepath)

    def transcribe(self):
        full_text = ''
        try:
            with self.audio_file as source:
                total_duration = source.DURATION
                offset = 0
                #the interval
                duration = 300
                while offset < total_duration:
                    audio = self.r.record(source,duration=duration,offset=offset)
                    try:
                        text = self.r.recognize_google(audio)
                        full_text += text + ' '
                    except sr.UnknownValueError:
                        print(f"error at chunk {offset} - {offset + duration}")
                    offset += duration
            return full_text
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print(f"Unknown Value Error")
        except KeyboardInterrupt:
            print("You stopped the code.")
        except TimeoutError:
            print("It timed out.")
        except:
            print("There is another error somewhere")


if __name__ == "__main__":
    filepath = input("enter the path to your file:")
    audiofile = AudioFileToText(filepath)
    text = audiofile.transcribe()
    print(text)
