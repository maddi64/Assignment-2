from tkinter import *
from Utils import Utils
from model.Animals import Animals
from AddAnimalView import AddAnimalView
from UserListView import UserListView
from model.AdoptionCentre import AdoptionCentre

class ManagerDashboardView:
    def __init__(self, root, animals):
        self.root = root
        self.adoption_centre = AdoptionCentre()
        self.animals = animals
        self.content()

    def content(self):
        self.setup_picture()
        self.setup_label()
        self.setup_filters()
        self.setup_animal_list()
        self.setup_buttons()
        
    def setup_picture(self): 
        frame = Utils.frame(self.root)
        lbl = Utils.image(self.root, 'image/cat_banner.jpg')
        lbl.pack()
        frame.pack(padx=0)

    def setup_label(self):
        separator1 = Utils.separator(self.root)
        separator1.pack(fill='x')  
        header = Utils.label(self.root, "Manager Dashboard")
        header.pack(pady=20)
        separator2 = Utils.separator(self.root)
        separator2.pack(fill='x')

    def setup_filters(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x', pady=(0, 10))

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)

        allBtn = Utils.filter_button(frame, "All", lambda: self.filter_animals("all"))
        allBtn.grid(row=0, column=0, sticky='ew')

        dogBtn = Utils.filter_button(frame, "Dog", lambda: self.filter_animals("Dog"))
        dogBtn.grid(row=0, column=1, sticky='ew')

        catBtn = Utils.filter_button(frame, "Cat", lambda: self.filter_animals("Cat"))
        catBtn.grid(row=0, column=2, sticky='ew')

        rabbitBtn = Utils.filter_button(frame, "Rabbit", lambda: self.filter_animals("Rabbit"))
        rabbitBtn.grid(row=0, column=3, sticky='ew')

    def filter_animals(self, filter_type):
        self.tree.delete(*self.tree.get_children())
        filtered_animals = self.animals.get_animals_by_filter(filter_type)
        
        for animal in filtered_animals:
            self.tree.insert("", END, values=(
                animal.get_name(),
                type(animal).__name__,
                animal.age,
                "Adopted" if animal.is_already_adopted() else "Available"
            ))

    def setup_animal_list(self):
        frame = Utils.frame(self.root)
        frame.pack(pady=20, fill='both', expand=True)
        
        columns = ("Name", "Type", "Age", "Adoption Status")
        self.tree = Utils.treeview(frame, columns)
        
        for animal in self.animals.get_animals():
            self.tree.insert("", END, values=(
                animal.get_name(),
                type(animal).__name__,
                animal.age,
                "Adopted" if animal.is_already_adopted() else "Available"
            ))
        
        self.tree.pack(fill='both', expand=True)

    def setup_buttons(self):
        frame = Utils.frame(self.root)
        frame.pack(fill='x')

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)

        viewUsersBtn = Utils.button(frame, "View Users", self.view_users)
        viewUsersBtn.grid(row=0, column=0, sticky='ew')

        addAnimalBtn = Utils.button(frame, "Add Animal", self.add_animal)
        addAnimalBtn.grid(row=0, column=1, sticky='ew')

        closeBtn = Utils.button(frame, "Close", lambda: self.root.destroy())
        closeBtn.grid(row=0, column=2, sticky='ew')

    def add_animal(self):
        add_animal_window = Utils.top_level("Add Animal")
        AddAnimalView(add_animal_window, self.adoption_centre.animals)

    def view_users(self):
        view_users_window = Utils.top_level("View User List")
        UserListView(view_users_window, self.adoption_centre.users)