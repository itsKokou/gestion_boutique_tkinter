import sqlite3
from tkinter import *
import tkinter
from tkinter import messagebox,ttk
from time import strftime
from PIL import ImageTk, Image
import customtkinter
import tkinter.font as tkFont




#==========================================================================================================

class Categorie :
    def __init__(self,id,libelle) :
        self.id = id
        self.libelle = libelle
    
class SousCategorie:
    def __init__(self, id, libelle, idCategorie) :
        self.id = id
        self.libelle = libelle
        self.idCategorie = idCategorie

class Produit:
    def __init__(self,id, nom, prix, stock, idSousCategorie,image) -> None:
        self.id = id
        self.nom = nom
        self.prix = prix
        self.stock = stock
        self.idSousCategorie = idSousCategorie
        self.image = image

class Vente :
    def __init__(self,id,idClient,numFact,idBoutique):
        self.id = id
        self.idClient = idClient
        self.numFacture = numFact
        self.idBoutique = idBoutique

#### Classe pour aider dans gestion de stock, faire migrer id et stock de produit vers paiement
class Stock:
    def __init__(self, id, stock):
        self.id = id
        self.stock = stock

## Classe pour aider dans la facture 

class Facture:
    def __init__(self, produit, qte, montant, tva) -> None:
        self.produit = produit
        self.qte = qte
        self.montant = montant
        self.tva = tva


### Tableau contenant les données Contient objet 
tabCategorie = [] 
tabSousCategorie = []
tabProduit = []
tabVentes = []
### et liste Objet contient les noms des objets
# Nom des objets
listCategorie = []
listSousCategorie = []
listProduit = []
listShop = ["Mode","Bijouterie","Maison","Sport","Restaurant","Alimentation"]

## Récupération des données depuis la base de données
conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/mode.db")
c = conn.cursor()

c.execute("Select * From produit")
dataProduit = c.fetchall()  # Les produits sont stockées ici

c.execute("Select * From categorie")
dataCategorie = c.fetchall()

c.execute("Select * From souscategorie")
dataSousCategorie = c.fetchall()

conn.close()

#### Spécification de chaque donnée

def specifierProduit(donnee:list):
    for ligne in donnee:
        id = int(ligne[0])
        nom = str(ligne[1])
        prix = int(ligne[2])
        stock = int(ligne[3])
        idSC = int(ligne[4])
        image = str(ligne[5])
        obj = Produit(id,nom,prix,stock,idSC,image) # Création de l'objet
        tabProduit.append(obj) # Ajout de l'objet au tableau

def specifierCategorie(donnee:list):
    for ligne in donnee:
        id = int(ligne[0])
        libelle = str(ligne[1])
        tabCategorie.append(Categorie(id,libelle))
        listCategorie.append(libelle)

def specifierSousCategorie(donnee:list):
    for ligne in donnee:
        id = int(ligne[0])
        libelle = str(ligne[1])
        idC = int(ligne[2])
        tabSousCategorie.append(SousCategorie(id,libelle,idC))


## Récupération des ventes pour la recherche de facture
conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/ventes.db")
c = conn.cursor()
c.execute("Select * From ventes")
dataVentes = c.fetchall()  # Les ventes sont stockées ici
conn.close()

#### Spécification les données de la ventes
def specifierVentes(donnee:list):
    for ligne in donnee:
        id = int(ligne[0])
        idClient = int(ligne[1])
        numFact = str(ligne[2])
        idBoutique = int(ligne[3])
        tabVentes.append(Vente(id,idClient,numFact,idBoutique))

#####
specifierProduit(dataProduit)
specifierCategorie(dataCategorie)
specifierSousCategorie(dataSousCategorie)



#---------------------------User ------------------------------------------------------------
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
tabUserChoix = []

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








#---------------------------------------------------------------------------------------------------------------


class Admin :
    def __init__(self,root) :
        self.root = root
        self.root.title("Interface Admin")
        self.root.geometry("1520x780+0+0") #Taille de l'interface 
        self.root.resizable(FALSE,FALSE)
        self.root.config(bg="white")

        

        from Boutiques.mall import Mall
        self.title = Label(self.root, text=f"Bienvenue {Mall.user.nom} {Mall.user.prenom}", font=("Algerian",32), bg="orange", fg="black")
        self.title.pack(side=TOP, fill=X) # fill=X ==> Pour remplir l'axe des abscisses

        self.Main_Frame = Frame(self.root, width=1520,height=700, bg="white")
        self.Main_Frame.place(x=0, y=54)

        imageMall = customtkinter.CTkImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/malls.jpg"), size=(1520, 700))
        self.lbl_image = customtkinter.CTkLabel(self.Main_Frame,text="" ,image=imageMall, width=1520, height=700)
        self.lbl_image.place(x=0, y=0)

        btn_mall = customtkinter.CTkButton(self.root, text="MALL",command=self.Accueil,font=("Consolas",16,"bold") ,width=8,bg_color="orange",fg_color='orange',text_color="black",hover_color='white', cursor="hand2", border_color="black", border_width=1 )
        btn_mall.place(x=15,y=13)

        self.footer = Label(self.root, text="Merci pour votre présence", font=("Monotype Corsiva",22,"bold"), bg="orange", fg="black")
        self.footer.pack(side=BOTTOM, fill=X )


        self.btn_ajoutProd = Button(self.Main_Frame, text="Ajouter \nProduit",command=self.ajouterProduit ,width=12, height=2,font=("times new roman",18,"bold"), bg="orange",cursor="hand2")
        self.btn_ajoutProd.place(x=150, y= 200)

        self.btn_gestStock = Button(self.Main_Frame, text="Gerer \nProduit" ,command=self.gererProduit,width=12, height=2,font=("times new roman",18,"bold"), bg="orange",cursor="hand2")
        self.btn_gestStock.place(x=645, y= 200)

        self.btn_gestAdmin = Button(self.Main_Frame, text="Ajouter \nAdmin",command=self.ajouterAdmin,width=12, height=2,font=("times new roman",18,"bold"), bg="orange",cursor="hand2")
        self.btn_gestAdmin.place(x=1140, y= 200)


        self.btn_listCategorie = Button(self.Main_Frame, text="Lister\nCatégorie",command=self.listerCategorie ,width=12, height=2,font=("times new roman",18,"bold"), bg="orange",cursor="hand2")
        self.btn_listCategorie.place(x=150, y= 400)

        self.btn_listerProduit = Button(self.Main_Frame, text="Lister\nProduits",command=self.listerProduit,width=12, height=2,font=("times new roman",18,"bold"), bg="orange",cursor="hand2")
        self.btn_listerProduit.place(x=645, y= 400)


        self.btn_listUsers = Button(self.Main_Frame, text="Lister\nUsers" ,command=self.listerUser,width=12, height=2,font=("times new roman",18,"bold"), bg="orange",cursor="hand2")
        self.btn_listUsers.place(x=1140, y= 400)




    def Accueil(self):
        self.root.destroy()
        self.root.quit()
        from Boutiques.mall import Mall
        app = Tk()
        Mall(app)
        app.mainloop()



    def listerCategorie(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        ListerCat(app)
        app.mainloop()


    def listerProduit(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        ListerProd(app)
        app.mainloop()


    def listerUser(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        ListerUser(app)
        app.mainloop()

    def ajouterProduit(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        AjoutProd(app)
        app.mainloop()

    def ajouterAdmin(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        AjoutAdmin(app)
        app.mainloop()

    def gererProduit(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        GererProd(app)
        app.mainloop()
        



#  -------------------------------------------------Lister Categorie------------------------------------------------------------


class ListerCat :
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("750x550+320+100")
        self.root.title("LES CATÉGORIES")
        self.root.resizable(FALSE,FALSE)
        self.root.config(bg="white")
        self.MainFrame=Frame(self.root,bg="white", width=500,height=500)
        self.MainFrame.place(x=125,y=10)

        self.boutique = StringVar()

        btn_mall = customtkinter.CTkButton(self.root, text="Admin",command=self.interAdmin,font=("Consolas",16,"bold") ,width=8,bg_color="white",fg_color='white',text_color="black",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        btn_mall.place(x=15,y=13)

        self.lbl_titre = Label(self.MainFrame,text="LISTE DES CATEGORIES", font=('algerian',22),bg="white", height=2)
        self.lbl_titre.place(x=85, y=0)

        # Souligner le texte 
        f = tkFont.Font(self.lbl_titre, self.lbl_titre.cget("font"))
        f.configure(underline = True)
        self.lbl_titre.configure(font=f)

        self.lbl_filtre = Label(self.MainFrame, text="Filtre : ", font=("regular",16,), bg="white")
        self.lbl_filtre.place(x=70, y=70)

        self.txt_filtre = ttk.Combobox(self.MainFrame, font=("times new roman",12,"bold"),textvariable=self.boutique,values=listShop,width=13, state="readonly" )
        self.txt_filtre.place(x=150, y=70)
        self.txt_filtre.bind("<<ComboboxSelected>>", self.findCategorieByShop)
        self.txt_filtre.set("Mode")

        self.tabFrame = Frame(self.MainFrame, width=500, height=358, bg="white")
        self.tabFrame.place(x=0,y=130)

        self.lbl_id = ttk.Entry(self.tabFrame, width=20, font=("times new roman",17), foreground="brown",justify='center')
        self.lbl_id.grid(row=0,column=0,sticky=W,)
        self.lbl_id.insert(END, "ID")
        self.lbl_id.config(state="readonly")

        self.lbl_nom = ttk.Entry(self.tabFrame, width=20, font=("times new roman",17),foreground="brown", justify='center')
        self.lbl_nom.grid(row=0,column=1,sticky=W)
        self.lbl_nom.insert(END, "NOM")
        self.lbl_nom.config(state="readonly")
        
        self.faireTabCategorie()# recharger le tableau

    def interAdmin(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        Admin(app)
        app.mainloop()   

    def findCategorieByShop(self,even= ""):
        if self.boutique.get() == "Mode":
            base= "mode"
        elif self.boutique.get() == "Bijouterie" :
            base= "bijouterie"
        elif self.boutique.get() == "Maison" :
            base= "maison"
        elif self.boutique.get() == "Sport" :
            base= "sport"
        elif self.boutique.get() == "Restaurant" :
            base= "restaurant"
        elif self.boutique.get() == "Alimentation" :
            base= "alimentation"

        conn = sqlite3.connect(f"C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/{base}.db")
        c = conn.cursor()
        c.execute("Select * From categorie")
        dataCategorie = c.fetchall()
        conn.close()
        self.effacerTab()
        tabCategorie.clear()
        specifierCategorie(dataCategorie)
        self.faireTabCategorie()

    
    def effacerTab(self):
        for i in range(len(tabCategorie)):
            # e= ttk.Entry(self.tabFrame, width=20, font=("times new roman",17), justify='center')
            # e.grid(row=i+1, column=0,sticky=W)
            # e.delete(0,END)

            # e2 = ttk.Entry(self.tabFrame, width=20, font=("times new roman",17), justify='center', background="white")
            # e2.grid(row=i+1, column=1,sticky=W)
            # e2.delete(0,END)

            e= ttk.Label(self.tabFrame, width=20,text='' ,font=("times new roman",17), justify='center',background="white")
            e.grid(row=i+1, column=0,sticky=W)
            # e.delete(0,END)

            e2 = ttk.Label(self.tabFrame, width=20,text='' ,font=("times new roman",17), justify='center', background="white")
            e2.grid(row=i+1, column=1,sticky=W)
            # e2.delete(0,END)


    def faireTabCategorie(self):
        # faire le tableau 
        for i in range(len(tabCategorie)):

            e= ttk.Entry(self.tabFrame, width=20, font=("times new roman",17), justify='center', background="white")
            e.grid(row=i+1, column=0,sticky=W)
            e.insert(END, tabCategorie[i].id)
            e.config(state="readonly")

            e2 = ttk.Entry(self.tabFrame, width=20, font=("times new roman",17), justify='center')
            e2.grid(row=i+1, column=1,sticky=W)
            e2.insert(END, tabCategorie[i].libelle)
            e2.config(state="readonly")




# -------------------------------------Lister Produit---------------------------------------------------------------------------- 




class ListerProd:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("900x700+320+60")
        self.root.title("LES PRODUITS")
        self.root.resizable(FALSE,FALSE)
        self.root.config(bg="white")

        MainFrame = Frame(self.root, background="cyan")
        MainFrame.pack(fill=BOTH, expand=1)

        MyCanva=Canvas(MainFrame, background="white")
        MyCanva.pack(side=LEFT, fill=BOTH, expand=1)

        scroll = ttk.Scrollbar(MainFrame, orient=VERTICAL,command=MyCanva.yview)
        scroll.pack(side=RIGHT, fill=Y)

        MyCanva.configure(yscrollcommand=scroll.set)
         
        MyCanva.bind('<Configure>', lambda e: MyCanva.configure(scrollregion= MyCanva.bbox('all')))

        self.secondFrame = Frame(MyCanva, background="white")

        MyCanva.create_window((0,0), window= self.secondFrame, anchor='nw')

        self.boutique = StringVar()

        btn_mall = customtkinter.CTkButton(self.secondFrame,command=self.interAdmin ,text="Admin",font=("Consolas",16,"bold") ,width=8,bg_color="white",fg_color='white',text_color="black",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        btn_mall.grid(row=0, column=0, pady=10)

        self.lbl_titre = Label(self.secondFrame,text="LISTE DES PRODUITS", font=('algerian',22),bg="white", height=2)
        self.lbl_titre.place(x=270, y=0)

        # Souligner le texte 
        f = tkFont.Font(self.lbl_titre, self.lbl_titre.cget("font"))
        f.configure(underline = True)
        self.lbl_titre.configure(font=f)

        self.lbl_filtre = Label(self.secondFrame, text="Filtre : ", font=("regular",16,), bg="white")
        self.lbl_filtre.grid(row=1, column=1, pady=20)

        self.txt_filtre = ttk.Combobox(self.secondFrame, font=("times new roman",12,"bold"),textvariable=self.boutique,values=listShop,width=13, state="readonly" )
        self.txt_filtre.place(x=350, y=70)
        self.txt_filtre.bind('<<ComboboxSelected>>', self.findProduitByShop)
        self.txt_filtre.set("Mode")

        self.lbl_id = ttk.Entry(self.secondFrame, width=10, font=("times new roman",17), foreground="brown",justify='center')
        self.lbl_id.grid(row=2,column=0,sticky=W,padx=(90,0))
        self.lbl_id.insert(END, "ID")
        self.lbl_id.config(state="readonly")

        self.lbl_nom = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17),foreground="brown", justify='center')
        self.lbl_nom.grid(row=2,column=1,sticky=W)
        self.lbl_nom.insert(END, "NOM")
        self.lbl_nom.config(state="readonly")

        self.lbl_id = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17), foreground="brown",justify='center')
        self.lbl_id.grid(row=2,column=2,sticky=W,)
        self.lbl_id.insert(END, "S-CATEGORIE")
        self.lbl_id.config(state="readonly")

        self.lbl_nom = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17),foreground="brown", justify='center')
        self.lbl_nom.grid(row=2,column=3,sticky=W)
        self.lbl_nom.insert(END, "CATEGORIE")
        self.lbl_nom.config(state="readonly")

        self.faireTabProduit()



    def interAdmin(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        Admin(app)
        app.mainloop()  


    def findProduitByShop(self,even= ""):
        if self.boutique.get() == "Mode":
            base= "mode"
        elif self.boutique.get() == "Bijouterie" :
            base= "bijouterie"
        elif self.boutique.get() == "Maison" :
            base= "maison"
        elif self.boutique.get() == "Sport" :
            base= "sport"
        elif self.boutique.get() == "Restaurant" :
            base= "restaurant"
        elif self.boutique.get() == "Alimentation" :
            base= "alimentation"

        conn = sqlite3.connect(f"C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/{base}.db")
        c = conn.cursor()
        c.execute("Select * From produit")
        dataProduit = c.fetchall()
        c.execute("Select * From categorie")
        dataCategorie = c.fetchall()
        c.execute("Select * From souscategorie")
        dataSousCategorie = c.fetchall()
        conn.close()
        self.effacerTab()
        tabProduit.clear()
        tabCategorie.clear()
        tabSousCategorie.clear()
        specifierProduit(dataProduit)
        specifierCategorie(dataCategorie)
        specifierSousCategorie(dataSousCategorie)
        self.faireTabProduit() 


    def findSousCategorieById(self,id):
        for i in tabSousCategorie :
            if i.id == id :
                return i
            
    def findCategorieById(self,id):
        for i in tabCategorie :
            if i.id == id :
                return i
            
    def effacerTab(self):
        for i in range(len(tabProduit)):

            e= ttk.Label(self.secondFrame, width=10,text='' ,font=("times new roman",17), justify='center',background="white")
            e.grid(row=i+4, column=0,sticky=W, padx=(90,0))

            e2 = ttk.Label(self.secondFrame, width=16,text='' ,font=("times new roman",17), justify='center',background="white")
            e2.grid(row=i+4, column=1,sticky=W)

            e3 = ttk.Label(self.secondFrame, width=16,text='' ,font=("times new roman",17), justify='center',background="white")
            e3.grid(row=i+4, column=2,sticky=W)

            e4 = ttk.Label(self.secondFrame, width=16,text='' ,font=("times new roman",17), justify='center',background="white")
            e4.grid(row=i+4, column=3,sticky=W)
           

    def faireTabProduit(self):
        for i in range(len(tabProduit)):

            e = ttk.Entry(self.secondFrame, width=10, font=("times new roman",17), justify='center', background="white")
            e.grid(row=i+4, column=0,sticky=W, padx=(90,0))
            e.insert(END, tabProduit[i].id)
            e.config(state="readonly")

            e2 = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17), justify='center')
            e2.grid(row=i+4, column=1,sticky=W)
            e2.insert(END, tabProduit[i].nom)
            e2.config(state="readonly")

            scat = self.findSousCategorieById(tabProduit[i].idSousCategorie)
            cat = self.findCategorieById(scat.idCategorie)

            e3 = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17), justify='center')
            e3.grid(row=i+4, column=2,sticky=W)
            e3.insert(END, scat.libelle)
            e3.config(state="readonly")

            e4 = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17), justify='center')
            e4.grid(row=i+4, column=3,sticky=W)
            e4.insert(END,cat.libelle )
            e4.config(state="readonly")




# ----------------------------------Lister Users---------------------------------------------------------------------------


class ListerUser :
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("900x550+320+100")
        self.root.title("LES UTILISATEURS")
        self.root.resizable(FALSE,FALSE)
        self.root.config(bg="white")

        self.MainFrame=Frame(self.root,bg="white", width=900,height=550)
        self.MainFrame.place(x=0,y=10)

        self.boutique = StringVar()
        self.choix_role = StringVar()
        self.choix_etat = StringVar()
        self.id = IntVar()
        self.choix_role.set("All")
        self.choix_etat.set("All")
        self.user = User(0,"","","","",1,1)

        btn_mall = customtkinter.CTkButton(self.root, text="Admin",command=self.interAdmin,font=("Consolas",16,"bold") ,width=8,bg_color="white",fg_color='white',text_color="black",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        btn_mall.place(x=15,y=13)

        self.lbl_titre = Label(self.MainFrame,text="LISTE DES UTILISATEURS", font=('algerian',22),bg="white", height=2)
        self.lbl_titre.place(x=255, y=0)

        # Souligner le texte 
        f = tkFont.Font(self.lbl_titre, self.lbl_titre.cget("font"))
        f.configure(underline = True)
        self.lbl_titre.configure(font=f)

        self.lbl_filtre = Label(self.MainFrame, text="Filtre : ", font=("regular",16,), bg="white")
        self.lbl_filtre.place(x=200, y=60)

        self.lbl_role = Label(self.MainFrame, text="Rôle : ", font=("regular",14,), bg="white")
        self.lbl_role.place(x=270, y=100)

        self.txt_filtre_role = ttk.Combobox(self.MainFrame, font=("times new roman",12,"bold"),textvariable=self.choix_role,values=["All","Admin","Client"],width=13, state="readonly" )
        self.txt_filtre_role.place(x=340, y=100)
        self.txt_filtre_role.bind("<<ComboboxSelected>>", self.choixRoleEtat)
        self.txt_filtre_role.set("All")

        self.lbl_etat = Label(self.MainFrame, text="Etat : ", font=("regular",14,), bg="white")
        self.lbl_etat.place(x=500, y=100)

        self.txt_filtre_etat = ttk.Combobox(self.MainFrame, font=("times new roman",12,"bold"),textvariable=self.choix_etat,values=["All","Actif","Suspendu"],width=13, state="readonly" )
        self.txt_filtre_etat.place(x=570, y=100)
        self.txt_filtre_etat.bind("<<ComboboxSelected>>", self.choixRoleEtat)
        self.txt_filtre_etat.set("All")


        self.tabFrame = Frame(self.MainFrame, width=800, height=358, bg="white")
        self.tabFrame.place(x=18,y=180)

        self.lbl_id = ttk.Entry(self.tabFrame, width=5, font=("times new roman",17), foreground="brown",justify='center')
        self.lbl_id.grid(row=0,column=0,sticky=W,)
        self.lbl_id.insert(END, "ID")
        self.lbl_id.config(state="readonly")

        self.lbl_nom = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17),foreground="brown", justify='center')
        self.lbl_nom.grid(row=0,column=1,sticky=W)
        self.lbl_nom.insert(END, "NOM")
        self.lbl_nom.config(state="readonly")

        self.lbl_prenom = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17),foreground="brown", justify='center')
        self.lbl_prenom.grid(row=0,column=2,sticky=W)
        self.lbl_prenom.insert(END, "PRENOM")
        self.lbl_prenom.config(state="readonly")

        self.lbl_login = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17),foreground="brown", justify='center')
        self.lbl_login.grid(row=0,column=3,sticky=W)
        self.lbl_login.insert(END, "LOGIN")
        self.lbl_login.config(state="readonly")

        self.lbl_role = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17),foreground="brown", justify='center')
        self.lbl_role.grid(row=0,column=4,sticky=W)
        self.lbl_role.insert(END, "ROLE")
        self.lbl_role.config(state="readonly")

        self.lbl_etat = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17),foreground="brown", justify='center')
        self.lbl_etat.grid(row=0,column=5,sticky=W)
        self.lbl_etat.insert(END, "ETAT")
        self.lbl_etat.config(state="readonly")

        self.lbl_rech = Label(self.MainFrame, text="Entrez l'ID  : ", font=("regular",16,), bg="white")
        self.lbl_rech.place(x=200, y=430)

        self.lbl_rech_id = Entry(self.MainFrame, width=10,border=2 ,textvariable=self.id, font=("regular",16))
        self.lbl_rech_id.place(x=330, y=430)

        self.lbl_action = Label(self.MainFrame, text="ACTIONS  : ", font=("regular",16,), bg="white")
        self.lbl_action.place(x=200, y=490)

        self.btn_bloquer = customtkinter.CTkButton(self.MainFrame, text="Bloquer",command=self.bloquer,font=("Consolas",16,"bold") ,width=15, height=35,bg_color="white",fg_color='red',text_color="black",hover_color='white', cursor="hand2", border_color="black", border_width=1 )
        self.btn_bloquer.place(x=330, y=490)

        self.btn_debloquer = customtkinter.CTkButton(self.MainFrame, text="Débloquer",command=self.debloquer,font=("Consolas",16,"bold") ,width=15, height=35,bg_color="white",fg_color='green',text_color="black",hover_color='white', cursor="hand2", border_color="black", border_width=1 )
        self.btn_debloquer.place(x=430, y=490)



        
        self.faireTabUser()# recharger le tableau

    def interAdmin(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        Admin(app)
        app.mainloop()  

    def role(self,n:int):
        if n==1:
            return "Admin"
        else :
            return "Client" 
    
    def etat(self,n:int):
        if n==1:
            return "Actif"
        else :
            return "Suspendu" 
    
    
    def choixRoleEtat(self, even=""):
        # Supprimer ancien tab
        self.effacerTab()
        tabUserChoix = []

        if self.choix_etat.get()== "All": # on ne choisit aucun état

            if self.choix_role.get()=="All": # aucun role
                tabUserChoix = tabUser

            elif self.choix_role.get()== "Admin": #  role = 1
                for i in tabUser:
                    if i.role == 1 :
                        tabUserChoix.append(i)

            elif self.choix_role.get()=="Client":  # role = 2
                for i in tabUser:
                    if i.role == 2 :
                        tabUserChoix.append(i)

        elif self.choix_etat.get()=="Actif": # Etat = 1

            if self.choix_role.get()=="All": # Aucun role choisi
                for i in tabUser:
                    if i.etat == 1 :
                        tabUserChoix.append(i)

            elif self.choix_role.get()== "Admin": # role = 1
                for i in tabUser:
                    if i.etat == 1 and i.role == 1 :
                        tabUserChoix.append(i)

            elif self.choix_role.get()=="Client":  # role = 2
                for i in tabUser:
                    if i.etat == 1 and i.role == 2 :
                        tabUserChoix.append(i)
        
        elif self.choix_etat.get()=="Suspendu": # etat = 0

            if self.choix_role.get()=="All": # aucun role choisit
                for i in tabUser:
                    if i.etat == 0 :
                        tabUserChoix.append(i)

            elif self.choix_role.get()== "Admin": # role = 1
                for i in tabUser:
                    if i.etat == 0 and i.role == 1 :
                        tabUserChoix.append(i)

            elif self.choix_role.get()=="Client": # role = 2
                for i in tabUser:
                    if i.etat == 0 and i.role == 2 :
                        tabUserChoix.append(i)
         
        # Faire nouveau tab
        self.faireTabUser(tabUserChoix)


    def effacerTab(self):

        for i in range(len(tabUser)):
            e= ttk.Label(self.tabFrame, width=5,text='' ,font=("times new roman",17), justify='center',background="white")
            e.grid(row=i+1, column=0,sticky=W)

            e2 = ttk.Label(self.tabFrame, width=14,text='' ,font=("times new roman",17), justify='center',background="white")
            e2.grid(row=i+1, column=1,sticky=W)

            e3 = ttk.Label(self.tabFrame, width=14,text='' ,font=("times new roman",17), justify='center',background="white")
            e3.grid(row=i+1, column=2,sticky=W)

            e4 = ttk.Label(self.tabFrame, width=14,text='' ,font=("times new roman",17), justify='center',background="white")
            e4.grid(row=i+1, column=3,sticky=W)

            e4 = ttk.Label(self.tabFrame, width=14,text='' ,font=("times new roman",17), justify='center',background="white")
            e4.grid(row=i+1, column=4,sticky=W)

            e5 = ttk.Label(self.tabFrame, width=14,text='' ,font=("times new roman",17), justify='center',background="white")
            e5.grid(row=i+1, column=5,sticky=W)
    

    def faireTabUser(self, tab = tabUser):
        # faire le tableau 
        for i in range(len(tab)):

            e= ttk.Entry(self.tabFrame, width=5, font=("times new roman",17), justify='center')
            e.grid(row=i+1, column=0,sticky=W)
            e.insert(END, tab[i].id)
            e.config(state="readonly")

            e2 = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17), justify='center')
            e2.grid(row=i+1, column=1,sticky=W)
            e2.insert(END, tab[i].nom)
            e2.config(state="readonly")

            e3 = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17), justify='center')
            e3.grid(row=i+1, column=2,sticky=W)
            e3.insert(END, tab[i].prenom)
            e3.config(state="readonly")

            e4 = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17), justify='center')
            e4.grid(row=i+1, column=3,sticky=W)
            e4.insert(END, tab[i].login)
            e4.config(state="readonly")

            e5 = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17), justify='center')
            e5.grid(row=i+1, column=4,sticky=W)
            e5.insert(END, self.role(tab[i].role))
            e5.config(state="readonly")

            e6 = ttk.Entry(self.tabFrame, width=14, font=("times new roman",17), justify='center')
            e6.grid(row=i+1, column=5,sticky=W)
            e6.insert(END, self.etat(tab[i].etat))
            e6.config(state="readonly")


    def rechercheUserById(self, id):
        for i in tabUser :
            if i.id == id :
                return i


    def bloquer(self):
        if self.id.get() < 1 or self.id.get()> len(tabUser) or self.id.get()== 0 : 
            messagebox.showerror("ERROR ID", "Cet ID ne correspond à aucun Utilisateur.")
        else:
            self.user = self.rechercheUserById(self.id.get())
            if self.user.etat == 0 :
                messagebox.showinfo("Info", f"Ah Chef, {self.user.nom} {self.user.prenom} est déjà suspendu")
            else:
                op = messagebox.askyesno("Confirmation", f"Voulez-vous bloquer {self.user.nom} {self.user.prenom} ?")

                if op == True :
                    tabUser[self.user.id - 1].etat = 0
                    conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/user.db")
                    c = conn.cursor()
                    c.execute(f"""
                        UPDATE user
                        SET etat = 0
                        WHERE id == {self.user.id}
                    """)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("SUCCESS", f"{self.user.nom} {self.user.prenom} a été bloqué avec succès.")
        self.id.set(0)




    def debloquer(self):
        if self.id.get() < 1 or self.id.get()> len(tabUser) or self.id.get()==0  : 
            messagebox.showerror("ERROR ID", "Cet ID ne correspond à aucun Utilisateur.")
        else:
            self.user = self.rechercheUserById(self.id.get())
            if self.user.etat == 1 :
                messagebox.showinfo("Info", f"Ah Chef, {self.user.nom} {self.user.prenom} est déjà actif")
            else:
                op = messagebox.askyesno("Confirmation", f"Voulez-vous débloquer {self.user.nom} {self.user.prenom} ?")

                if op == True :
                    tabUser[self.user.id - 1].etat = 1
                    conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/user.db")
                    c = conn.cursor()
                    c.execute(f"""
                        UPDATE user
                        SET etat = 1
                        WHERE id == {self.user.id}
                    """)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("SUCCESS", f"{self.user.nom} {self.user.prenom} a été débloqué avec succès.")
        self.id.set(0)




#---------------------------------------------------Ajout Produit------------------------------------------------------

class AjoutProd:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("800x600+350+90")
        self.root.title("Ajout de Produit")
        self.root.resizable(FALSE,FALSE)

        #-----------Variables à utiliser--------
        self.boutique = StringVar()
        self.categorie = StringVar()
        self.idCategorie = IntVar()
        self.SousCategorie = StringVar()
        self.idSousCategorie = IntVar()
        self.nom = StringVar()
        self.stock = IntVar()
        self.prix = IntVar()
        self.nomImage = StringVar()
        self.base = ''

        MainFrame = Frame(self.root, background="white")
        MainFrame.pack(fill=BOTH, expand=1)

        btn_mall = customtkinter.CTkButton(MainFrame, text="Admin",command=self.interAdmin,font=("Consolas",16,"bold") ,width=8,bg_color="white",fg_color='white',text_color="black",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        btn_mall.place(x=15,y=13)

        self.lbl_titre = Label(MainFrame,text="AJOUT DE PRODUIT", font=('algerian',22),background='white', height=2)
        self.lbl_titre.place(x=245, y=30)

        # Souligner le texte 
        f = tkFont.Font(self.lbl_titre, self.lbl_titre.cget("font"))
        f.configure(underline = True)
        self.lbl_titre.configure(font=f)

        self.formFrame = Frame(MainFrame, background="#E1E1E2", width=500, height=450)
        self.formFrame.place(x=130, y=100)

        self.lbl_boutique = Label(self.formFrame, text="Boutique : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_boutique.place(x=30, y=10)

        self.txt_boutique = ttk.Combobox(self.formFrame, font=("times new roman",16,"bold"),textvariable=self.boutique,values=listShop,width=15, state="readonly" )
        self.txt_boutique.place(x=220, y=10)
        self.txt_boutique.bind('<<ComboboxSelected>>',self.chargerCategorie )
        self.txt_boutique.set("Mode")


        self.lbl_categorie = Label(self.formFrame, text="Catégorie : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_categorie.place(x=30, y=60)

        self.txt_categorie = ttk.Combobox(self.formFrame, font=("times new roman",16,"bold"),textvariable=self.categorie,values=[],width=15, state="readonly" )
        self.txt_categorie.place(x=220, y=60)
        self.txt_categorie.bind('<<ComboboxSelected>>',self.chargerSousCategorie)
        


        self.lbl_souscategorie = Label(self.formFrame, text="Sous-Catégorie : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_souscategorie.place(x=30, y=110)

        self.txt_souscategorie = ttk.Combobox(self.formFrame, font=("times new roman",16,"bold"),textvariable=self.SousCategorie,values=[],width=15, state="readonly" )
        self.txt_souscategorie.place(x=220, y=110)
        self.txt_souscategorie.bind('<<ComboboxSelected>>', self.choisirSousCategorie)
    

        self.lbl_nom = Label(self.formFrame, text="Nom Produit : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_nom.place(x=30, y=160)

        self.txt_nom = customtkinter.CTkEntry(self.formFrame, width=190,textvariable=self.nom ,font=("times new roman",18,"bold"), state='readonly')
        self.txt_nom.place(x=220, y=160)

        self.lbl_prix = Label(self.formFrame, text="Prix : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_prix.place(x=30, y=210)

        self.txt_prix = customtkinter.CTkEntry(self.formFrame, width=190,font=("times new roman",18,"bold"), state='readonly')
        self.txt_prix.place(x=220, y=210)

        self.lbl_stock = Label(self.formFrame, text="Stock : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_stock.place(x=30, y=260)

        self.txt_stock = customtkinter.CTkEntry(self.formFrame, width=190 ,font=("times new roman",18,"bold"), state='readonly')
        self.txt_stock.place(x=220, y=260)

        self.lbl_image = Label(self.formFrame, text="Image : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_image.place(x=30, y=310)

        self.txt_image = customtkinter.CTkEntry(self.formFrame, width=190 ,font=("times new roman",18,"bold"), placeholder_text='ex : image.jpg', placeholder_text_color="gray", state='readonly')
        self.txt_image.place(x=220, y=310)

        self.btn_annuler = customtkinter.CTkButton(self.formFrame,command=self.annuler ,text="Annuler",font=("Consolas",16,"bold") ,width=15, height=35,bg_color="#E1E1E2",fg_color='red',text_color="white",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        self.btn_annuler.place(x=100, y=400)

        self.btn_valider = customtkinter.CTkButton(self.formFrame,command=self.valider ,text="Valider",font=("Consolas",16,"bold") ,width=15, height=35,bg_color="#E1E1E2",fg_color='green',text_color="white",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        self.btn_valider.place(x=300, y=400)





    def interAdmin(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        Admin(app)
        app.mainloop()

    def chargerCategorie(self, even=""):
        tabCategorie.clear()
        tabProduit.clear()
        tabSousCategorie.clear()
        listCategorie.clear()
        listSousCategorie.clear()
        listProduit.clear()
        if self.boutique.get() == "Mode":
            self.base= "mode"
        elif self.boutique.get() == "Bijouterie" :
            self.base= "bijouterie"
        elif self.boutique.get() == "Maison" :
            self.base= "maison"
        elif self.boutique.get() == "Sport" :
            self.base= "sport"
        elif self.boutique.get() == "Restaurant" :
            self.base= "restaurant"
        elif self.boutique.get() == "Alimentation" :
            self.base= "alimentation"

        conn = sqlite3.connect(f"C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/{self.base}.db")
        c = conn.cursor()
        c.execute("Select * From produit")
        dataProduit = c.fetchall()
        c.execute("Select * From categorie")
        dataCategorie = c.fetchall()
        c.execute("Select * From souscategorie")
        dataSousCategorie = c.fetchall()
        conn.close() 
        specifierProduit(dataProduit)
        specifierCategorie(dataCategorie)
        specifierSousCategorie(dataSousCategorie)
        self.txt_categorie.config(values=listCategorie)
        self.txt_categorie.set(listCategorie[0])

    def findCategorieId(self,libelle):
        for i in tabCategorie:
            if i.libelle == libelle :
                return i.id 
    
    def findSousCategorieId(self,libelle):
        for i in tabSousCategorie:
            if i.libelle == libelle :
                return i.id 


    def chargerSousCategorie(self, even=""):
        listSousCategorie.clear()
        listProduit.clear()
        self.idCategorie.set(self.findCategorieId(self.categorie.get()))
        
        for i in tabSousCategorie :
            if i.idCategorie == self.idCategorie.get() :
                listSousCategorie.append(i.libelle)

        self.txt_souscategorie.config(values=listSousCategorie)
        self.txt_souscategorie.set(listSousCategorie[0])

    def choisirSousCategorie(self, even=""):
        listProduit.clear()
        self.idSousCategorie.set(self.findSousCategorieId(self.SousCategorie.get()))

        for i in tabProduit :
            if i.idSousCategorie == self.idSousCategorie.get() :
                listProduit.append(i.nom)

        self.txt_nom.configure(state="normal")
        self.txt_prix.configure(state="normal")
        self.txt_stock.configure(state="normal")
        self.txt_image.configure(state="normal", placeholder_text='ex : image.jpg', placeholder_text_color="gray")


    def annuler(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        Admin(app)
        app.mainloop()

    def rechercheProduit(self, nom):
        for i in listProduit:
            if i.lower() == nom.lower() :
                return True
        return False

    def valider(self):
        if self.nom.get().strip() =="":
            messagebox.showerror("ERROR NOM", "Veuillez  saisir le nom du produit")
        elif len(self.nom.get().strip()) <2:
            messagebox.showerror("ERROR NOM", "Veuillez  saisir un nom de produit valide")
        elif self.rechercheProduit(self.nom.get()) == True :
            messagebox.showerror("ERROR NOM", "Ce Produit existe déjà dans cette Sous-Catégorie, veuillez modifier le nom.")
        elif self.txt_prix.get().strip() == "":
            messagebox.showerror("ERROR PRIX", "Veuillez  saisir le prix du produit")
        elif self.txt_prix.get().strip().isdigit()==False:
            messagebox.showerror("ERROR PRIX", "Un prix est composé de valeur entière !")
        elif int(self.txt_prix.get()) <100 :
            messagebox.showerror("ERROR PRIX", "Le prix minimum d'un produit de la boutique est 100 !")
        elif self.txt_stock.get().strip() == "":
            messagebox.showerror("ERROR STOCK", "Veuillez  saisir le stock du produit")
        elif self.txt_stock.get().strip().isdigit()==False:
            messagebox.showerror("ERROR STOCK", "Le Stock est un nombre supérieur à zéro.")
        elif int(self.txt_stock.get().strip())>100:
            messagebox.showerror("ERROR STOCK", "Ah Chef,Tu abuses ! Il s'agirait de doser !")
        elif self.txt_image.get().strip() == "":
            messagebox.showerror("ERROR IMAGE", "Veuillez  saisir le nom de l'image du produit")
        elif '.' not in self.txt_image.get():
            messagebox.showerror("ERROR IMAGE FORMAT", "Veuillez  saisir le format de l'image 'image.format'")
        else:
            l = self.txt_image.get().split('.')
            if l[1].lower() != 'jpg' and l[1].lower() != 'jpeg' and l[1].lower() != 'png' :
                messagebox.showerror("ERROR IMAGE FORMAT", "Veuillez  saisir un format correct d'image : JPG, PNG ou JPEG")
            else :
                self.prix.set(int(self.txt_prix.get()))
                self.stock.set(int(self.txt_stock.get()))
                self.nomImage.set(self.txt_image.get())

            prod = Produit(len(tabProduit)+1,self.nom.get(),self.prix.get(),self.stock.get(),self.idSousCategorie.get(),self.nomImage.get())
            tabProduit.append(prod)

            conn = sqlite3.connect(f"C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/{self.base}.db")
            c = conn.cursor()
            param = {"i": self.nom.get(), "l": self.prix.get(), "p": self.stock.get(), "q": self.idSousCategorie.get(),"r":self.nomImage.get()}
            c.execute("""
                INSERT INTO produit(nom,prix,stock,idSousCategorie,image)
                VALUES(:i,:l,:p,:q,:r)
            """, param)
            conn.commit()
            conn.close()

            messagebox.showinfo("SUCCESS", "Produit ajouté avec succès !!!")
            self.annuler()


       

#---------------------------------------------------Ajout d'Admin--------------------------------------------------------------                     


class AjoutAdmin:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("600x550+450+110")
        self.root.title("Création de Compte Admin")
        self.root.resizable(FALSE,FALSE)

        # Variable 
        self.user = User(0,"","","","",1,1)

        self.imageMall = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/malls.jpg"))
        self.lbl_image = Label(self.root, image=self.imageMall)
        self.lbl_image.place(x=0, y=0)

        elFrame = customtkinter.CTkFrame(self.root,width=320, height=460, fg_color="#E1E1E2")
        elFrame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        lbl_title = customtkinter.CTkLabel(elFrame, text="Ajouter Admin",font=('Century Gothic',20))
        lbl_title.place(x=80, y=45)

        self.nom= customtkinter.CTkEntry(elFrame, width=220, placeholder_text='Entrez le nom')
        self.nom.place(x=50, y=90)

        self.prenom= entry2=customtkinter.CTkEntry(master=elFrame, width=220, placeholder_text='Entrez le Prénom')
        self.prenom.place(x=50, y=140)

        self.login= customtkinter.CTkEntry(elFrame, width=220, placeholder_text='Entrez le Login')
        self.login.place(x=50, y=190)

        self.password= entry2=customtkinter.CTkEntry(master=elFrame, width=220, placeholder_text='Entrez le Mot de Passe', show="*")
        self.password.place(x=50, y=240)

        self.password2= entry2=customtkinter.CTkEntry(master=elFrame, width=220, placeholder_text='Confirmez le Mot de Passe', show="*")
        self.password2.place(x=50, y=290)

        self.btn_annuler = customtkinter.CTkButton(elFrame,command=self.annuler ,text="Annuler",font=("Consolas",16,"bold") ,width=15, height=35,bg_color="#E1E1E2",fg_color='red',text_color="white",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        self.btn_annuler.place(x=50, y=360)

        self.btn_valider = customtkinter.CTkButton(elFrame,command=self.ajouterCompte ,text="Valider",font=("Consolas",16,"bold") ,width=15, height=35,bg_color="#E1E1E2",fg_color='green',text_color="white",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        self.btn_valider.place(x=195, y=360)



    def annuler(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        Admin(app)
        app.mainloop()

    def rechercheLogin(self, login):
        for i in tabUser :
            if login == i.login  :
                return True
        return False


    def ajouterCompte(self):
        if self.nom.get().strip() =="":
            messagebox.showerror("Error nom", "Veuillez  saisir le nom")
        elif len(self.nom.get().strip()) <2:
            messagebox.showerror("Error nom", "Veuillez  saisir un nom Valide")
        elif self.prenom.get().strip() =="":
            messagebox.showerror("Error Prenom", "Veuillez  saisir le prénom")
        elif len(self.prenom.get().strip()) <2:
            messagebox.showerror("Error Prenom", "Veuillez  saisir un prénom valide")
        elif self.login.get().strip() =="":
            messagebox.showerror("Error Login", "Veuillez  saisir le Login")
        elif len(self.login.get().strip()) <4:
            messagebox.showerror("Error Login", "Un Login contient au moins 4 caracteres")
        elif self.password.get().strip() =="":
            messagebox.showerror("Error Password", "Veuillez  saisir le Mot de passe")
        elif len(self.password.get().strip()) <4:
            messagebox.showerror("Error Password", "Un Password contient au moins 4 caracteres")
        elif self.password2.get().strip() =="":
            messagebox.showerror("Error Password", "Veuillez Confirmer le Mot de passe")
        elif self.password2.get().strip() != self.password.get().strip() :
            messagebox.showerror("Error Confirmation", "Les mots de passe ne correspondent pas !")
        else :
            result = self.rechercheLogin(self.login.get())
            if result == True :
                messagebox.showwarning("Attention", f"le nom d'utilisateur {self.login.get()} n'est pas disponible !")
            else:
                conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/user.db")
                c = conn.cursor()
                self.user = User(len(tabUser)+1,self.nom.get(),self.prenom.get(),self.login.get(),self.password.get(),1,1)
                tabUser.append(self.user)
                param = {"i": self.nom.get(), "l": self.prenom.get(), "p": self.login.get(), "q": self.password.get(),"r":1,"t":1}
                c.execute("""
                    INSERT INTO user(nom,prenom,login,password,role,etat)
                    VALUES(:i,:l,:p,:q,:r,:t)
                """, param)
                conn.commit()
                conn.close()
                messagebox.showinfo("SUCCES","Nouveau administrateur ajouté avec succès !")
                self.annuler()




#-------------------------------------Gestion de Produit----------------------------------------------------------------------------


class GererProd:
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x600+350+90")
        self.root.title("Ajout de Produit")
        self.root.resizable(FALSE,FALSE)

        #-----------Variables à utiliser--------
        self.boutique = StringVar()
        self.categorie = StringVar()
        self.idCategorie = IntVar()
        self.SousCategorie = StringVar()
        self.idSousCategorie = IntVar()
        self.nom = StringVar()
        self.stock = IntVar()
        self.prix = IntVar()
        self.nomImage = StringVar()
        self.base = ''
        self.produit = Produit(0,"",0,0,0,"")

        MainFrame = Frame(self.root, background="white")
        MainFrame.pack(fill=BOTH, expand=1)

        btn_mall = customtkinter.CTkButton(MainFrame, text="Admin",command=self.interAdmin,font=("Consolas",16,"bold") ,width=8,bg_color="white",fg_color='white',text_color="black",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        btn_mall.place(x=15,y=13)

        self.lbl_titre = Label(MainFrame,text="GESTION DE PRODUIT", font=('algerian',22),background='white', height=2)
        self.lbl_titre.place(x=245, y=30)

        # Souligner le texte 
        f = tkFont.Font(self.lbl_titre, self.lbl_titre.cget("font"))
        f.configure(underline = True)
        self.lbl_titre.configure(font=f)

        self.formFrame = Frame(MainFrame, background="#E1E1E2", width=500, height=450)
        self.formFrame.place(x=130, y=100)

        self.lbl_boutique = Label(self.formFrame, text="Boutique : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_boutique.place(x=30, y=10)

        self.txt_boutique = ttk.Combobox(self.formFrame, font=("times new roman",16,"bold"),textvariable=self.boutique,values=listShop,width=15, state="readonly" )
        self.txt_boutique.place(x=220, y=10)
        self.txt_boutique.bind('<<ComboboxSelected>>',self.chargerCategorie )
        self.txt_boutique.set("Mode")


        self.lbl_categorie = Label(self.formFrame, text="Catégorie : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_categorie.place(x=30, y=60)

        self.txt_categorie = ttk.Combobox(self.formFrame, font=("times new roman",16,"bold"),textvariable=self.categorie,values=[],width=15, state="readonly" )
        self.txt_categorie.place(x=220, y=60)
        self.txt_categorie.bind('<<ComboboxSelected>>',self.chargerSousCategorie)
        


        self.lbl_souscategorie = Label(self.formFrame, text="Sous-Catégorie : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_souscategorie.place(x=30, y=110)

        self.txt_souscategorie = ttk.Combobox(self.formFrame, font=("times new roman",16,"bold"),textvariable=self.SousCategorie,values=[],width=15, state="readonly" )
        self.txt_souscategorie.place(x=220, y=110)
        self.txt_souscategorie.bind('<<ComboboxSelected>>', self.choisirSousCategorie)
    

        self.lbl_nom = Label(self.formFrame, text="Nom Produit : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_nom.place(x=30, y=160)

        self.txt_nom = ttk.Combobox(self.formFrame, font=("times new roman",16,"bold"),textvariable=self.nom,values=[],width=15, state="readonly" )
        self.txt_nom.place(x=220, y=160)
        self.txt_nom.bind('<<ComboboxSelected>>',self.choisirProduit)

        self.lbl_prix = Label(self.formFrame, text="Prix : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_prix.place(x=30, y=210)

        self.txt_prix = customtkinter.CTkEntry(self.formFrame, width=190,font=("times new roman",18,"bold"), state='readonly')
        self.txt_prix.place(x=220, y=210)

        self.lbl_stock = Label(self.formFrame, text="Stock : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_stock.place(x=30, y=260)

        self.txt_stock = customtkinter.CTkEntry(self.formFrame, width=190 ,font=("times new roman",18,"bold"), state='readonly')
        self.txt_stock.place(x=220, y=260)

        self.lbl_image = Label(self.formFrame, text="Image : ", font=("regular",16,), bg="#E1E1E2")
        self.lbl_image.place(x=30, y=310)

        self.txt_image = customtkinter.CTkEntry(self.formFrame, width=190 ,font=("times new roman",18,"bold"), placeholder_text='ex : image.jpg', placeholder_text_color="gray", state='readonly')
        self.txt_image.place(x=220, y=310)

        self.btn_annuler = customtkinter.CTkButton(self.formFrame,command=self.annuler ,text="Annuler",font=("Consolas",16,"bold") ,width=15, height=35,bg_color="#E1E1E2",fg_color='red',text_color="white",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        self.btn_annuler.place(x=100, y=400)

        self.btn_valider = customtkinter.CTkButton(self.formFrame,command=self.valider ,text="Valider",font=("Consolas",16,"bold") ,width=15, height=35,bg_color="#E1E1E2",fg_color='green',text_color="white",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
        self.btn_valider.place(x=300, y=400)





    def interAdmin(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        Admin(app)
        app.mainloop()

    def chargerCategorie(self, even=""):
        tabCategorie.clear()
        tabProduit.clear()
        tabSousCategorie.clear()
        listCategorie.clear()
        listSousCategorie.clear()
        listProduit.clear()
        if self.boutique.get() == "Mode":
            self.base= "mode"
        elif self.boutique.get() == "Bijouterie" :
            self.base= "bijouterie"
        elif self.boutique.get() == "Maison" :
            self.base= "maison"
        elif self.boutique.get() == "Sport" :
            self.base= "sport"
        elif self.boutique.get() == "Restaurant" :
            self.base= "restaurant"
        elif self.boutique.get() == "Alimentation" :
            self.base= "alimentation"

        conn = sqlite3.connect(f"C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/{self.base}.db")
        c = conn.cursor()
        c.execute("Select * From produit")
        dataProduit = c.fetchall()
        c.execute("Select * From categorie")
        dataCategorie = c.fetchall()
        c.execute("Select * From souscategorie")
        dataSousCategorie = c.fetchall()
        conn.close() 
        specifierProduit(dataProduit)
        specifierCategorie(dataCategorie)
        specifierSousCategorie(dataSousCategorie)
        self.txt_categorie.config(values=listCategorie)
        self.txt_categorie.set(listCategorie[0])

    def findCategorieId(self,libelle):
        for i in tabCategorie:
            if i.libelle == libelle :
                return i.id 
    
    def findSousCategorieId(self,libelle):
        for i in tabSousCategorie:
            if i.libelle == libelle :
                return i.id 


    def chargerSousCategorie(self, even=""):
        listSousCategorie.clear()
        listProduit.clear()
        self.idCategorie.set(self.findCategorieId(self.categorie.get()))
        
        for i in tabSousCategorie :
            if i.idCategorie == self.idCategorie.get() :
                listSousCategorie.append(i.libelle)

        self.txt_souscategorie.config(values=listSousCategorie)
        self.txt_souscategorie.set(listSousCategorie[0])

    def choisirSousCategorie(self, even=""):
        listProduit.clear()
        self.idSousCategorie.set(self.findSousCategorieId(self.SousCategorie.get()))

        for i in tabProduit :
            if i.idSousCategorie == self.idSousCategorie.get() :
                listProduit.append(i.nom)
        
        self.txt_nom.configure(values=listProduit)
        self.txt_nom.set(listProduit[0])


    def choisirProduit(self, even=""):
        for produit in tabProduit :
            if produit.nom.lower() == self.nom.get().lower() :
                self.produit = produit
                break

        self.txt_prix.configure(state="normal", placeholder_text=self.produit.prix, placeholder_text_color="gray")
        self.txt_stock.configure(state="normal", placeholder_text=self.produit.stock, placeholder_text_color="gray")
        self.txt_image.configure(state="normal", placeholder_text=self.produit.image, placeholder_text_color="gray")

    def annuler(self):
        self.root.destroy()
        self.root.quit()
        app = Tk()
        Admin(app)
        app.mainloop()


    def valider(self):
        if self.nom.get() =="":
            messagebox.showerror("ERROR", "Veuillez  choisir un produit pour modification")
        elif self.txt_prix.get().strip() == "" and self.txt_stock.get().strip() == "" and self.txt_image.get().strip() == "":
            messagebox.showerror("ERROR", "Veuillez au moins modifier une caractéristique du produit !")
        else : 
            if  self.txt_prix.get().strip() != "":
                if self.txt_prix.get().strip().isdigit()==False:
                    messagebox.showerror("ERROR PRIX", "Un prix est composé de valeur entière !")
                elif int(self.txt_prix.get()) <100 :
                    messagebox.showerror("ERROR PRIX", "Le prix minimum d'un produit de la boutique est 100 !")
                else:
                    self.prix.set(int(self.txt_prix.get()))
                    self.produit.prix = self.prix.get()

            elif self.txt_stock.get().strip() != "":
                if self.txt_stock.get().strip().isdigit()==False:
                    messagebox.showerror("ERROR STOCK", "Le Stock est un nombre supérieur à zéro.")
                elif int(self.txt_stock.get().strip())>100:
                    messagebox.showerror("ERROR STOCK", "Ah Chef,Tu abuses ! Il s'agirait de doser !")
                else:
                    self.stock.set(int(self.txt_stock.get()))
                    self.produit.stock = self.stock.get()
            
            elif self.txt_image.get().strip() != "" :
                if '.' not in self.txt_image.get():
                    messagebox.showerror("ERROR IMAGE FORMAT", "Veuillez  saisir le format de l'image 'image.format'")
                else:
                    l = self.txt_image.get().split('.')
                    if l[1].lower() not in ['jpg', 'jpeg', 'png']:
                        messagebox.showerror("ERROR IMAGE FORMAT", "Veuillez  saisir un format correct d'image : JPG, PNG ou JPEG")
                    else :
                        self.nomImage.set(self.txt_image.get())
                        self.produit.image = self.nomImage.get()

            for i in range(len(tabProduit)) :
                if tabProduit[i].id == self.produit.id : 
                    tabProduit[i].prix = self.produit.prix               
                    tabProduit[i].stock = self.produit.stock               
                    tabProduit[i].image = self.produit.image               

            conn = sqlite3.connect(f"C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/{self.base}.db")
            c = conn.cursor() 
            c.execute(f"""
                UPDATE produit
                SET prix = {self.produit.prix}, stock = {self.produit.stock}, image = '{self.produit.image}'
                WHERE id == {self.produit.id}
            """)
            conn.commit()
            conn.close()

            messagebox.showinfo("SUCCESS", "Produit mis à jour avec succès !!!")
            self.annuler()
                


        



# root = Tk()
# GererProd(root)
# root.mainloop()