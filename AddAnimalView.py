from tkinter import *
from model.AdoptionCentre import AdoptionCentre
from model.Animal import Cat, Dog, Rabbit
from model.exception.InvalidOperationException import InvalidOperationException
from model.Animals import Animals
from Utils import Utils
from ErrorView import ErrorView

class AddAnimalView:
    def __init__(self, root, animals, manager_dashboard=None):
        self.root = root  
        self.animals = animals
        self.manager_dashboard = manager_dashboard
        self.content()

    def content(self):
        self.setup_picture()
        self.setup_label()
        self.setup_add_animal()
        self.setup_buttons()
    
    def setup_picture(self): 
        frame = Utils.frame(self.root)
        lbl = Utils.image(self.root, 'image/cat_banner.jpg')
        lbl.pack()
        frame.pack(padx=0)

    def setup_label(self):
        separator1 = Utils.separator(self.root)
        separator1.pack(fill='x')  
        header = Utils.label(self.root, "Add Animal")
        header.pack(pady=20)
        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')

    def setup_add_animal(self):
        frame = Utils.frame(self.root)
        frame.pack(padx=10, pady=20)
        
        typeLbl = Utils.label(frame, "Type:")
        typeLbl.grid(row=0, column=0, sticky=W)
        
        nameLbl = Utils.label(frame, "Name:")
        nameLbl.grid(row=1, column=0, sticky=W)

        AgeLbl = Utils.label(frame, "Age:")
        AgeLbl.grid(row=3, column=0, sticky=W)
        
        self.type_var = StringVar(frame)
        self.type_var.set("Cat")  # Set default value
        types = ["Cat", "Dog", "Rabbit"]
        self.typeMenu = OptionMenu(frame, self.type_var, *types)
        self.typeMenu.config(width=15)
        self.typeMenu.grid(row=0, column=1, sticky='w')
        
        self.nameTxt = Entry(frame, relief=FLAT)
        self.nameTxt.grid(row=1, column=1)

        self.AgeTxt = Entry(frame, relief=FLAT)
        self.AgeTxt.grid(row=3, column=1)

        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')

    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        self.addBtn = Utils.button(frame, "Add", self.add_animal)
        self.addBtn.grid(row=0, column=0, sticky='ew')

        closeBtn = Utils.button(frame, "Close", lambda: self.root.destroy())
        closeBtn.grid(row=0, column=1, sticky='ew')

    def add_animal(self):
        try:
            animal_type = self.type_var.get()
            name = self.nameTxt.get().strip()
            
            try:
                age = int(self.AgeTxt.get().strip())
            except ValueError:
                raise InvalidOperationException("Age must be an integer")

            # Check if animal already exists
            for existing_animal in self.animals.get_animals():
                if existing_animal.get_name() == name:
                    raise InvalidOperationException(f"{name} already exists in the adoption centre")

            # Create the appropriate animal type
            new_animal = None
            if animal_type == "Cat":
                new_animal = Cat(name, age)
            elif animal_type == "Dog":
                new_animal = Dog(name, age)
            elif animal_type == "Rabbit":
                new_animal = Rabbit(name, age)

            self.animals.add(new_animal)
            
            # Refresh the manager dashboard if it exists
            if self.manager_dashboard:
                self.manager_dashboard.refresh_animal_list()
                
            self.root.destroy()  # Close the add animal window
            
        except InvalidOperationException as e:
            error_window = Utils.top_level("Error")
            ErrorView(error_window)
