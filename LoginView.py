import sys
import os
from tkinter import *

# Temporarily add model directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'model'))

from tkinter import *
from CustomerDashboardView import CustomerDashboardView
from ManagerDashboardView import ManagerDashboardView
from ErrorView import ErrorView
from model.User import User
from model.Users import Users
from model.AdoptionCentre import AdoptionCentre
from Utils import Utils  

class LoginView:    
    def __init__(self, root):
        self.root = root 
        self.adoption_centre = AdoptionCentre()
        self.users = self.adoption_centre.get_users()
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
        self.usernameTxt.bind('<KeyRelease>', self.on_customer_input)
        
        self.emailTxt = Entry(frame, relief=FLAT)
        self.emailTxt.grid(row=1, column=1)
        self.emailTxt.bind('<KeyRelease>', self.on_customer_input)

        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')

    def setup_manager(self):
        frame = Utils.frame(self.root)
        frame.pack(pady=20)

        managerLbl = Utils.label(frame, "Manager ID:")
        managerLbl.grid(row=0, column=0, sticky=W)

        self.managerTxt = Entry(frame, relief=FLAT)
        self.managerTxt.grid(row=0, column=1)
        self.managerTxt.bind('<KeyRelease>', self.on_manager_input)

        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')

    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        self.loginBtn = Utils.button(frame, "Login", self.handle_login)
        self.loginBtn.grid(row=0, column=0, sticky='ew')
        self.loginBtn['state'] = 'disabled'

        exitBtn = Utils.button(frame, "Exit", lambda: self.root.quit())
        exitBtn.grid(row=0, column=1, sticky='ew')

    def on_customer_input(self, event=None):
        username = self.usernameTxt.get().strip()
        email = self.emailTxt.get().strip()
        
        if username or email:
            self.managerTxt.config(state='disabled')
            self.loginBtn['state'] = 'normal' if username and email else 'disabled'
        else:
            self.managerTxt.config(state='normal')
            self.loginBtn['state'] = 'disabled'

    def on_manager_input(self, event=None):
        manager_id = self.managerTxt.get().strip()
        
        if manager_id:
            self.usernameTxt.config(state='disabled')
            self.emailTxt.config(state='disabled')
            self.loginBtn['state'] = 'normal'
        else:
            self.usernameTxt.config(state='normal')
            self.emailTxt.config(state='normal')
            self.loginBtn['state'] = 'disabled'
        
    def handle_login(self):
        username = self.usernameTxt.get().strip()
        email = self.emailTxt.get().strip()
        managerid = self.managerTxt.get().strip()

        if managerid:
            try:
                user = self.users.validate_manager(managerid)
                if user:
                    self.manager_login()
            except Exception as e:
                error_window = Utils.top_level("Error")
                ErrorView(error_window)
        elif username and email:
            user = self.users.validate_customer(username, email)
            if user:
                self.customer_login()
            else:
                error_window = Utils.top_level("Error")
                ErrorView(error_window)

    def customer_login(self):
        customer_window = Utils.top_level("Customer View")
        user = self.users.validate_customer(self.usernameTxt.get().strip(), self.emailTxt.get().strip())
        self.root.withdraw()  # Hide login window
        CustomerDashboardView(customer_window, self.adoption_centre.animals, user)
        customer_window.bind("<<DashboardClosed>>", lambda e: self.on_dashboard_close())

    def manager_login(self):
        manager_window = Utils.top_level("Manager View")
        self.root.withdraw()  # Hide login window
        ManagerDashboardView(manager_window, self.adoption_centre.animals)
        manager_window.bind("<<DashboardClosed>>", lambda e: self.on_dashboard_close())

    def on_dashboard_close(self):
        self.root.deiconify()  # Show login window again

if __name__ == '__main__':
    root = Utils.root()  # Should return a Tk() instance
    LoginView(root)
    root.mainloop()