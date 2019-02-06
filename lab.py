#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:40:22 2015

@author: gilles
"""

from tkinter import *

class Personnage:
    """Définition de la classe personnage"""
    def __init__(self, canvas, matrice, image="perso.gif"):
        self.coo = [0, 0]
        self.canvas = canvas
        self.matrice = matrice
        self.image = PhotoImage(file=image)
        self.perso = canvas.create_image(self.coo[0], self.coo[1], anchor=NW, image=self.image)
    
    def eventKeyDown(self, event):
        move = {
            "Down":  [0,  1],
            "Up":    [0, -1],
            "Left":  [-1, 0],
            "Right": [1,  0]
        }
        if (event.keysym not in move):
            return
        self.move(move[event.keysym])
    
    def move(self, coo):
        if (self.coo[0] + coo[0] * 25 >= 0):
            if (self.coo[0] + coo[0] * 25 < 25 * len(self.matrice[0])):
                self.coo[0] += coo[0] * 25
        if (self.coo[1] + coo[1] * 25 >= 0):
            if (self.coo[1] + coo[1] * 25 < 25 * len(self.matrice)):
                self.coo[1] += coo[1] * 25
        if (self.matrice[self.coo[1] // 25][self.coo[0] // 25] == 1):
            self.coo[0] -= coo[0] * 25
            self.coo[1] -= coo[1] * 25
        self.canvas.coords(self.perso, self.coo[0], self.coo[1])

#############
# FONCTIONS #
#############

def finish():
    fond.create_text(100, 10, fill="darkblue", font="Times 20 italic bold", text="Félicitation !")

def gestionEvent(event):
    personnage.eventKeyDown(event)
    if (personnage.coo[0] // 25 == len(matrice[0]) - 1):
        if (personnage.coo[1] // 25 == len(matrice) - 1):
            finish()

def poseDecor(tab):
    for v in range(len(tab)):
        for i in range(len(tab[v])):
            if (tab[v][i] == 1):
                img = fond.create_image(i * 25, v * 25, anchor=NW, image=mur)
            else:
                img = fond.create_image(i * 25, v * 25, anchor=NW, image=sol)
    img = fond.create_image((len(tab[0]) - 1) * 25, (len(tab) - 1) * 25, anchor=NW, image=end)


#######################
# PROGRAMME PRINCIPAL #
#######################

racine = Tk()
racine.geometry("1775x950") #détermination de la taille de la fenêtre principale

sol = PhotoImage(file="sol.gif") # creation d'un objet de la classe PhotoImage
mur = PhotoImage(file="mur.gif") # creation d'un objet de la classe PhotoImage
end = PhotoImage(file="end.png") # creation d'un objet de la classe PhotoImage

fond = Canvas(racine, bg='blue', width=1775, height=950)
solFond = fond.create_image(0, 0, image=sol)
fond.pack(side=LEFT)

with open("lab.csv", "r") as file:
    content = file.read()

matrice = eval(content)
poseDecor(matrice)

personnage = Personnage(fond, matrice)

racine.bind("<Key>", gestionEvent)

racine.mainloop()
