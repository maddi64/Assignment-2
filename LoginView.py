import sys
import os
from tkinter import *

# Temporarily add model directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'model'))

from tkinter import *
from CustomerDashboardView import CustomerDashboardView
from ManagerDashboardView import ManagerDashboardView
from model.User import User
from model.Users import Users
from Utils import Utils  

class LoginView:    
    def __init__(self, root):
        self.root = root 
        self.users = Users()
        self.content()

    def content(self):
        self.setup_picture()
        self.setup_label()
        self.setup_customer()
        self.setup_manager()
        self.setup_buttons()
    
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

    def setup_customer(self):
        frame = Utils.frame(self.root)
        frame.pack(padx=10, pady=20)
        
        usernameLbl = Utils.label(frame, "Username:")
        usernameLbl.grid(row=0, column=0, sticky=W)
        
        emailLbl = Utils.label(frame, "Email:")
        emailLbl.grid(row=1, column=0, sticky=W)
        
        self.usernameTxt = Entry(frame, relief=FLAT)
        self.usernameTxt.grid(row=0, column=1)
        
        self.emailTxt = Entry(frame, relief=FLAT)
        self.emailTxt.grid(row=1, column=1)

        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')

    def setup_manager(self):
        frame = Utils.frame(self.root)
        frame.pack(pady=20)

        managerLbl = Utils.label(frame, "Manager ID:")
        managerLbl.grid(row=0, column=0, sticky=W)

        self.managerTxt = Entry(frame, relief=FLAT)
        self.managerTxt.grid(row=0, column=1)

        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')
        

    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        loginBtn = Utils.button(frame, "Login", self.handle_login)
        loginBtn.grid(row=0, column=0, sticky='ew')

        exitBtn = Utils.button(frame, "Exit")
        exitBtn.grid(row=0, column=1, sticky='ew')
        
    def handle_login(self):
        username = self.usernameTxt.get().strip()
        email = self.emailTxt.get().strip()
        managerid = self.managerTxt.get().strip()


        if not username and not email:
            user = self.users.validate_manager(managerid)

        else:
            self.customer_login()

    def customer_login(self):
        customer_window = Utils.top_level("Customer View")
        CustomerDashboardView(customer_window)

    def manager_login(self):
        
        manager_window = Utils.top_level("Manager View")
        ManagerDashboardView(manager_window)


if __name__ == '__main__':
    root = Utils.root()  # Should return a Tk() instance
    LoginView(root)
    root.mainloop()
