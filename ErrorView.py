from tkinter import *
from Utils import Utils

class ErrorView:
    def __init__(self, root):
        self.root = root  
        self.content()

    def content(self):
        self.setup_picture()
        self.setup_label()
        # self.setup_buttons()

    def setup_picture(self): 
        frame = Utils.frame(self.root)
        lbl = Utils.image(self.root, 'image/cat_banner.jpg')
        lbl.pack()
        frame.pack(padx=0)

    def setup_label(self):
        separator1 = Utils.separator(self.root)
        separator1.pack(fill='x')  
        header = Utils.label(self.root, "Login")
        header.pack(pady=20)
        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')
