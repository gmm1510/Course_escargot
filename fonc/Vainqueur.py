from tkinter import *
from time import sleep
from random import randint
from fonc.interface import*
from fonc.Escargot import*
from fonc.Vainqueur import*
#from main import canvas


class Vainqueur:
    def __init__(self, x_debut, y_debut,vainq):
        #self.vainq = vainq
        self.image = vainq
        self.canvas_img = None
        self.x_debut = x_debut
        self.y_debut = y_debut

    def Dessin(self,canvas):
        self.image = PhotoImage(file=self.image, format="gif -index 0")
        self.canvas_img = canvas.create_image(self.x_debut, self.y_debut, image=self.image)

    def vainqueur(self,canvas,x,y):
        self.x = x
        self.y = y
        self.Dessin(canvas=canvas)
        canvas.coords(self.canvas_img, x, y)