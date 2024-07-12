from tkinter import *

root = Tk()

root.title("Interface Graphique")
root.geometry("800x500+300+150")
root.config(bg="cyan")
root.resizable(FALSE,FALSE)

lbl= Label(root,text="Formulaire", font=("times new roman",30,"bold"),bg="yellow",foreground="red",pady=10,bd=10,relief=GROOVE).pack(fill=X,padx=200,pady=20)
nom= Entry(root,font=("times new roman",20),bg="gray",fg="black").place(x=200,y=150)
prenom= Entry(root,font=("times new roman",20),bg="gray",fg="black").place(x=200,y=200)


root.mainloop()