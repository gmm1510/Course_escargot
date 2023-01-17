
from classes.Escargot import*
from classes.Course import*
from utilitaires.fonctions import*
# On crée 4 instances de la classe Escargot
escargot1 = Escargot("escargot1", 130, 75, "escargot1.gif")
escargot2 = Escargot("escargot2", 130, 225, "escargot2.gif")
escargot3 = Escargot("escargot3", 130, 375, "escargot3.gif")
escargot4 = Escargot("escargot4", 130, 525, "escargot6.jpg")

# On dessine la fenêtre
fen=Tk()
fen.title("Championnat Course d'escargots")
canvas = Canvas(fen, width=1100, height=600, bg ='white')
canvas.pack(side=TOP, padx=5, pady=5)

list_escargot = [escargot1, escargot2, escargot3, escargot4]
course = Course(list_escargot, canvas)

# Placer le boutton "Reinitialiser"
Reinitialiser = Button(fen, text="Nouvelle Course", command=course.reinitialiser)
Reinitialiser.pack(side=LEFT)

# creation du boutton "Demarrer" permettant de lancer la course
b1=Button(fen,text='Partez !', width=15, command=course.start)
b1.pack(side=LEFT)

b3 = Button(fen, text='Quitter', width=15, command=fen.quit)
b3.pack(side=RIGHT)


# décor
canvas.create_line(940, 0, 940, 600, width=5, fill="red")
canvas.create_line(250, 0, 250, 600, width=5, fill="green")
canvas.create_line(0, 150, 1100, 150, width=5, fill="black")
canvas.create_line(0, 300, 1100, 300, width=5, fill="black")
canvas.create_line(0, 450, 1100, 450, width=5, fill="black")


# On dessine les escargots avec la methode dessin sur le canvas
escargot1.dessin(canvas)
escargot2.dessin(canvas)
escargot3.dessin(canvas)
escargot4.dessin(canvas)



#course.start()
vainqueur = course.get_winner()
print("Le vainqueur est:", vainqueur)
fen.mainloop()
#fen.destroy()