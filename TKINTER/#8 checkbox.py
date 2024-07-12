from tkinter import *

root = Tk()

root.title("Interface Graphique")
root.geometry("900x700+300+20")
root.config(bg="cyan")
root.resizable(FALSE,FALSE)

langue1 = BooleanVar()
langue2 = IntVar()
langue3 = IntVar()
langue4 = IntVar()

def soumettre():
    print(langue1.get())
    print(langue2.get())
    print(langue3.get())
    print(langue4.get())


lbl_langue = Label(root,text="Langue : ",font=("times new roman",17,"bold"),bg="cyan").place(x=100,y=150)

anglais= Checkbutton(root,text="ENGLISH", font=("times new roman",15),bg="cyan", variable=langue1, onvalue=True, offvalue=False).place(x=100,y=180)

francais= Checkbutton(root,text="FRENCH", font=("times new roman",15),bg="cyan", variable=langue2).place(x=100,y=210)

ewe= Checkbutton(root,text="EWE", font=("times new roman",15),bg="cyan", variable=langue3).place(x=100,y=240)

espagnol= Checkbutton(root,text="SPANISH", font=("times new roman",15),bg="cyan", variable=langue4).place(x=100,y=270)

btn = Button(root,text="Soumettre",font=("times new roman",17,"bold"),bg="green",fg="white",cursor="hand2", command=soumettre).place(x=350,y=600)



root.mainloop()