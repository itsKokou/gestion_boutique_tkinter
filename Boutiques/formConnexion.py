from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import ImageTk,Image
import customtkinter
import sqlite3
from Boutiques.formCompte import Compte
# from webbrowser import *
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


class Form :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("600x550+450+150")
        self.root.title("Login")
        self.root.resizable(FALSE,FALSE)

        # Variable 
        self.user = User(0,"","","","",2,1)

        self.imageMall = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/malls.jpg"))
        self.lbl_image = Label(self.root, image=self.imageMall)
        self.lbl_image.place(x=0, y=0)

        elFrame = customtkinter.CTkFrame(self.root,width=320, height=360, fg_color="#E1E1E2")
        elFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        lbl_title = customtkinter.CTkLabel(elFrame, text="Log in",font=('Century Gothic',20))
        lbl_title.place(x=120, y=45)

        self.username= customtkinter.CTkEntry(elFrame, width=220, placeholder_text='Username')
        self.username.place(x=50, y=110)

        self.password= entry2=customtkinter.CTkEntry(master=elFrame, width=220, placeholder_text='Password', show="*")
        self.password.place(x=50, y=165)

        btn_msg=customtkinter.CTkButton(master=elFrame,text="Nouveau Client ? Créer un compte",command=self.creerCompte,font=('Century Gothic',12), fg_color="#E1E1E2",text_color='black', hover_color="#E1E1E2", cursor="hand2" )
        btn_msg.place(x=55,y=195)

        btn_login = customtkinter.CTkButton(master=elFrame,width=220,command=self.connexion ,text="Login",font=("times new roman",15,"bold") , corner_radius=6, cursor="hand2", hover_color="green")
        btn_login.place(x=50, y=240)

        facebook=customtkinter.CTkImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/facebook.ico").resize((20,20),Image.LANCZOS))

        google=customtkinter.CTkImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/google.ico").resize((20,20),Image.LANCZOS))

        btn_google= customtkinter.CTkButton(elFrame,image=google,command= self.openGoogle ,text="Google",width=100, height=20, compound="left",fg_color='white',text_color='black', hover_color='#AFAFAF', cursor="hand2")
        btn_google.place(x=50, y=290)

        btn_facebook= customtkinter.CTkButton(master=elFrame,image=facebook,command=self.openFacebook ,text="Facebook", width=100, height=20, compound="left",fg_color='white', text_color='black', hover_color='#AFAFAF', cursor="hand2")
        btn_facebook.place(x=170, y=290)

    


    #--------------------Les Fonctions 
    def rechercheUser(self, login, password):
        for i in tabUser :
            if login == i.login and password == i.password :
                self.user = i
                return True
        return False

    def connexion(self):
        if self.username.get() =="":
            messagebox.showerror("Error Username", "Username is required")
        elif self.password.get() =="":
            messagebox.showerror("Error Password", "Password is required")
        else :
            result = self.rechercheUser(self.username.get(),self.password.get())
            if result == False :
                messagebox.showwarning("Attention", "Login Ou Mot de passe Incorrect !")
            else:
                self.root.destroy()
                self.root.quit()
                if self.user.etat == 1 :
                    # Tester si aller dans Mall ou paiement 
                    from Boutiques.mall import Mall
                    from Boutiques.formPaiement import Paiement
                    Mall.user = self.user
                    Mall.testConn = True
                    root = Tk()
    
                    if Mall.testProduit == False and self.user.role == 1 : #Si pas de produit choisi et c'est un admin il va dans son interface 
                        from Boutiques.interAdmin import Admin
                        Admin(root)
                    elif Mall.testProduit == False :
                        Mall(root)
                    else :
                        Paiement(root)
                    root.mainloop()
                else : 
                    messagebox.showinfo("Compte Suspendu", "Votre compte a été suspendu. Veuillez-vous rapprocher d'un administrateur !!!")




            
    def creerCompte(self):
        self.root.destroy()
        self.root.quit()
        root = Tk()
        ob = Compte(root)
        root.mainloop()


    def openGoogle(self):
        webbrowser.open("https://accounts.google.com/v3/signin/identifier?dsh=S1695339280%3A1680471882545681&ifkv=AQMjQ7TX_9DAd5vKpwMh5LHQTuoHE2OizUrp3LNdyy6vmV5Zvcl7VYHUu5w6Lrp5PN17OMo-AncKeA&flowName=GlifWebSignIn&flowEntry=ServiceLogin")


    def openFacebook(self):
        webbrowser.open("https://www.facebook.com/login")
            






# root =Tk()
# ob = Form(root)

# root.mainloop()