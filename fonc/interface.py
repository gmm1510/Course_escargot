from tkinter import *
from fonc.Course import*
from fonc.Escargot import*
#from PIL import Image
#from PIL import ImageTk

#from main import course


class interface:
    def __init__(self, root, course, canvas):
        self.root = root
        self.course = course
        #self.canvas = Canvas(root, width=1100, height=600, bg='white')
        #self.canvas.pack(side=TOP, padx=5, pady=5)

        # Placement des boutons
        self.reset_button = Button(root, text="Nouvelle Course", command=course.reinitialiser)
        self.reset_button.pack(side=LEFT)
        self.start_button = Button(root, text='Partez !', width=15, command=course.start)
        self.start_button.pack(side=LEFT)
        self.quit_button = Button(root, text='Quitter', width=15, command=root.quit)
        self.quit_button.pack(side=RIGHT)

        # Dessin des éléments de décors
        canvas.create_line(940, 0, 940, 600, width=5, fill="red")
        canvas.create_line(250, 0, 250, 600, width=5, fill="green")
        canvas.create_line(0, 150, 1100, 150, width=5, fill="black")
        canvas.create_line(0, 300, 1100, 300, width=5, fill="black")
        canvas.create_line(0, 450, 1100, 450, width=5, fill="black")
