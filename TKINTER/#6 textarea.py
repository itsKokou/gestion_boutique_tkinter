from tkinter import *

root = Tk()

root.title("Interface Graphique")
root.geometry("900x700+300+20")
root.config(bg="cyan")
root.resizable(FALSE,FALSE)

#--Pour afficher ou recuperer les informations, il faut faire le positionneent après

def soumettre():
    result.config(text=str(nom.get()+" "+ prenom.get()))

lbl= Label(root,text="Formulaire", font=("times new roman",30,"bold"),bg="yellow",foreground="red",pady=10,bd=10,relief=GROOVE).pack(fill=X,padx=200,pady=20)

lbl1=Label(root,text="Nom : ",font=("times new roman",17),bg="cyan").place(x=100,y=150)
nom= Entry(root,font=("times new roman",20),bg="gray",fg="black")
nom.place(x=200,y=150) 

lbl2=Label(root,text="Prénom : ",font=("times new roman",17),bg="cyan").place(x=100,y=200)
prenom= Entry(root,font=("times new roman",20),bg="gray",fg="black")
prenom.place(x=200,y=200)

btn = Button(root,text="Soumettre",font=("times new roman",17,"bold"),bg="green",fg="white",cursor="hand2",command=soumettre).place(x=350,y=600)

result= Label(root,font=("times new roman",20),bg="cyan",fg="red")
result.place(x=300,y=300)


lb = Label(root,text="Adresse : ",font=("times new roman",17),bg="cyan").place(x=100,y=300)
adresse = Text(root).place(x=200,y=300,width=400,height=200)



root.mainloop()