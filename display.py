import tkinter as tk
from PIL import Image, ImageTk

class Display:

    '''
    Constructor
    Constructs the Display class and prepares it for displaying an image with the size image_width, image_height.
    This function doesn't start the tkinter main thread. This is done by the startWindowLoop() function. This
    prevents direct blocking from the tkinter main loop.
    '''
    def __init__(self, image_width: int, image_height: int):
        self.image_width = image_width
        self.image_height = image_height

        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(image_width*2, image_height))

        self.frame = tk.Frame(self.window)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(fill=tk.BOTH, expand=True)


        empty_image_left = Image.new('RGB', (image_width, image_height), (0, 0, 0))
        self.displayable_image_left = ImageTk.PhotoImage(empty_image_left)

        empty_image_right = Image.new('RGB', (image_width, image_height), (0, 0, 0))
        self.displayable_image_right = ImageTk.PhotoImage(empty_image_right)

        self.frame.frame_image_left = self.canvas.create_image((image_width/2, image_height/2), image=self.displayable_image_left)
        self.frame.frame_image_right = self.canvas.create_image((image_width/2, image_height/2), image=self.displayable_image_right)
        self.canvas.move(self.frame.frame_image_right, image_width, 0)

        self.frame.pack(fill=tk.BOTH, expand=True)


    '''
    Starts the window loop, this function is blocking for anything that comes after this function until the window
    is closed down. 
    '''
    def startWindowLoop(self):
        self.window.mainloop()

    '''
    This function allows to change the left image
    '''
    def changeImageLeft(self, new_image: Image):
        self.displayable_image_left = ImageTk.PhotoImage(new_image)
        self.image_left = new_image
        self.frame.frame_image_left = self.canvas.create_image((self.image_width / 2, self.image_height / 2), image=self.displayable_image_left)

        #self.displayable_image = ImageTk.PhotoImage(new_image)
        #self.panel.configure(image=self.displayable_image)
        #self.panel.image=self.displayable_image


    '''
    This function allows to change the right image
    '''
    def changeImageRight(self, new_image: Image):
        self.displayable_image_right = ImageTk.PhotoImage(new_image)
        self.image_right = new_image
        self.frame.frame_image_right = self.canvas.create_image((self.image_width / 2, self.image_height / 2), image=self.displayable_image_right)
        self.canvas.move(self.frame.frame_image_right, self.image_width, 0)

