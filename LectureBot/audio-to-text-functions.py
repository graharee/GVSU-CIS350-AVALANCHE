import speech_recognition as sr
import pyttsx3


class Audio_to_text():

    def __init__(self):
        self.name = 'audio button'
        self.recog = sr.Recognizer()

    def listen(self):
        try:
            with sr.Microphone() as source:
                self.recog.adjust_for_ambient_noise(source, duration=0.2)
                audio = self.recog.listen(source)
                text = sr.Recognizer.recognize_google(audio)
                return text
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

    def output(self, text):
        print(text)


if __name__ == "__main__":
    a = Audio_to_text()
    text = a.listen()
    a.output(text)
