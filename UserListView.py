from tkinter import *
from Utils import Utils
from model.Users import Users
from model.Customer import Customer
from model.Manager import Manager

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

    def setup_user_list(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='both', expand=True)
        
        self.tree = Utils.treeview(frame, [""], multi=False)
        self.tree["show"] = "" 

        for user in self.users.get_users():
            if user.__class__.__name__ == "Customer":
                self.tree.insert("", END, values=(
                    f"{user.get_name()} ({user.get_email()})",
                    "Customer"
                ))
            elif user.__class__.__name__ == "Manager":
                self.tree.insert("", END, values=(
                    f"{user.get_name()} (Manager)",
                    "Manager"
                ))
        
        self.tree.pack(fill='both', expand=True)


        # listbox_frame = Frame(frame)
        # listbox_frame.pack(fill='both', expand=True, padx=20)
        
        # for user in self.users.get_users():
        #     user_frame = Frame(listbox_frame)
        #     user_frame.pack(fill='x', pady=2)
            
        #     if user.__class__.__name__ == "Customer":
        #         user_label = Label(user_frame, text=f"{user.get_name()} ({user.get_email()})")
        #         user_label.pack(fill='x')
        #     elif user.__class__.__name__ == "Manager":
        #         user_label = Label(user_frame, text=f"{user.get_name()} (Manager)")
        #         user_label.pack(fill='x')

    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')

        frame.grid_columnconfigure(0, weight=1)

        closeBtn = Utils.button(frame, "Close", lambda: self.root.destroy())
        closeBtn.grid(row=0, column=0, sticky='ew')
