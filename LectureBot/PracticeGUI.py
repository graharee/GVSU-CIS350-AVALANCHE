from tkinter import *
 #windows hold widgets

class GUI:
    def __init__(self):
        '''
            Description:
            Parameter "":
            Parameter "":
            Return:
        '''
        window = Tk()
        window.geometry("1800x900")
        window.configure(background = "white")
        window.title("LectureBot")
        logo = PhotoImage(file='logo.png')
        window.iconphoto(True, logo)

        downloadButton = PhotoImage(file='download.png')

        audioButton = Button(window, image= downloadButton, command=self.buttonTest)

        audioButton.config(command = self.buttonTest) #performs callback of function
        audioButton.config(width = "44", height = "50")
        audioButton.place()
        audioButton.pack()
        window.mainloop()

    def buttonTest(self):
        print("hi")

def main():
    g = GUI()


if __name__ == '__main__':
    main()