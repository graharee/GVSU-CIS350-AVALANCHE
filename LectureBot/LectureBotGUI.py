'''
    Description: This initializes the GUI and assigns the functions to each button
    Return: NONE
'''
from tkinter import *
from tkinter import filedialog
from pathlib import Path
import speech_recognition as sr
import asyncio
import pyttsx3
from googletrans import Translator

class GUI:
    def __init__(self):
        '''
            Description: This initializes the GUI
            Return: NONE
        '''
        self.main = Tk()            # Creating GUI base
        self.main.geometry("900x900")
        self.main.configure(background = "white")
        self.main.title("LectureBot")
        logo = PhotoImage(file='logo.png')
        self.main.iconphoto(True, logo)

        # adding orange box
        self.border = Frame(self.main, bg="orange")
        self.border.place(x=100, y=100, width=750, height=750)

        self.square = Frame(self.border, bg="white")
        self.square.place(x=5, y=5, width=740, height=740)

        self.placeButtons()

        # adding pancake panel that shows all downloaded files
        self.isPanelVisible = False
        self.fileList = []

        self.pancakePanel = Frame(self.main, background = "#FFA580", width = 200, height = 850)
        label = Label(self.pancakePanel, text = "Files Saved:", font=("Times New Roman", 14, "bold"), background = "#FFA580")
        label.place(x=18, y=10)
        self.pancakePanel.place(x = -200, y = 50)

        # The output file that keeps track of recorded responses.
        self.file = None
        # This is defined in the audioPress funciton. It is so you can display what is being recorded.
        self.text_box = None
        # This is so you can edit and save the text that was outputted.
        self.txt_file = "output.txt"

        self.main.mainloop()

    def placeButtons(self):
        '''
            Description: This function places the buttons onto the GUI and assigns functionality
            Return: NONE
        '''

        # Assigning picture to each button
        self.downloadButtonImg = PhotoImage(file = 'download.png')
        self.pancakeButtonImg = PhotoImage(file = 'pancake.png')
        self.micButtonImg = PhotoImage(file = 'mic.png')

        # Adding picture to each button and assigning function
        downloadButton = Button(self.main, image = self.downloadButtonImg, command = self.downloadPress)
        pancakeButton = Button(self.main, image = self.pancakeButtonImg, command = self.pancakePress)
        micButton = Button(self.square, image = self.micButtonImg, command = self.audioPress)
        transcriptButton = Button(self.main, text = "T", command = self.translatePress)
        saveButton = Button(self.main, text= "Save", command=self.savePress)

        # Places transcript button
        transcriptButton.config(font = ("Times New Roman", 21, "bold"), background = "white", width = "1", height = "1")  # performs callback of function
        transcriptButton.place(x = 825, y = 0)

        # Places download button
        downloadButton.config(width = "44", height = "50")
        downloadButton.place(x = 850, y = 0)

        # Places pancake button
        pancakeButton.config(width = "58", height = "50")
        pancakeButton.place(x = 0, y = 0)

        # Places audio button
        micButton.config(width = "237", height = "200")
        micButton.place(x = 250, y = 450)

        saveButton.config(width="5", height="1")
        saveButton.place(x=700, y=600)

    async def translatePress(self):
        '''
            Description: Translate button pressed-> button prompts the audio to text conversion
            Return: NONE
        '''
        src_lang = "en"
        dest_lang = "es"
        print("Translating")

        # Have a screen pop up that asks which file to translate and which language (dest_lang)

        trans = Translator()
        translation = await trans.translate(self.file, src=src_lang, dest=dest_lang)
        # For testing purposes
        print(translation.text)
        # For the GUI
        trans_file = open("translated_" + self.file + ".txt", "w")
        trans_file.write(translation.text)
        trans_file.close()
        # Adds the translated file to the list of files in the pancake button.
        self.fileList += trans_file

    def audioPress(self):
        '''
            Description: Audio button pressed-> button prompts audio to begin recording
            Return: NONE
        '''
        recog = sr.Recognizer()
        TEXT = None
        print("audio")
        while(1):
            try:
                with sr.Microphone() as source:
                    recog.adjust_for_ambient_noise(source, duration=0.1)
                    audio = recog.listen(source, phrase_time_limit=1200)
                    TEXT = recog.recognize_google(audio)
                    print(TEXT)
                    if TEXT != None:
                        # This is a file that keeps track of what is being said, until the file is downloaded.
                        self.file = open("output.txt", "a")
                        self.file.write(TEXT + '\n')
                        self.file.close()
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except sr.UnknownValueError:
                print(f"Unknown Value Error")
                break
            except KeyboardInterrupt:
                print("You stopped the code.")
            except TimeoutError:
                print("It timed out.")
        self.text_box = Text(self.main, width=70, height=20, font=("Times New Roman", 12))
        self.text_box.place(x=200, y=120)
        output_file = open("output.txt", "r")
        reading = output_file.read()
        self.text_box.insert(END, reading)
        output_file.close()

    def savePress(self):
        print("Saving...")
        self.txt_file = open(self.txt_file, "w")
        self.txt_file.write(self.text_box.get(1.0, END))

    def pancakePress(self):
        '''
            Description: Pancake button pressed-> pop up window appears to show what files have been
                        created and saved so far
            Return: NONE
        '''
        if (self.isPanelVisible == False): # If the panel is not shown
            self.pancakePanel.place(x = 0, y = 50)  # Show the panel

            y = 0
            for item in self.fileList:      # List all the file created
                label = Label(self.pancakePanel, text=item, font=("Times New Roman", 12, "bold"), background="#FFA580")
                label.place(x = 18, y = 40 + y)
                y += 30

            self.isPanelVisible = True      # Change state to panel shown
        else:   # If the panel is shown
            self.pancakePanel.place(x = -200, y = 50) # Make the panel disappear
            self.isPanelVisible = False     # Change state to panel not shown

    def downloadPress(self):
        '''
            Description: Download button pressed-> pop up window appears to prompt user
                        to save file by a specified name.
            Return: NONE
        '''

        self.savingFile = Toplevel()    # Creating pop up window
        self.savingFile.title("Naming Lecture File")
        self.savingFile.geometry("200x100")

        label = Label(self.savingFile, text = "File saves to downloads folder", font = ("Times New Roman", 10))
        label.place(x = 18, y = 10)             # Always saving files to downloads folder

        self.saveButton = Button(self.savingFile, text = "Save", command = self.getFilename)
        self.saveButton.place(x = 85, y = 70)  # Creating save button on pop up window, this button saves the file to downloads folder

        self.filename = Entry(self.savingFile, width = 25)
        self.filename.place(x = 25, y = 30)  # Creating text box for user to enter a file name

        # You have to make a copy of output.txt, while re-nameing it with self.filename, and clearing output.txt.

    def getFilename(self):
        '''
            Description: Getting file name from GUI text box
            Return: NONE
        '''
        self.lectureName = self.filename.get() + ".txt"
        self.fileList.append(self.lectureName)

        self.saveFile()
        self.savingFile.destroy()

    def saveFile(self):
        '''
            Description: Saving file to downloads folder
            Return: NONE
        '''
        downloads = Path.home() / "Downloads"
        file_path = downloads / self.lectureName

        file_path.write_text("audio content") # adding audio to text here


def main():
    g = GUI()

if __name__ == '__main__':
    main()
