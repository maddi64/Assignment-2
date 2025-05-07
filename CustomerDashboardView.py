from tkinter import *
from Utils import Utils
from DetailsView import DetailsView
#from model.AdoptionCentre import AdoptionCentre

class CustomerDashboardView:
    def __init__(self, root):
            self.root = root  
            self.content()

    def content(self):
        self.setup_picture()
        self.setup_label()
        self.setup_buttons()
        
    def setup_picture(self): 
        frame = Utils.frame(self.root)
        lbl = Utils.image(self.root, 'image/cat_banner.jpg')
        lbl.pack()
        frame.pack(padx=(0,0))

    def setup_label(self):
        separator1 = Utils.separator(self.root)
        separator1.pack(fill='x')  
        applicationTitle = "Welcome XX"
        header = Utils.label(self.root, applicationTitle)
        header.pack(pady=20)
        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')

    
                
         
    
    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')  # Make frame expand horizontally

        frame.grid_columnconfigure(0, weight=1)  # Column 0 expands
        frame.grid_columnconfigure(1, weight=1)  # Column 1 expands
        frame.grid_columnconfigure(2, weight=1)  # Column 2 expands

        loginBtn = Utils.button(frame, "My Detais", self.open_customer_details_view)
        loginBtn.grid(row=0, column=0, sticky='ew')

        exitBtn = Utils.button(frame, "Adopt")
        exitBtn.grid(row=0, column=1, sticky='ew')

        exitBtn = Utils.button(frame, "Close")
        exitBtn.grid(row=0, column=2, sticky='ew')

    def open_customer_details_view(self):
        #customer_details_window = Utils.top_level("Customer Details View")
        #DetailsView(customer_details_window)
        pass
