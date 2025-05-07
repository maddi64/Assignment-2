from tkinter import *
from Utils import Utils
from model.Users import Users

class UserListView:
    def __init__(self, root, users):
        self.root = root
        self.users = users
        self.content()

    def content(self):
        self.setup_picture()
        self.setup_label()
        self.setup_user_list()
        self.setup_buttons()
        
    def setup_picture(self): 
        frame = Utils.frame(self.root)
        lbl = Utils.image(self.root, 'image/cat_banner.jpg')
        lbl.pack()
        frame.pack(padx=0)

    def setup_label(self):
        separator1 = Utils.separator(self.root)
        separator1.pack(fill='x')  
        header = Utils.label(self.root, "User List")
        header.pack(pady=20)
        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')

    def setup_user_list(self):
        frame = Utils.frame(self.root)
        frame.pack(pady=20, fill='both', expand=True)
        
        for user in self.users.get_users():
            Utils.label(self.root, user.get_name())
            
        frame.pack(fill='both', expand=True)
        
        

    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')

        frame.grid_columnconfigure(0, weight=1)

        closeBtn = Utils.button(frame, "Close", lambda: self.root.destroy())
        closeBtn.grid(row=0, column=0, sticky='ew')

