from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import customtkinter
import sqlite3
import webbrowser



class User:
    def __init__(self, id, nom, prenom,login,password,role,etat):
        self.id = id
        self.nom =nom
        self.prenom = prenom
        self.login = login
        self.password = password
        self.role = role
        self.etat = etat

#Tableau d'utilisateur 
tabUser =[]

conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/user.db")
c = conn.cursor()

c.execute("Select * From user")
data = c.fetchall()

conn.close()

# Specifier les données
def specifierUser(donnee:list):
    for ligne in donnee:
        id = int(ligne[0])
        nom = str(ligne[1])
        prenom = str(ligne[2])
        role = int(ligne[3])
        login = str(ligne[4])
        password = str(ligne[5])
        etat = int(ligne[6])
        us = User(id,nom,prenom,login,password,role,etat)  # Création de l'objet
        tabUser.append(us) # Ajout de l'objet au tableau

specifierUser(data)



class Compte :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("600x550+450+110")
        self.root.title("Création de Compte")
        self.root.resizable(FALSE,FALSE)

        # Variable 
        self.user = User(0,"","","","",2,1)

        self.imageMall = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/malls.jpg"))
        self.lbl_image = Label(self.root, image=self.imageMall)
        self.lbl_image.place(x=0, y=0)

        elFrame = customtkinter.CTkFrame(self.root,width=320, height=460, fg_color="#E1E1E2")
        elFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        lbl_title = customtkinter.CTkLabel(elFrame, text="Créer Compte",font=('Century Gothic',20))
        lbl_title.place(x=80, y=45)

        self.nom= customtkinter.CTkEntry(elFrame, width=220, placeholder_text='Entrez votre nom')
        self.nom.place(x=50, y=90)

        self.prenom= entry2=customtkinter.CTkEntry(master=elFrame, width=220, placeholder_text='Entrez votre Prénom')
        self.prenom.place(x=50, y=140)

        self.login= customtkinter.CTkEntry(elFrame, width=220, placeholder_text='Entrez votre Login')
        self.login.place(x=50, y=190)

        self.password= entry2=customtkinter.CTkEntry(master=elFrame, width=220, placeholder_text='Entrez votre Mot de Passe', show="*")
        self.password.place(x=50, y=240)

        self.password2= entry2=customtkinter.CTkEntry(master=elFrame, width=220, placeholder_text='Confirmez votre Mot de Passe', show="*")
        self.password2.place(x=50, y=290)

        btn_login = customtkinter.CTkButton(master=elFrame,width=220,command=self.connexion ,text="Soumettre",font=("times new roman",15,"bold") ,corner_radius=6, cursor="hand2", hover_color="green")
        btn_login.place(x=50, y=345)

        facebook=customtkinter.CTkImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/facebook.ico").resize((20,20),Image.LANCZOS))

        google=customtkinter.CTkImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/google.ico").resize((20,20),Image.LANCZOS))

        btn_google= customtkinter.CTkButton(elFrame,image=google,command=self.openGoogle ,text="Google",width=100, height=20, compound="left",fg_color='white',text_color='black', hover_color='#AFAFAF', cursor="hand2")
        btn_google.place(x=50, y=390)

        btn_facebook= customtkinter.CTkButton(master=elFrame,image=facebook,command=self.openFacebook ,text="Facebook", width=100, height=20, compound="left",fg_color='white', text_color='black', hover_color='#AFAFAF', cursor="hand2")
        btn_facebook.place(x=170, y=390)

    


    #--------------------Les Fonctions 
    def openGoogle(self):
        webbrowser.open("https://accounts.google.com/v3/signin/identifier?dsh=S1695339280%3A1680471882545681&ifkv=AQMjQ7TX_9DAd5vKpwMh5LHQTuoHE2OizUrp3LNdyy6vmV5Zvcl7VYHUu5w6Lrp5PN17OMo-AncKeA&flowName=GlifWebSignIn&flowEntry=ServiceLogin")


    def openFacebook(self):
        webbrowser.open("https://www.facebook.com/login")


    def rechercheLogin(self, login):
        for i in tabUser :
            if login == i.login  :
                return True
        return False

    def connexion(self):
        if self.nom.get().strip() =="":
            messagebox.showerror("Error nom", "Veuillez  saisir votre nom")
        elif len(self.nom.get().strip()) <2:
            messagebox.showerror("Error nom", "Veuillez  saisir un nom Valide")
        elif self.prenom.get().strip() =="":
            messagebox.showerror("Error Prenom", "Veuillez  saisir votre prénom")
        elif len(self.prenom.get().strip()) <2:
            messagebox.showerror("Error Prenom", "Veuillez  saisir un prénom valide")
        elif self.login.get().strip() =="":
            messagebox.showerror("Error Login", "Veuillez  saisir votre Login")
        elif len(self.login.get().strip()) <4:
            messagebox.showerror("Error Login", "Un Login contient au moins 4 caracteres")
        elif self.password.get().strip() =="":
            messagebox.showerror("Error Password", "Veuillez  saisir votre Mot de passe")
        elif len(self.password.get().strip()) <4:
            messagebox.showerror("Error Password", "Un Password contient au moins 4 caracteres")
        elif self.password2.get().strip() =="":
            messagebox.showerror("Error Password", "Veuillez Confirmer votre Mot de passe")
        elif self.password2.get().strip() != self.password.get().strip() :
            messagebox.showerror("Error Confirmation", "Les mots de passe ne correspondent pas !")
        else :
            result = self.rechercheLogin(self.login.get())
            if result == True :
                messagebox.showwarning("Attention", f"le nom d'utilisateur {self.login.get()} n'est pas disponible !")
            else:
                conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/user.db")
                c = conn.cursor()
                self.user = User(len(tabUser)+1,self.nom.get(),self.prenom.get(),self.login.get(),self.password.get(),2,1)
                param = {"i": self.nom.get(), "l": self.prenom.get(), "p": self.login.get(), "q": self.password.get(),"r":2,"t":1}
                c.execute("""
                    INSERT INTO user(nom,prenom,login,password,role,etat)
                    VALUES(:i,:l,:p,:q,:r,:t)
                """, param)
                conn.commit()
                conn.close()
                self.root.destroy()
                self.root.quit()
                # Tester si aller dans Mall ou paiement
                from Boutiques.mall import Mall
                from Boutiques.formPaiement import Paiement
                Mall.user = self.user
                Mall.testConn = True
                root = Tk()
                if Mall.testProduit == False :
                    Mall(root)
                else :
                    Paiement(root)
                root.mainloop()





# root =Tk()
# ob = Compte(root)
# root.mainloop()