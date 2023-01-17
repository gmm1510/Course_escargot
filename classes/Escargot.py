
from tkinter import *
from PIL import Image
from PIL import ImageTk



class Escargot:
    def __init__(self, nom, x, y, fichier_image):
        self.nom=nom
        self.x=x
        self.y=y
        self.image = Image.open(fichier_image)
        self.canvas_image = None
        self.x_depart=x
        self.y_depart =y
        self.finished=False

    def dessin(self, canvas):
        self.image = ImageTk.PhotoImage(self.image)
        self.canvas_image = canvas.create_image(self.x, self.y, image=self.image) # Je crée l'image de l'escargot passé dans l'argument "image" sur le canvas aux coordonnées x et y

    def mouvement(self,canvas, x_move, y_move):
        self.x+=x_move
        self.y+=y_move
        canvas.coords(self.canvas_image, self.x, self.y)
        if self.x>=900:
            self.finished=True






