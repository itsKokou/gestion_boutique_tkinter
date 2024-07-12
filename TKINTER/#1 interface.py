from tkinter import *

root=Tk()   # ouvrir interface

root.title("Interface Graphique")  #Title interface 
root.geometry("800x400+350+200") # taille interface + position : largeur x hauteur + axe de X +axe de Y
#Empêcher d'agrandir ou de reduire la taille de l'interface
root.resizable(False,False)
#Backgroud color 
root.config(bg="Cyan")

root.mainloop()  # fermer interface