from tkinter import *
from tkinter import messagebox


fenetre=Tk()  # Ferme la classe 

fenetre.title("Formulaire avec une base de donnée") 
fenetre.geometry("1520x780+0+0")

def soumettre():
    messagebox.showinfo("Statut de l'inscription", "Formulaire Envoyé !")

lbl = Label(fenetre, text="Nom :")
lbl.pack()
ent = Entry(fenetre)
ent.pack()
btn = Button(fenetre,text="Submit", command=soumettre)
btn.pack()
rb1 = Radiobutton(fenetre, text = "Feminin", value = '1')
rb1.pack()
rb2 = Radiobutton(fenetre, text = "Masculin", value = '2')
rb2.pack()
c1 = Checkbutton (fenetre, text = "art", variable = '1')
c1.pack()
c2 = Checkbutton (fenetre, text = "science", variable = '2')
c2.pack()
c3 = Checkbutton (fenetre, text = "litterature", variable = '3')
c3.pack()
lb = Listbox(fenetre)
lb.insert(0, 'Asie')
lb.insert(1, 'Afrique')
lb.insert(2, 'Amérique')
lb.insert(3, 'Europe')
lb.pack()


fenetre.mainloop() #Fermer globalement la fonction 













