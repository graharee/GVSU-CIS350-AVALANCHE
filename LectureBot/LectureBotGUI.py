'''
    Description: This initializes the GUI and assigns the functions to each button
    Return: NONE
'''
from tkinter import *
from pathlib import Path

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
        border = Frame(self.main, bg="orange")
        border.place(x=100, y=100, width=750, height=750)

        self.square = Frame(border, bg="white")
        self.square.place(x=5, y=5, width=740, height=740)

        self.placeButtons()

        # adding pancake panel that shows all downloaded files
        self.isPanelVisible = False
        self.fileList = []

        self.pancakePanel = Frame(self.main, background = "#FFA580", width = 200, height = 850)
        label = Label(self.pancakePanel, text = "Files Saved:", font=("Times New Roman", 14, "bold"), background = "#FFA580")
        label.place(x=18, y=10)
        self.pancakePanel.place(x = -200, y = 50)

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
    def translatePress(self):
        '''
            Description: Translate button pressed-> button prompts the audio to text conversion
            Return: NONE
        '''
        print("Translating")
        # adding translating here
    def audioPress(self):
        '''
            Description: Audio button pressed-> button prompts audio to begin recording
            Return: NONE
        '''
        print("audio")
        # adding audio recording here

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
