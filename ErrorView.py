from tkinter import *
from Utils import Utils

class ErrorView:
    def __init__(self, root, error_message):
        self.root = root  
        self.error_message = error_message
        self.content()

    def content(self):
        self.setup_picture()
        self.setup_err_label()
        self.setup_label()
        self.setup_buttons()

    def setup_picture(self): 
        frame = Utils.frame(self.root)
        lbl = Utils.image(self.root, 'image/error_banner.jpg')
        lbl.pack()
        frame.pack(padx=0)

    def setup_err_label(self):
        separator1 = Utils.separator(self.root)
        separator1.pack(fill='x')  
        print(self.error_message)
        if self.error_message == "Invalid manager credentials":
            header = Label(self.root, text="UnauthorizedAccessException", font="Courier 14 bold", foreground="red")
        else:
            header = Label(self.root, text="InvalidOperationException", font="Courier 14 bold", foreground="red")
        header.pack(pady=20)

    def setup_label(self):
        separator1 = Utils.separator(self.root)
        separator1.pack(fill='x')  
        header = Label(self.root, text=self.error_message, font="Helvetica 10 bold", foreground=Utils.purple)
        header.pack(pady=20)

    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')

        closeBtn = Utils.button(frame, "Close", lambda: self.root.destroy())
        closeBtn.pack(fill='x')