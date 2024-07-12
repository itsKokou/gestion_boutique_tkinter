from tkinter import *
root=Tk()
root.title("Interface Graphique")  #Title interface 
root.geometry("800x400+350+200") # taille interface + position : largeur x hauteur + axe de X +axe de Y
#Empêcher d'agrandir ou de reduire la taille de l'interface
root.resizable(False,False)
#Backgroud color 
root.config(bg="Cyan")
#---------------------------------------------------
# Padding dans position ==> Margin 
# Padding dans label ==> Padding 
# lbl = Label(root, text="GRID POSITION1", font=("times new roman",40,"bold"), bg="yellow", fg="red").pack(fill=X)
# lbl = Label(root, text="GRID POSITION2", font=("times new roman",40,"bold"), bg="yellow", fg="red").pack(fill=X, padx=20, pady=20)
# lbl = Label(root, text="GRID POSITION3", font=("times new roman",40,"bold"), bg="yellow", fg="red", pady=40).pack(fill=X,padx=30, pady=30)

# Décorationn
# bd : agrandit l'interieur du label 
# relief : le type de cadrage SUNKEN, GROOVE, RAISED
lbl = Label(root, text="GRID POSITION4", font=("times new roman",40,"bold"), bg="yellow", fg="red", pady=40, bd=10,relief=GROOVE).pack(fill=X,padx=30, pady=30)

root.mainloop()  # fermer interface