from time import sleep
from random import randint

#from main import canvas


class Course:
    def __init__(self, liste_escargots, canvas):
        self.liste_escargots = liste_escargots
        self.canvas = canvas
        self.partez = None


    def start(self):
       # print(self.vainqueur)
        self.partez=True
        while self.partez:
            for escargot in self.liste_escargots:
                x_move = randint(0, 2)
                y_move = 0

                if escargot.finished:
                    print(f"{escargot.nom} a gagné")
                    self.partez = False
                else:
                    escargot.mouvement(self.canvas, x_move, y_move)

            sleep(0.0001)
            self.canvas.update()

        # On efface cette donnée pour permettre de relancer une nouvelle course grâce à la condition du while



    def reinitialiser(self):
        for escargot in self.liste_escargots:
            escargot.x = escargot.x_depart
            escargot.y = escargot.y_depart
            self.canvas.coords(escargot.canvas_image, escargot.x, escargot.y)
            self.canvas.update()
            escargot.finished=False



