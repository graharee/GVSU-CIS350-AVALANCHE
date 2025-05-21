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
        window.geometry("900x900")
        window.configure(background = "white")
        window.title("LectureBot")
        logo = PhotoImage(file='logo.png')
        window.iconphoto(True, logo)

        downloadButtonImg = PhotoImage(file = 'download.png')
        pancakeButtonImg = PhotoImage(file = 'pancake.png')

        downloadButton = Button(window, image= downloadButtonImg, command=self.buttonTest)
        pancakeButton = Button(window, image=pancakeButtonImg, command=self.buttonTest)

        downloadButton.config(command = self.buttonTest) #performs callback of function
        downloadButton.config(width = "44", height = "50")
        downloadButton.place(x=850, y=0)

        pancakeButton.config(command=self.buttonTest)  # performs callback of function
        pancakeButton.config(width="58", height="50")
        pancakeButton.place(x=0, y=0)

        window.mainloop()

    def buttonTest(self):
        print("hi")

def main():
    g = GUI()


if __name__ == '__main__':
    main()