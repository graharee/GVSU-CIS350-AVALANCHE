from tkinter import *

class GUI:
    def __init__(self):
        '''
            Description:
            Parameter "":
            Parameter "":
            Return:
        '''

        self.main = Tk()
        self.main.geometry("900x900")
        self.main.configure(background = "white")
        self.main.title("LectureBot")
        logo = PhotoImage(file='logo.png')
        self.main.iconphoto(True, logo)
        self.counter = 0

        border = Frame(self.main, bg="orange")
        border.place(x=100, y=100, width=750, height=750)

        self.square = Frame(border, bg="white")
        self.square.place(x=5, y=5, width=740, height=740)

        downloadButtonImg = PhotoImage(file='download.png')
        pancakeButtonImg = PhotoImage(file='pancake.png')
        micButtonImg = PhotoImage(file='mic.png')

        downloadButton = Button(self.main, image = downloadButtonImg, command = self.downloadPress)
        pancakeButton = Button(self.main, image = pancakeButtonImg, command = self.pancakePress)
        micButton = Button(self.square, image = micButtonImg, command = self.buttonTest)
        transcriptButton = Button(self.main, text = "T", command = self.buttonTest)

        transcriptButton.config(font=("Times New Roman", 21, "bold"), background="white", width="1",height="1")  # performs callback of function
        transcriptButton.place(x=825, y=0)

        downloadButton.config(width="44", height="50")
        downloadButton.place(x=850, y=0)

        pancakeButton.config(width="58", height="50")
        pancakeButton.place(x=0, y=0)

        micButton.config(width="237", height="200")
        micButton.place(x=250, y=450)

        self.main.mainloop()
    def buttonTest(self):
        print("hi")

    def pancakePress(self):
        print("yo")

    def downloadPress(self):
        namingFile = Toplevel()
        namingFile.title("Naming Lecture File")
        namingFile.geometry("200x100")

        closeButton = Button(namingFile, text = "Save", command = namingFile.destroy)
        closeButton.place(x=50, y=50)

def main():
    g = GUI()


if __name__ == '__main__':
    main()