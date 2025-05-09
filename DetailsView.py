from tkinter import *
from Utils import Utils

class DetailsView:
    def __init__(self, root, customer):
        self.root = root
        self.customer = customer
        self.content()

    def content(self):
        self.setup_picture()
        self.setup_label()
        self.setup_adopted_animals()
        self.setup_buttons()
        
    def setup_picture(self): 
        frame = Utils.frame(self.root)
        lbl = Utils.image(self.root, 'image/cat_banner.jpg')
        lbl.pack()
        frame.pack(padx=0)

    def setup_label(self):
        separator1 = Utils.separator(self.root)
        separator1.pack(fill='x')  
        header = Utils.label(self.root, f"{self.customer.get_name()}")
        header.pack(pady=20)
        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')
        header2 = Utils.label(self.root, "Adopted Animals")
        header2.pack(pady=20)
        separator3 = Utils.separator(self.root)
        separator3.pack(fill='x')

    def setup_adopted_animals(self):
        list_frame = Utils.frame(self.root)
        list_frame.pack(fill='both', expand=True)
        
        adopted_animals = self.customer.get_adopted_animals().get_animals()
        if adopted_animals:
            for animal in adopted_animals:
                animal_label = Label(list_frame, 
                                   text=f"{animal.get_name()} ({type(animal).__name__}, Age: {animal.age})")
                animal_label.pack(fill='x', pady=2)
        else:
            no_animals_label = Label(list_frame,
                                   text="No animals adopted yet")
            no_animals_label.pack(fill='x', pady=2)

    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')

        frame.grid_columnconfigure(0, weight=1)

        closeBtn = Utils.button(frame, "Close", lambda: self.root.destroy())
        closeBtn.grid(row=0, column=0, sticky='ew')
