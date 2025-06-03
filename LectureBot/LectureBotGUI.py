'''
    Description: This initializes the GUI and assigns the functions to each button
    Return: NONE
'''
from tkinter import *
from pathlib import Path
from tkinter import filedialog
from audiofile_to_text import AudioFileToText
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
        self.savingFile = None
        self.saveButton = None
        self.filename = None
        self.lectureName = None
        self.box = None
        self.box2 = None
        self.choosing_lang = None
        self.name = None
        self.dest_lang = ""
        self.src_lang = ""

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
        label = Label(self.pancakePanel, text = "Files Downloaded:", font=("Times New Roman", 14, "bold"), background = "#FFA580")
        label.place(x=18, y=10)
        self.pancakePanel.place(x = -200, y = 50)

        # The output file that keeps track of recorded responses.
        self.file = "output.txt"
        self.translated_file = f"translated_{self.file}.txt"
        # This is defined in the audioPress funciton. It is so you can display what is being recorded.
        self.text_box = None
        # This is so you can edit and save the text that was outputted.
        self.txt_file = "output.txt"
        self.curr_file = "output.txt"

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
        audiofilebutton = Button(self.main,text = "Upload File",command = self.audiofilepress)

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

        # Places audiofile button
        audiofilebutton.config(font = ("Times New Roman",7,"bold"), background = "white", width = "13", height = "1")
        audiofilebutton.place(x=825,y=56)


    def translatePress(self):
        '''
            Description: Translate button pressed-> button prompts the audio to text conversion
            Return: NONE
        '''
        # Have a screen pop up that asks which file to translate and which language (dest_lang)
        self.choosing_lang = Toplevel()  # Creating pop up window
        self.choosing_lang.title("Choosing the Language")
        self.choosing_lang.geometry("450x300")

        label = Label(self.choosing_lang, text="Unfortunately, this program cannot support characters at the moment\n"
                                               "Please pick a different language.\n"
                                               "For spanish it is \'es\'.", font=("Times New Roman", 10))
        label.place(x=18, y=10)

        label = Label(self.choosing_lang, text="Type the First 2 Letters of the Starting Language.",
                      font=("Times New Roman", 10))
        label.place(x=18, y=70)

        self.box = Entry(self.choosing_lang, width=60)
        self.box.place(x=25, y=90)

        label2 = Label(self.choosing_lang, text="Type the First 2 Letters of the Ending Language.",
                       font=("Times New Roman", 10))
        label2.place(x=18, y=120)

        self.box2 = Entry(self.choosing_lang, width=60)
        self.box2.place(x=25, y=140)

        label3 = Label(self.choosing_lang, text="Name of File",
                       font=("Times New Roman", 10))
        label3.place(x=18, y=170)

        self.box3 = Entry(self.choosing_lang, width=60)
        self.box3.place(x=25, y=190)

        nextButton = Button(self.choosing_lang, text="Done", command=self.done)
        nextButton.place(x=180, y=230)

    def done(self):
        '''
            Description: This button allows the program to access the source and destination languages. Then it calls
            translate() to translate the text. Finally, it destroys the window.
            Return: NONE
        '''
        self.src_lang = self.box.get()
        print(self.src_lang)
        self.dest_lang = self.box2.get()
        print(self.dest_lang)
        self.translate()
        self.choosing_lang.destroy()

    def translate(self):
        '''
            Description: This translates the file.
            Return: NONE
        '''
        t = Translate(self.src_lang, self.dest_lang, self.curr_file, self.text_box)
        asyncio.run(t.output(self.text_box.get(1.0, END)))
        t.display()
        self.lectureName = self.box3.get()
        self.saveTranslated()
        # Adds the translated file to the list of files in the pancake button.
        self.fileList.append(t.file_name)

    def audioPress(self):
        '''
            Description: Audio button pressed-> button prompts audio to begin recording
            Return: NONE
        '''
        recog = sr.Recognizer()
        print("audio")
        while(1):
            try:
                with sr.Microphone() as source:
                    recog.adjust_for_ambient_noise(source, duration=0.1)
                    audio = recog.listen(source, phrase_time_limit=1200)
                    TEXT = recog.recognize_google(audio)
                    print(TEXT)
                    if TEXT != "":
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
        '''
            Description: This button allows you to save the changes you made in the text box.
            Return: NONE
        '''
        print("Saving...")
        if isinstance(self.txt_file, str):
            self.curr_file = self.txt_file
        self.txt_file = open(f'{self.curr_file}', "w")
        self.txt_file.write(self.text_box.get(1.0, END))
        self.txt_file.close()

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

        with open("output.txt", "r") as output:  # Copying contents of the output file into the file the user created
            content = output.read()

        with open(file_path, "w") as new_file:
            new_file.write(content)

        with open("output.txt", "w") as output:
            output.write("")

    def saveTranslated(self):
        '''
            Description: Saving translated file to downloads folder and then clearing output.txt, as well.
            Return: NONE
        '''
        downloads = Path.home() / "Downloads"
        file_path = downloads / self.lectureName

        with open("translated_output.txt", "r") as output:  # Copying contents of the output file into the file the user created
            content = output.read()

        with open(file_path, "w") as new_file:
            new_file.write(content)

        with open("translated_output.txt", "w") as output:
            output.write("")

        with open("output.txt", "w") as output:
            output.write("")

<<<<<<< HEAD
=======
    def audiofilepress(self):
        """
        Description: this function allows the user to select an audio file and
        trancribes it into text.
        :return: None
        """
        file_path = filedialog.askopenfilename(title="Select audio file",filetypes=[("Audio Files", "*.wav")])
        if file_path:
            transcriber = AudioFileToText(file_path)
            text = transcriber.transcribe()

            if text:
                with open(self.file,"a") as f:
                    f.write(text + "\n")
                self.text_box = Text(self.main, width=70, height=20, font=("Times New Roman", 12))
                self.text_box.place(x=200, y=120)
                self.text_box.insert(END,text)

def main():
    g = GUI()


>>>>>>> audiofile_to_text
class Translate():
    '''
        Description: This class helps us translate the text and output it into the text_box in the GUI.
    '''
    def __init__(self, src_lang, dest_lang, file_name, text_box):
        '''
            Parameters:
                src_lang = the language we are translating from.
                dest_lang = the language we want to translate to.
                file_name = the name of the file that is in the text box.
                text_box = the textbox in the GUI itself.
        '''
        self.src_lang = src_lang
        self.dest_lang = dest_lang
        self.file = file_name
        self.text_box = text_box
        self.trans = Translator()
        self.translation = None
        self.file_name = f"translated_{self.file}"

    async def output(self, text):
        """
            Description: This is translating the text and then writing it to the translated version of the file.
            Parameter:
                text = the text that we are translating
            Return: NONE
        """
        # Translates the Text
        self.translation = await self.trans.translate(text, src=self.src_lang, dest=self.dest_lang)
        print(self.translation.text)
        # Writes to the
        f = open(f"{self.file_name}", "w")
        f.close()
        trans_file = open(f"{self.file_name}", "r+")
        trans_file.write(self.translation.text)
        trans_file.close()

    def display(self):
        '''
            Description: Inserts the translated text into the GUI.
            Return: NONE
        '''
        self.text_box.delete(1.0, END)
        f = open(f'{self.file_name}', "r")
        reading = f.read()
        self.text_box.insert(END, reading)
        f.close()

def main():
    g = GUI()


if __name__ == '__main__':
    main()
