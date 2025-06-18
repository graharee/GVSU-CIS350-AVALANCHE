"""
    Description: This initializes the GUI and assigns the functions to each button
    Return: NONE
"""
from tkinter import *
from pathlib import Path
from tkinter import filedialog
from audiofile_to_text import AudioFileToText
import speech_recognition as sr
import asyncio
import pyttsx3
from googletrans import Translator
import threading


class GUI:

    def __init__(self):
        """
            Description: This initializes the GUI
            Return: NONE
        """
        self.main = Tk()  # Creating GUI base
        self.savingFile = None
        self.filename = None
        self.lectureName = None
        self.box = None
        self.box2 = None
        self.box3 = None
        self.choosing_lang = None
        self.dest_lang = ""
        self.src_lang = ""
        self.downloadButton = None
        self.downloadButtonImg = None
        self.pancakeButton = None
        self.pancakeButtonImg = None
        self.audioButton = None
        self.audioButtonImg = None
        self.transcriptButton = None
        self.saveButton = None
        self.saveButtonImg = None
        self.audiofilebutton = None
        self.uploadButtonImg = None
        self.stop_thread = None
        self.thread = None

        self.main.geometry("900x900")
        self.main.configure(background="#FFA580")
        self.main.title("LectureBot")
        self.logo = PhotoImage(file='logo.png')
        self.main.iconphoto(True, self.logo)

        self.border = Frame(self.main, bg="orange")
        self.border.place(x=100, y=100, width=750, height=650)

        self.square = Frame(self.border, bg="white")
        self.square.place(x=5, y=5, width=740, height=640)

        self.placeButtons()

        # adding pancake panel that shows all downloaded files
        self.isPanelVisible = False

        #creates the folder that the .txt files save to if not already made
        self.save_folder = Path("saved_transcripts")
        self.save_folder.mkdir(exist_ok=True)


        self.fileList = []

        for file in self.save_folder.iterdir():
            self.fileList.append(file.name)

        self.pancakePanel = Frame(self.main, background="orange", width=200, height=850)
        label = Label(self.pancakePanel, text="Files Downloaded:", font=("Times New Roman", 14, "bold"),
                      background="orange")
        label.place(x=18, y=10)
        self.pancakePanel.place(x=-200, y=50)

        # The output file that keeps track of recorded responses.
        self.file = "output.txt"
        self.translated_file = f"translated_{self.file}.txt"
        # This is defined in the audioPress function. It is so you can display what is being recorded.
        self.text_box = Text(self.square, width=91, height=33, font=("Times New Roman", 12))
        self.text_box.place(x=5, y=5)
        # Displaying the output.txt (Last known file)
        output_file = open("output.txt", "r")
        reading = output_file.read()
        self.text_box.insert(END, reading)
        output_file.close()
        # This is so you can edit and save the text that was outputted.
        self.txt_file = "output.txt"
        self.curr_file = "output.txt"
        # For the dropdown menus for the Translation
        self.clicked = None
        self.clicked2 = None

        self.run()

    def run(self):
        """
            Description: This function runs the GUI
            Return: NONE
        """
        self.main.mainloop()

    def placeButtons(self):
        """
            Description: This function places the buttons onto the GUI and assigns functionality
            Return: NONE
        """

        # Assigning picture to each button
        self.downloadButtonImg = PhotoImage(file='download.png')
        self.pancakeButtonImg = PhotoImage(file='pancake.png')
        self.audioButtonImg = PhotoImage(file='mic.png')
        self.saveButtonImg = PhotoImage(file='save_button.png')
        self.uploadButtonImg = PhotoImage(file='upload.png')

        # Adding picture to each button and assigning function
        self.downloadButton = Button(self.main, image=self.downloadButtonImg, command=self.downloadPress)
        self.pancakeButton = Button(self.main, image=self.pancakeButtonImg, command=self.pancakePress)
        self.audioButton = Button(self.main, image=self.audioButtonImg, command=self.audioPress)
        self.transcriptButton = Button(self.main, text="T", command=self.translatePress)
        self.saveButton = Button(self.main, image=self.saveButtonImg, command=self.savePress)
        self.audiofilebutton = Button(self.main, image=self.uploadButtonImg, command=self.audiofilepress)

        # Places transcript button
        # performs callback of function
        self.transcriptButton.config(font=("Times New Roman", 21, "bold"), background="white", width="1", height="1")
        self.transcriptButton.place(x=731, y=0)

        # Places download button
        self.downloadButton.config(width="44", height="50")
        self.downloadButton.place(x=850, y=0)

        # Places pancake button
        self.pancakeButton.config(width="50", height="50")
        self.pancakeButton.place(x=0, y=0)

        # Places audio button
        self.audioButton.config(width="35", height="50")
        self.audioButton.place(x=690, y=0)

        self.saveButton.config(width="41", height="50")
        self.saveButton.place(x=758, y=0)

        # Places audiofile button
        self.audiofilebutton.config(font=("Times New Roman", 7, "bold"), background="white", width="40", height="50")
        self.audiofilebutton.place(x=805, y=0)

    def translatePress(self):
        """
            Description: Translate button pressed-> button prompts the audio to text conversion
            Return: NONE
        """
        # Have a screen pop up that asks which file to translate and which language (dest_lang)

        self.choosing_lang = Toplevel()  # Creating pop up window
        self.choosing_lang.title("Choosing the Language")
        self.choosing_lang.geometry("450x300")

        label = Label(self.choosing_lang, text="Please select a language and name your file\n",
                      font=("Times New Roman", 10))
        label.place(x=18, y=10)

        label = Label(self.choosing_lang, text="Choose Starting Language",
                      font=("Times New Roman", 10))
        label.place(x=18, y=70)

        self.clicked = StringVar()
        self.clicked.set("English")

        self.box = OptionMenu(self.choosing_lang, self.clicked, 'Afrikaans', 'Albanian', 'Amharic', 'Arabic',
                              'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian',
                              'Catalan', 'Cebuano', 'Chichewa', 'Chinese (simplified)', 'Chinese (traditional)',
                              'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian',
                              'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek',
                              'Gujarati', 'Haitian creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hebrew', 'Hindi', 'Hmong',
                              'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese',
                              'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz', 'Lao',
                              'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay',
                              'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (burmese)', 'Nepali',
                              'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian',
                              'Russian', 'Samoan', 'Scots gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala',
                              'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik',
                              'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek',
                              'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')
        """self.box = Entry(self.choosing_lang, width=60)"""
        self.box.place(x=25, y=90)

        label2 = Label(self.choosing_lang, text="Choose Ending Language.",
                       font=("Times New Roman", 10))
        label2.place(x=18, y=120)

        self.clicked2 = StringVar()
        self.clicked2.set("Spanish")

        self.box2 = OptionMenu(self.choosing_lang, self.clicked2, 'Afrikaans', 'Albanian', 'Amharic', 'Arabic',
                               'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian',
                               'Catalan', 'Cebuano', 'Chichewa', 'Chinese (simplified)', 'Chinese (traditional)',
                               'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian',
                               'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek',
                               'Gujarati', 'Haitian creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong',
                               'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese',
                               'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish (Kurmanji)', 'Kyrgyz',
                               'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy',
                               'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (burmese)',
                               'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi',
                               'Romanian', 'Russian', 'Samoan', 'Scots gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi',
                               'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish',
                               'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek',
                               'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')
        """self.box2 = Entry(self.choosing_lang, width=60)"""
        self.box2.place(x=25, y=140)

        label3 = Label(self.choosing_lang, text="Name of File",
                       font=("Times New Roman", 10))
        label3.place(x=18, y=170)

        self.box3 = Entry(self.choosing_lang, width=60)
        self.box3.place(x=25, y=190)

        nextButton = Button(self.choosing_lang, text="Done", command=self.done)
        nextButton.place(x=180, y=230)

    def done(self):
        """
            Description: This button allows the program to access the source and destination languages. Then it calls
            translate() to translate the text. Finally, it destroys the window.
            Return: NONE
        """
        LANGUAGES = dict({'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
                          'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
                          'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny',
                          'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co',
                          'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
                          'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr',
                          'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el',
                          'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he',
                          'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig',
                          'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw',
                          'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
                          'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt',
                          'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml',
                          'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my',
                          'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa',
                          'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru',
                          'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
                          'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so',
                          'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg',
                          'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur',
                          'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',
                          'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'})
        self.src_lang = LANGUAGES[self.clicked.get().lower()]
        print(self.src_lang)
        self.dest_lang = LANGUAGES[self.clicked2.get().lower()]
        print(self.dest_lang)
        self.translate()
        self.choosing_lang.destroy()

    def translate(self):
        """
            Description: This translates the file.
            Return: NONE
        """
        t = Translate(self.src_lang, self.dest_lang, self.curr_file, self.text_box)
        asyncio.run(t.output(self.text_box.get(1.0, END)))
        t.display()
        self.lectureName = self.box3.get()
        self.saveTranslated()
        # Adds the translated file to the list of files in the pancake button.
        self.fileList.append(t.file_name)

    def audioPress(self):
        """
            Description: Audio button pressed-> button prompts audio to begin recording
            Return: NONE
        """
        print("audio")
        self.stop_thread = threading.Event()
        a = Audio_to_Text(self.text_box)
        self.thread = threading.Thread(target=a.listen)
        self.thread.start()

    def savePress(self):
        """
            Description: This button allows you to save the changes you made in the text box.
            Return: None
        """

        print("Saving...")  # testing GUI buttons go to correct task
        if isinstance(self.txt_file, str):
            self.curr_file = self.txt_file
        self.txt_file = open(f'{self.curr_file}', "w")
        self.txt_file.write(self.text_box.get(1.0, END))
        self.txt_file.close()

    def pancakePress(self):
        """
            Description: Pancake button pressed-> pop up window appears to show what files have been
                        created and saved so far
            Return: NONE
        """

        if self.isPanelVisible is False:  # If the panel is not shown
            self.pancakePanel.place(x=0, y=0)  # Show the panel

            y = 0

            for item in self.fileList:      # List all the file created and creates a button for them
                button = Button(self.pancakePanel, text=item, font=("Times New Roman", 12, "bold"), background="orange",
                                command=lambda i=item: self.loadfile(i))
                button.place(x = 18, y = 40 + y)
                y += 30

            self.isPanelVisible = True      # Change state to panel shown

        else:   # If the panel is shown
            self.pancakePanel.place(x=-200, y=50)  # Make the panel disappear
            self.isPanelVisible = False     # Change state to panel not shown

    def loadfile(self,filename):
        """
        :param filename: name of the file that is being loaded
        :return: None
        """

        filepath = self.save_folder / filename

        #checks if file exists
        if not filepath.exists():
            print(f"{filename} does not exists")
            return None

        with open(filepath,"r") as f:
            text = f.read()

        self.text_box.delete("1.0","end")
        self.text_box.insert("1.0",text)

        self.curr_file = filepath
        self.txt_file = str(filepath)


    def downloadPress(self):
        """
            Description: Download button pressed-> pop up window appears to prompt user
                        to save file by a specified name.
            Return: NONE
        """

        self.savingFile = Toplevel()    # Creating pop up window
        self.savingFile.title("Naming Lecture File")
        self.savingFile.geometry("200x100")


        label = Label(self.savingFile, text = "File saves to saved_transcripts folder", font = ("Times New Roman", 10))
        label.place(x = 18, y = 10)             # Always saving files to downloads folder

        self.saveButton = Button(self.savingFile, text="Save", command=self.getFilename)
        # Creating save button on pop up window, this button saves the file to downloads folder
        self.saveButton.place(x=85, y=70)

        self.filename = Entry(self.savingFile, width=25)
        self.filename.place(x=25, y=30)  # Creating text box for user to enter a file name

    def getFilename(self):
        """
            Description: Getting file name from GUI text box
            Return: NONE
        """
        self.lectureName = self.filename.get() + ".txt"
        self.fileList.append(self.lectureName)

        self.saveFile()
        self.savingFile.destroy()

    def saveFile(self):

        '''
            Description: Saving file to save_folder
            Return: NONE
        '''

        file_path = self.save_folder / self.lectureName

        with open("output.txt", "r") as output:  # Copying contents of the output file into the file the user created
            content = output.read()

        with open(file_path, "w") as new_file:
            new_file.write(content)

        with open("output.txt", "w") as output:
            output.write("")

    def saveTranslated(self):

        '''
            Description: Saving translated file to the saved_transcripts folder and then clearing output.txt, as well.
            Return: NONE
        '''

        file_path = self.save_folder / self.lectureName


        # Copying contents of the output file into the file the user created
        with open("translated_output.txt", "r", encoding='utf-8') as output:
            content = output.read()

        with open(file_path, "w", encoding='utf-8') as new_file:
            new_file.write(content)

        with open("translated_output.txt", "w", encoding='utf-8') as output:
            output.write("")

        with open("output.txt", "w", encoding='utf-8') as output:
            output.write("")

    def audiofilepress(self):
        """
        Description: this function allows the user to select an audio file and
        trancribes it into text.
        :return: None
        """
        file_path = filedialog.askopenfilename(title="Select audio file", filetypes=[("Audio Files", "*.wav")])
        if file_path:
            transcriber = AudioFileToText(file_path)
            text = transcriber.transcribe()

            if text:
                with open("output.txt","a") as f:
                    f.write(text + "\n")
                self.text_box.insert(END,text + "\n")


class Translate:
    """
        Description: This class helps us translate the text and output it into the text_box in the GUI.
    """
    def __init__(self, src_lang, dest_lang, file_name, text_box):
        """
            Parameters:
                src_lang = the language we are translating from.
                dest_lang = the language we want to translate to.
                file_name = the name of the file that is in the text box.
                text_box = the textbox in the GUI itself.
        """
        self.src_lang = src_lang
        self.dest_lang = dest_lang
        self.file = file_name
        self.text_box = text_box
        self.trans = Translator()
        self.translation = None
        self.file_name = f"translated_output.txt"

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
        trans_file = open(f"{self.file_name}", "r+", encoding="utf-8", errors='ignore')
        trans_file.write(self.translation.text)
        trans_file.close()

    def display(self):
        """
            Description: Inserts the translated text into the GUI.
            Return: NONE
        """
        self.text_box.delete(1.0, END)
        f = open(f'{self.file_name}', "r", encoding="utf-8", errors='ignore')
        reading = f.read()
        self.text_box.insert(END, reading)
        f.close()


class Audio_to_Text(threading.Thread):

    def __init__(self, text_box):
        super(Audio_to_Text, self).__init__()
        self.recog = sr.Recognizer()
        self.text_box = text_box
        self.file = None

    def listen(self):
        with sr.Microphone() as source:
            while 1:
                try:
                    self.recog.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recog.listen(source, phrase_time_limit=1200)
                    TEXT = self.recog.recognize_google(audio)
                    print(TEXT)
                    if TEXT != "":
                        # This is a file that keeps track of what is being said, until the file is downloaded.
                        self.file = open("output.txt", "a")
                        self.file.write(TEXT + '\n')
                        self.file.close()
                        self.text_box.after(0, self.update_text_box)
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                except sr.UnknownValueError:
                    print(f"Unknown Value Error")
                    break
                except KeyboardInterrupt:
                    print("You stopped the microphone.")
                except TimeoutError:
                    print("It timed out.")

    def update_text_box(self):
        self.text_box.delete(1.0, END)
        output_file = open("output.txt", "r")
        reading = output_file.read()
        self.text_box.insert(END, reading)
        output_file.close()


class LectureBot(GUI):
    def build(self):
        """
            Description: Builds the GUI
            Return: NONE
        """
        return self


def main():
    app = LectureBot().build()
    app.run()


if __name__ == '__main__':
    main()
