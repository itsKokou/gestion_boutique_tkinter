from tkinter import *

root = Tk()

root.title("Interface Graphique")
root.geometry("900x700+300+20")
root.config(bg="cyan")
root.resizable(FALSE,FALSE)

def soumettre():
    print(sex.get())

sex = StringVar()

lbl_sexe = Label(root,text="Sexe : ",font=("times new roman",17,"bold"),bg="cyan").place(x=100,y=150)

homme= Radiobutton(root,text="Homme",value="Man", font=("times new roman",15),bg="cyan", variable=sex).place(x=100,y=180)

femme= Radiobutton(root,text="Femme",value="Woman", font=("times new roman",15),bg="cyan", variable=sex).place(x=200,y=180)

btn = Button(root,text="Soumettre",font=("times new roman",17,"bold"),bg="green",fg="white",cursor="hand2", command=soumettre).place(x=350,y=600)

sex.set("Man") #Par defaut il chosiit un homme 


root.mainloop()