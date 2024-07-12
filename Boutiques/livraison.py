from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter


class Livraison:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x550+450+110")
        self.root.title("Information de Livraison")
        self.root.resizable(FALSE, FALSE)

        # Variable
        Main = Frame(self.root, bg="white")
        Main.pack(fill=BOTH, expand=1)

        # img = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/malls.jpg"))
        # lbl_img = Label(self.root,image=img)
        # lbl_img.place(x=0,y=0)

        elFrame = customtkinter.CTkFrame(self.root,width=320, height=420, fg_color="#E1E1E2")
        elFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        lbl_title = customtkinter.CTkLabel(elFrame, text="Informations de livraison",font=('Century Gothic',20))
        lbl_title.place(x=43, y=30)

        lbl_info = customtkinter.CTkLabel(elFrame, text="( Les livraisons ne sont disponibles que dans Dakar )",font=('times new roman',14),text_color='red' )
        lbl_info.place(x=10, y=55)

        self.quartier= entry2=customtkinter.CTkEntry(master=elFrame, width=220, placeholder_text='Entrez la localité')
        self.quartier.place(x=50, y=90)

        self.rue= customtkinter.CTkEntry(elFrame, width=220, placeholder_text='Entrez la rue')
        self.rue.place(x=50, y=140)

        self.numero= entry2=customtkinter.CTkEntry(master=elFrame, width=220, placeholder_text='Entrez le numero de téléphone')
        self.numero.place(x=50, y=190)

        lbl_info2 = customtkinter.CTkLabel(elFrame, text="Infos : Toute livraison est à 2500 Francs.",font=('times new roman',17) )
        lbl_info2.place(x=20, y=240)

        self.btn_annuler = customtkinter.CTkButton(elFrame,command=self.annuler ,text="Annuler",font=("Consolas",16,"bold") ,width=15, height=35,bg_color="white",fg_color='red',text_color="black",hover_color='white', cursor="hand2", border_color="black", border_width=1 )
        self.btn_annuler.place(x=60, y=345)

        self.btn_valider = customtkinter.CTkButton(elFrame,command=self.valider, text="Valider",font=("Consolas",16,"bold") ,width=15, height=35,bg_color="white",fg_color='green',text_color="black",hover_color='white', cursor="hand2", border_color="black", border_width=1 )
        self.btn_valider.place(x=190, y=345)

    def annuler(self):
        from Boutiques.mode import Mode # Importer toutes les boutiques et tester d'où vient le paiement
        from Boutiques.bijouterie import Bijouterie
        from Boutiques.maison import Maison
        from Boutiques.sport import Sport
        from Boutiques.alimentation import Alimentation
        from Boutiques.restaurant import Restaurant

        if Mode.livraison == True:
            Mode.livraison = False
        elif Bijouterie.livraison == True:
            Bijouterie.livraison = False
        elif Sport.livraison == True:
            Sport.livraison = False
        elif Maison.livraison == True:
            Maison.livraison = False
        elif Alimentation.livraison == True:
            Alimentation.livraison = False
        elif Restaurant.livraison == True:
            Restaurant.livraison = False

        self.root.destroy()
        self.root.quit()

    def checkName(self):
        if self.quartier.get().strip() == "" :
            messagebox.showerror("Error Localité", "Veuillez  saisir une localité")
            result = False
        elif len(self.quartier.get().strip()) <3:
            messagebox.showerror("Error Localité", "Veuillez  saisir une localité valide")
            result = False
        else :
            tab = self.quartier.get().strip().split(" ")
            result = True
            for i in tab :
                if i.isalpha()== False:
                    messagebox.showerror("Error Localité", "Veuillez  saisir une localité valide")
                    result = False
            return result

    def valider(self):
        if self.checkName() == True :
            if self.rue.get().strip() =="":
                messagebox.showerror("Error Rue", "Veuillez  saisir la rue")
            elif len(self.rue.get().strip()) <3:
                messagebox.showerror("Error Rue", "Veuillez saisir une rue valide")
            elif self.numero.get().strip() =="":
                messagebox.showerror("Error Numéro", "Veuillez saisir le numéro de téléphone du destinataire")
            elif len(self.numero.get().strip()) != 9:
                messagebox.showerror("Error Numéro", "Veuillez saisir un numéro valide")
            elif self.numero.get().strip().isdigit() == False:
                messagebox.showerror("Error Numéro", "Un numéro est composé uniquement de chiffres")
            else:
                from Boutiques.mode import Mode # Importer toutes les boutiques et tester d'où vient le paiement
                from Boutiques.bijouterie import Bijouterie
                from Boutiques.maison import Maison
                from Boutiques.sport import Sport
                from Boutiques.alimentation import Alimentation
                from Boutiques.restaurant import Restaurant

                if Mode.livraison ==  True:
                    Mode.adresse = self.quartier.get()+", "+self.rue.get()
                    Mode.numero = self.numero.get()
                elif Bijouterie.livraison == True:
                    Bijouterie.adresse = self.quartier.get()+", "+self.rue.get()
                    Bijouterie.numero = self.numero.get()
                elif Sport.livraison == True:
                    Sport.adresse = self.quartier.get()+", "+self.rue.get()
                    Sport.numero = self.numero.get()
                elif Maison.livraison == True:
                    Maison.adresse = self.quartier.get()+", "+self.rue.get()
                    Maison.numero = self.numero.get()
                elif Alimentation.livraison == True:
                    Alimentation.adresse = self.quartier.get()+", "+self.rue.get()
                    Alimentation.numero = self.numero.get()
                elif Restaurant.livraison == True:
                    Restaurant.adresse = self.quartier.get()+", "+self.rue.get()
                    Restaurant.numero = self.numero.get()

                self.root.destroy()
                self.root.quit()


# root = Tk()
# Livraison(root)
# root.mainloop()
