from tkinter import *
from model.AdoptionCentre import AdoptionCentre
from model.Animal import Cat
from model.exception.InvalidOperationException import InvalidOperationException
from model.Animals import Animals
from Utils import Utils  

class AddAnimalView:
    def __init__(self, root, animals):
        self.root = root  
        self.animals = animals
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
        

        # types = ["Cat", "Dog", "Rabbit"]
        # self.typeMenu = OptionMenu(frame, "Cat", *types)
        # self.typeMenu.grid(row=0, column=1)
        
        self.typeMenu = Entry(frame, relief=FLAT)
        self.typeMenu.grid(row=0, column=1)
        
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
        type = self.typeMenu.get()
        name = self.nameTxt.get().strip()
        age = self.AgeTxt.get().strip()

        try:
            age = int(age)
        except:
            raise InvalidOperationException("Age must be an integer")
        
        newAnimal = self.animals.add(Cat(name, age))

        for animal in self.animals.get_animals():
            if animal == newAnimal:
                raise InvalidOperationException(animal.get_name() + " already exists in the adoption centre")


