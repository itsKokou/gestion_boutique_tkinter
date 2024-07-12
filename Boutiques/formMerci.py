from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import customtkinter
import tempfile   # pour imprimer facture
import os # pour l'impression



class Merci :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("800x500+370+110")
        self.root.title("Merci")
        self.root.resizable(FALSE,FALSE)

        self.image = customtkinter.CTkImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/malls.jpg"),size=(800,500))
        self.lbl_image = customtkinter.CTkLabel(self.root, image=self.image)
        self.lbl_image.place(x=0, y=0)
        

        Main_Frame = customtkinter.CTkFrame(self.root,width=600, height=400, fg_color="#FDFBF7")
        Main_Frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.img_merci = customtkinter.CTkImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/merci.png"), size=(600,400))
        lbl_title =customtkinter.CTkLabel(Main_Frame,image=self.img_merci, text="")
        lbl_title.place(x=0, y=0)

        btn_mall = customtkinter.CTkButton(Main_Frame, text="MALL",command=self.Accueil,font=("Consolas",14,"bold") ,width=8,fg_color='#FDFBF7',text_color="black",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        btn_mall.place(x=20,y=15)

        self.icone = customtkinter.CTkImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/imprimer.png"), size=(25,25))
        btn_imprimer= customtkinter.CTkButton(master=Main_Frame,image=self.icone,command=self.imprimer ,text="", width=30, height=10, compound="left",fg_color='#FDFBF7', text_color='black', hover_color='gray', cursor="hand2")
        btn_imprimer.place(x=540, y=15)


    def imprimer(self):
        from Boutiques.mall import Mall
        with open(f"C:/Users/winny/Desktop/Projet Python POO/Factures/{Mall.nomFact}","r",encoding='UTF-8') as f :
            data = f.read()

        fichier = tempfile.mktemp(".txt")
        open(fichier, "w").write(data)
        os.startfile(fichier,"print") 

    def Accueil(self):
        self.root.destroy()
        self.root.quit()
        from Boutiques.mall import Mall
        app = Tk()
        Mall(app)
        app.mainloop()

# root = Tk()
# Merci(root)
# root.mainloop()