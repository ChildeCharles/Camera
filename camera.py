import tkinter as tk
from scene import Scene


class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.pack()
        self.scene = Scene(self, width=800, height=800, background_color="white")

        self.bind("<w>", self.scene.move_handler)
        self.bind("<s>", self.scene.move_handler)
        self.bind("<a>", self.scene.move_handler)
        self.bind("<d>", self.scene.move_handler)
        self.bind("<Up>", self.scene.move_handler)
        self.bind("<Down>", self.scene.move_handler)

        self.bind("<Control-w>", self.scene.rotate_handler)
        self.bind("<Control-s>", self.scene.rotate_handler)
        self.bind("<Control-a>", self.scene.rotate_handler)
        self.bind("<Control-d>", self.scene.rotate_handler)
        self.bind("<Control-Up>", self.scene.rotate_handler)
        self.bind("<Control-Down>", self.scene.rotate_handler)

        self.bind("<plus>", self.scene.zoom_handler)
        self.bind("<minus>", self.scene.zoom_handler)
        self.bind("<KP_Add>", self.scene.zoom_handler)
        self.bind("<KP_Subtract>", self.scene.zoom_handler)


root = tk.Tk()
application = Application(master=root)
application.focus_set()
application.mainloop()
