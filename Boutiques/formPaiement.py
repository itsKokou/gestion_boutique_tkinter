from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import customtkinter
import sqlite3





class Paiement :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("600x550+430+110")
        self.root.title("Paiement")
        self.root.resizable(FALSE,FALSE)

        Main_Frame = customtkinter.CTkFrame(self.root,width=400, height=500, fg_color="white")
        Main_Frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        lbl_title = customtkinter.CTkLabel(Main_Frame, text="Payer en ligne",font=('arial',20,"bold"))
        lbl_title.place(x=25, y=15)

        self.lbl_imageD= ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/droite.png"))
        self.lbl_droite = Label(Main_Frame, image=self.lbl_imageD, bg="white")
        self.lbl_droite.place(x=340, y=15)

        self.lbl_imageL= ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/logo.png"))
        self.lbl_logo = Label(Main_Frame, image=self.lbl_imageL, bg="white")
        self.lbl_logo.place(x=20, y=40)

        self.lbl_nom = customtkinter.CTkLabel(Main_Frame, text="Nom sur la carte", font=("times new roman",17))
        self.lbl_nom.place(x=25, y=110)

        self.txt_nom = customtkinter.CTkEntry(Main_Frame, width=330,height=40 ,placeholder_text='Nom Complet', border_width=1, font=("times new roman",17), fg_color="white")
        self.txt_nom.place(x=25, y=140)

        self.lbl_numero = customtkinter.CTkLabel(Main_Frame ,text="N° de carte", font=("times new roman",17))
        self.lbl_numero.place(x=25, y=205)

        self.txt_numero = customtkinter.CTkEntry(Main_Frame, width=330,height=40 ,placeholder_text='.... .... .... ....', border_width=1, font=("times new roman",17), fg_color="white")
        self.txt_numero.place(x=25, y=240)

        self.lbl_imageC= ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/carte.png"))
        self.lbl_carte = Label(Main_Frame, image=self.lbl_imageC, bg="white")
        self.lbl_carte.place(x=310, y=248)

        self.lbl_date = customtkinter.CTkLabel(Main_Frame, text="Date d'expiration", font=("times new roman",17))
        self.lbl_date.place(x=25, y=300)

        self.txt_date = customtkinter.CTkEntry(Main_Frame, width=150,height=40 ,placeholder_text='MM/AA', border_width=1, font=("times new roman",17), fg_color="white")
        self.txt_date.place(x=25, y=330)

        self.lbl_code = customtkinter.CTkLabel(Main_Frame, text="Cryptogramme visuel", font=("times new roman",17))
        self.lbl_code.place(x=204, y=300)

        self.txt_code = customtkinter.CTkEntry(Main_Frame, width=150,height=40 ,placeholder_text='CVV', border_width=1, font=("times new roman",17), fg_color="white")
        self.txt_code.place(x=204, y=330)

        img_payer = customtkinter.CTkImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/cadenas.png").resize((20,20),Image.LANCZOS))
        self.btn_payer = customtkinter.CTkButton(master=Main_Frame,image=img_payer,command=self.Payer ,text="Payer",font=("times new roman",17,"bold") ,width=326, height=40, compound="left",fg_color='#3388FF', text_color='white', hover_color='#3388FF', cursor="hand2")
        self.btn_payer.place(x=25, y=420)




    #------------------------------ Fonction

    def gererStock(self):
        from Boutiques.mode import Mode # Importer toutes les boutiques et tester d'où vient le paiement
        from Boutiques.bijouterie import Bijouterie
        from Boutiques.maison import Maison
        from Boutiques.sport import Sport
        from Boutiques.alimentation import Alimentation
        from Boutiques.restaurant import Restaurant
        # On charge les produits dont on veut modifier les stock dans data en fonction de la boutique
        data = []
        base =""

        if Mode.paiement == True :
            Mode.Facture()
            data = Mode.tabStock
            base = "mode"
            Mode.paiement = False #On retire le paiement en cours 
        elif Bijouterie.paiement == True :
            Bijouterie.Facture()
            data = Bijouterie.tabStock
            base = "bijouterie"
            Bijouterie.paiement = False
        elif Maison.paiement == True :
            Maison.Facture()
            data = Maison.tabStock
            base = "maison"
            Maison.paiement = False
        elif Sport.paiement == True :
            Sport.Facture()
            data = Sport.tabStock
            base = "sport"
            Sport.paiement = False
        elif Restaurant.paiement == True :
            Restaurant.Facture()
            data = Restaurant.tabStock
            base = "restaurant"
            Restaurant.paiement = False
        elif Alimentation.paiement == True :
            Alimentation.Facture()
            data = Alimentation.tabStock
            base = "alimentation"
            Alimentation.paiement = False  
        

        conn = sqlite3.connect(f"C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/{base}.db")
        c = conn.cursor()
       
        for i in data :
            c.execute(f"""
                UPDATE produit
                SET stock = {i.stock}
                WHERE id == {i.id}
            """)
            conn.commit()
        
        conn.close()

    def checkName(self):
        if self.txt_nom.get().strip() == "" :
            messagebox.showerror("Error nom", "Veuillez  saisir le nom sur la carte")
            result = False
        elif len(self.txt_nom.get().strip()) <4:
            messagebox.showerror("Error nom", "Veuillez  saisir un nom Valide") 
            result = False
        else :
            tab = self.txt_nom.get().strip().split(" ")
            result = True
            for i in tab :
                if i.isalpha()== False:
                    messagebox.showerror("Error nom", "Veuillez  saisir un nom valide")
                    result = False
            return result
    
    def checkDate(self):
        if self.txt_date.get().strip() =="":
            messagebox.showerror("Error Date", "Veuillez  la date d'expiration de la carte")
            result = False
        elif len(self.txt_date.get().strip()) !=5:
            messagebox.showerror("Error Date", "Veuillez  une date valide")
            result = False
        else :
            tab = self.txt_date.get().strip().split("/")
            if (tab[0].isdigit()==True and tab[1].isdigit()==True):
                result = True
                if int(tab[0])==0 or int(tab[0])>12 :
                    messagebox.showerror("Error Date", "Le mois n'est pas valide")
                    result = False
                elif int(tab[1])<23 or int(tab[1])>26 :
                    messagebox.showerror("Error Date", "L'année n'est pas valide")
                    result = False
                elif int(tab[1])==23 and int(tab[0])<4 :
                    messagebox.showerror("Error Carte", "Votre carte a expiré. Essayez une autre carte !")
                    result = False
            else : 
                messagebox.showerror("Error Date", "La date doit être sous format MM/YY")
                result = False
        return result 

    def Payer(self): 
        if self.checkName() == True :
            if self.txt_numero.get().strip() =="":
                messagebox.showerror("Error Numéro", "Veuillez  saisir le numéro de la carte")
            elif len(self.txt_numero.get().strip()) != 16:
                messagebox.showerror("Error Numéro", "Un numéro de carte contient 16 chiffres !")
            elif self.txt_numero.get().strip().isdigit() == False:
                messagebox.showerror("Error Numéro", "Un numéro de carte est composé uniquement de chiffres")
            elif self.checkDate()==True:
                if self.txt_code.get().strip() =="":
                    messagebox.showerror("Error CVV", "Veuillez  saisir le code derière votre carte")
                elif len(self.txt_code.get().strip()) != 3:
                    messagebox.showerror("Error CVV", "Un CVV ne contient que 3 chiffres")
                elif self.txt_code.get().strip().isdigit()==False:
                    messagebox.showerror("Error CVV", "Un CVV est Composé uniquement de chiffe!")
                else: 
                    self.gererStock()
                    self.root.destroy()
                    self.root.quit()
                    from Boutiques.mall import Mall
                    Mall.testProduit = False
                    #Aller sur Page de remerciment
                    from Boutiques.formMerci import Merci
                    root = Tk()
                    Merci(root)
                    root.mainloop()







# root= Tk()
# ob = Paiement(root)
# root.mainloop()