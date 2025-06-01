from os import remove

import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

AudioSegment.converter = r"//wsl.localhost/Ubuntu/home/finkeln/CIS350-HW2-Finkel/GVSU-CIS350-S25/LectureBot/ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe"

class AudioFileToText:

    def __init__(self,filepath):
        self.filepath = filepath
        self.r = sr.Recognizer()
        self.audio_file = sr.AudioFile(filepath)

    def transcribe(self):
        full_text = ''
        chunk_files = self.remove_silence()
        for chunk in chunk_files:
            try:
                with sr.AudioFile(chunk) as source:
                    total_duration = source.DURATION
                    offset = 0
                    duration = 10
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

    def remove_silence(self):
        chunk_files = []
        audio = AudioSegment.from_file(self.filepath)
        chunks = split_on_silence(audio,min_silence_len=2000,silence_thresh=-16,keep_silence=200)
        for i, chunk in enumerate(chunks):
            chunk_audio = f"chunk_{i}.wav"
            chunk.export(chunk_audio,format="wav")
            chunk_files.append(chunk_audio)
        return chunk_files


if __name__ == "__main__":
    filepath = input("enter the path to your file:")
    audiofile = AudioFileToText(filepath)
    text = audiofile.transcribe()
    print(text)
