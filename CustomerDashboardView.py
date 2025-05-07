from tkinter import *
from Utils import Utils
from DetailsView import DetailsView
from model.Animals import Animals
from model.AdoptionCentre import AdoptionCentre

class CustomerDashboardView:
    def __init__(self, root, animals, customer=None):
        self.root = root  
        self.animals = animals
        self.customer = customer
        self.content()

    def content(self):
        self.setup_picture()
        self.setup_label()
        self.setup_animal_list()
        self.setup_buttons()
        
    def setup_picture(self): 
        frame = Utils.frame(self.root)
        lbl = Utils.image(self.root, 'image/cat_banner.jpg')
        lbl.pack()
        frame.pack(padx=(0,0))

    def setup_label(self):
        separator1 = Utils.separator(self.root)
        separator1.pack(fill='x')  
        applicationTitle = "Welcome to the Adoption Centre"
        header = Utils.label(self.root, applicationTitle)
        header.pack(pady=20)
        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')

    def setup_animal_list(self):
        frame = Utils.frame(self.root)
        frame.pack(pady=20, fill='both', expand=True)
        
        columns = ("Name", "Type", "Age", "Adoption Status")
        self.tree = Utils.treeview(frame, columns)
        
        for animal in self.animals.get_animals():
            if not animal.is_already_adopted():
                self.tree.insert("", END, values=(
                    animal.get_name(),
                    type(animal).__name__,
                    animal.age,
                    "Available"
                ))
        
        self.tree.pack(fill='both', expand=True)
                
    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')  

        frame.grid_columnconfigure(0, weight=1)  
        frame.grid_columnconfigure(1, weight=1)  
        frame.grid_columnconfigure(2, weight=1)  

        loginBtn = Utils.button(frame, "My Details", self.open_customer_details_view)
        loginBtn.grid(row=0, column=0, sticky='ew')

        adoptBtn = Utils.button(frame, "Adopt", self.adopt)
        adoptBtn.grid(row=0, column=1, sticky='ew')

        closeBtn = Utils.button(frame, "Close", lambda: self.root.destroy())
        closeBtn.grid(row=0, column=2, sticky='ew')

    def open_customer_details_view(self):
        customer_details_window = Utils.top_level("Customer Details View")
        DetailsView(customer_details_window, self.customer)

    def adopt(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return
            
        item = self.tree.item(selected_item[0])
        animal_name = item['values'][0]
        
        animal = self.animals.animal(animal_name)
        if animal and not animal.is_already_adopted():
            if self.customer.can_adopt(animal):
                animal.adopt()
                self.customer.get_adopted_animals().add(animal)
                self.tree.delete(selected_item)
