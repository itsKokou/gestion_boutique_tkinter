# LES POSITIONS : GRID, PACK & PLACE

from tkinter import *
root=Tk()
root.title("Interface Graphique")  #Title interface 
root.geometry("800x400+350+200") # taille interface + position : largeur x hauteur + axe de X +axe de Y
#Empêcher d'agrandir ou de reduire la taille de l'interface
root.resizable(False,False)
#Backgroud color 
root.config(bg="Cyan")
#---------------------------------------------------

#-------------------GRID

# lbl = Label(root, text="GRID POSITION").grid(row=0,column=0) # quand on ecrit un texte, il faut spécifier son emplacement pour pouvoir le voir
# lbl = Label(root, text="GRID POSITION1").grid(row=1,column=0)
# lbl = Label(root, text="GRID POSITION2").grid(row=1,column=1)
# lbl = Label(root, text="GRID POSITION3").grid(row=3,column=3)

#-------------------PACK
#lbl = Label(root, text="GRID POSITION").pack() # par defaut pack le met au milieu
# lbl = Label(root, text="GRID POSITION1").pack(side=LEFT)  # aligne au milieu de la vertical à gauche
# lbl = Label(root, text="GRID POSITION2").pack(fill=X)  # Aligne sur toute la ligne au milieu
#lbl = Label(root, text="GRID POSITION2").pack(expand=1, fill="both") # prend toute la largeur et met le texte au milieu

#-------------------PLACE
lbl = Label(root, text="GRID POSITION").place(x=300,y=100)




root.mainloop()  # fermer interface