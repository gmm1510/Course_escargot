from tkinter import *
from fonc.Course import*
from fonc.interface import*
from time import sleep
from random import randint
from PIL import Image
from PIL import ImageTk

class Escargot:
    def __init__(self, nom, x, y, fichier_image, canvas):
        self.nom = nom
        self.x = x
        self.y = y
        self.image = fichier_image
        self.gif = None
        self.canvas = canvas
        self.canvas_image = None
        self.x_depart = x
        self.y_depart = y
        self.finished = False
        self.gif_state = 0

    def dessin(self, canvas):
        self.gif = PhotoImage(file=self.image, format=f"gif -index {str(self.gif_state)}")
        self.canvas_image = canvas.create_image(self.x, self.y, image=self.gif) # Je crée l'image de l'escargot passé dans l'argument "image" sur le canvas aux coordonnées x et y
        if self.gif_state < 11:
            self.gif_state += 1
        else:
            self.gif_state = 0
        self.canvas.update()

    def mouvement(self,canvas, x_move, y_move):
        self.x += x_move
        self.y += y_move

        self.dessin(canvas=canvas)
        canvas.coords(self.canvas_image, self.x, self.y)

        if self.x >= 900:
            self.finished = True