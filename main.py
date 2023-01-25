
from classes.Escargot import*
from classes.Course import*
from utilitaires.fonctions import*
from classes.Interface import*
from tkinter import*
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

escargot1.dessin(canvas)
escargot2.dessin(canvas)
escargot3.dessin(canvas)
escargot4.dessin(canvas)

list_escargot = [escargot1, escargot2, escargot3, escargot4]

course = Course(list_escargot, canvas)
interface=Interface(fen,course,canvas)

texte=StringVar()

texteLabel=Label(fen, textvariable=texte)
texteLabel.pack()

texte.set("Que le meilleur gagne !")


# On dessine les escargots avec la methode dessin sur le canvas



#course.start()
#vainqueur = course.get_winner()
#print("Le vainqueur est:", vainqueur)
fen.mainloop()

#fen.destroy()