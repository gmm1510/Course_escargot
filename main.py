from tkinter import *
from fonc.Course import*
from fonc.interface import*
from fonc.Escargot import*
from time import sleep
from keyboard import*
from fonc.Thread import*
import pygame as py
import os

if __name__ == '__main__':


    # On dessine la fenêtre
    fen=Tk()
    #MusicPlayer(root)
    fen.title("Championnat : Course d'escargots")
    canvas = Canvas(fen, width=1100, height=600, bg ='white')
    canvas.pack(side=TOP, padx=5, pady=5)
    bg = PhotoImage(file="gazon2.png")
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # On crée 4 instances de la classe Escargot
    esca1 = Escargot("escargot 1", 190, 75, "ezgifj.gif",canvas)
    esca2 = Escargot("escargot 2", 190, 225, "ezgifm.gif",canvas)
    esca3 = Escargot("escargot 3", 190, 375, "ezgifr.gif",canvas)
    esca4 = Escargot("escargot 4", 190, 525, "ezgifv.gif",canvas)

    texte = StringVar()
    textLab = Label(fen, textvariable=texte)
    textLab.pack()
    texte.set("Que le meilleur gagne !")

    #start_T(canvas)

    list_escargot = [esca1, esca2, esca3, esca4]
    course = Course(list_escargot, canvas)
    interface = interface(fen, course, canvas)






    # On dessine les escargots avec la methode dessin sur le canvas
    esca1.dessin(canvas)
    esca2.dessin(canvas)
    esca3.dessin(canvas)
    esca4.dessin(canvas)

    #course.start()
    #vainqueur = course.get_winner()
    #print("Le vainqueur est:", vainqueur)
    fen.mainloop()

    #fen.destroy()


    # son ? keyboard ?