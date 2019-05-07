from tkinter import *
from PIL import Image, ImageTk

class Display:

    '''
    Constructor
    Constructs the Display class and prepares it for displaying an image with the size image_width, image_height.
    This function doesn't start the tkinter main thread. This is done by the startWindowLoop() function. This
    prevents direct blocking from the tkinter main loop.
    '''
    def __init__(self, image_width: int, image_height: int):
        self.window = Tk()

        empty_image = Image.new('RGB', (image_width, image_height), (0, 0, 0))
        self.displayable_image = ImageTk.PhotoImage(empty_image)

        self.panel = Label(self.window, image=self.displayable_image)
        self.panel.pack(side="bottom", fill="both", expand="yes")

    '''
    Starts the window loop, this function is blocking for anything that comes after this function until the window
    is closed down. 
    '''
    def startWindowLoop(self):
        self.window.mainloop()

    '''
    This function allows displayed images to be changed
    '''
    def changeImage(self, new_image: Image):
        self.displayable_image = ImageTk.PhotoImage(new_image)
        self.panel.configure(image=self.displayable_image)
        self.panel.image=self.displayable_image

