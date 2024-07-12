from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Interface Graphique")
root.geometry("900x700+300+20")
root.config(bg="cyan")
root.resizable(FALSE,FALSE)

def soumettre():
    if pays.get() == "Votre Pays" :
        print("Veuillez choisir un pays")
    else :
        print(pays.get())
        root.quit()
    

lbl_pays = Label(root,text="Pays : ",font=("times new roman",17,"bold"),bg="cyan").place(x=100,y=150)

# state = "readonly" desactive la modification
pays = ttk.Combobox(root,values=("Togo","Sénégal","Tchad", "Congo", "Gabon", "Rwanda"), font=("times new roman",20), state="readonly", justify="center") 
pays.place(x=170,y=150)

pays.set("Votre Pays")  # Valeur afficher par defaut

btn = Button(root,text="Soumettre",font=("times new roman",17,"bold"),bg="green",fg="white",cursor="hand2",command=soumettre).place(x=350,y=600)

root.mainloop()