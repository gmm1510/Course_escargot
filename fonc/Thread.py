from tkinter import*
from time import sleep
from threading import Thread

class __appThread__(Thread):
    def __init__(self, args):
        Thread.__init__(self)
        self.args = args

    def run(self) -> None:
        #self.thread(args)
        __app__(self.args)

def __app__(canvas):
    x1,y1 = 130,75
    x2,y2 = 130,225
    x3,y3 = 130,375
    x4,y4 = 130,525
    i=0
    while True:
        while i != 15:
            while i < 12:
                number_image = "gif -index " + str(i)
                photo1 = PhotoImage(file='ezgifj.gif', format=number_image)
                esca1 = canvas.create_image(x1, y1, image=photo1)
                photo2 = PhotoImage(file='ezgifm.gif', format=number_image)
                esca2 = canvas.create_image(x2, y2, image=photo2)
                photo3 = PhotoImage(file='ezgifr.gif', format=number_image)
                esca3 = canvas.create_image(x3, y3, image=photo3)
                photo4 = PhotoImage(file='ezgifv.gif', format=number_image)
                esca4 = canvas.create_image(x4, y4, image=photo4)
                sleep(0.05)
                canvas.update()
                i = i + 1
            i = 0




def start_T(canvas):
    __appThread__(args=canvas).start()