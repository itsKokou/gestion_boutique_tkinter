# # # import tkinter as tk
# # # import tkinter.ttk as ttk

# # # CHOIX = ["oui", "non", "peut-être"]
# # # VALEURS = ['Lundi', 'Mardi', 'Mercredi',
# # #            'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']


# # # class DemoWidget(tk.Frame):

# # #     def __init__(self, root):
# # #         super().__init__(root)
# # #         self._create_gui()
# # #         self.pack()


# # #     def _create_gui(self):
# # #         label = tk.Label(self, text="Un message")
# # #         label.grid(column=0, row=0)

# # #         text = tk.Entry(self)
# # #         text.grid(column=1, row=0, columnspan=2)

# # #         label = tk.Label(self, text="Un choix")
# # #         label.grid(column=0, row=1)

# # #         combo = ttk.Combobox(self, text="choix", values=VALEURS)
# # #         combo.grid(column=1, row=1, columnspan=2)

# # #         for i, rb_label in enumerate(CHOIX):
# # #             rb = ttk.Radiobutton(self, text=rb_label, value=i)
# # #             rb.grid(column=i, row=2)

# # #         checkButton = ttk.Checkbutton(self, text="Accepter les conditions")
# # #         checkButton.grid(column=0, row=3, columnspan=3)

# # #         button = tk.Button(self, text="Fermer", command=app.quit)
# # #         button.grid(column=1, row=4)


# # # app = tk.Tk()
# # # app.title("Demo Widgets")
# # # DemoWidget(app)

# # # app.mainloop()

# # # import tkinter  as tk 
# # # from tkcalendar import DateEntry
# # # my_w = tk.Tk()
# # # my_w.geometry("340x220")  

# # # cal=DateEntry(my_w,selectmode='day',date_pattern='MM-dd-yyyy')
# # # cal.grid(row=1,column=1,padx=15)
# # # my_w.mainloop()


# from tkinter import *
# from tkinter import ttk

# import sqlite3
# from tkinter import *
# from tkinter import messagebox,ttk
# from time import strftime
# from PIL import ImageTk, Image
# import customtkinter
# import tkinter.font as tkFont




# #==========================================================================================================

# class Categorie :
#     def __init__(self,id,libelle) :
#         self.id = id
#         self.libelle = libelle
    
# class SousCategorie:
#     def __init__(self, id, libelle, idCategorie) :
#         self.id = id
#         self.libelle = libelle
#         self.idCategorie = idCategorie

# class Produit:
#     def __init__(self,id, nom, prix, stock, idSousCategorie,image) -> None:
#         self.id = id
#         self.nom = nom
#         self.prix = prix
#         self.stock = stock
#         self.idSousCategorie = idSousCategorie
#         self.image = image

# class Vente :
#     def __init__(self,id,idClient,numFact,idBoutique):
#         self.id = id
#         self.idClient = idClient
#         self.numFacture = numFact
#         self.idBoutique = idBoutique

# #### Classe pour aider dans gestion de stock, faire migrer id et stock de produit vers paiement
# class Stock:
#     def __init__(self, id, stock):
#         self.id = id
#         self.stock = stock

# ## Classe pour aider dans la facture 

# class Facture:
#     def __init__(self, produit, qte, montant, tva) -> None:
#         self.produit = produit
#         self.qte = qte
#         self.montant = montant
#         self.tva = tva


# ### Tableau contenant les données Contient objet 
# tabCategorie = [] 
# tabSousCategorie = []
# tabProduit = []
# tabVentes = []
# ### et liste Objet contient les noms des objets
# # Nom des objets
# listCategorie = []
# listSousCategorie = []
# listProduit = []
# listShop = ["Mode","Bijouterie","Maison","Sport","Restaurant","Alimentation"]

# ## Récupération des données depuis la base de données
# conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/mode.db")
# c = conn.cursor()

# c.execute("Select * From produit")
# dataProduit = c.fetchall()  # Les produits sont stockées ici

# c.execute("Select * From categorie")
# dataCategorie = c.fetchall()

# c.execute("Select * From souscategorie")
# dataSousCategorie = c.fetchall()

# conn.close()

# #### Spécification de chaque donnée

# def specifierProduit(donnee:list):
#     for ligne in donnee:
#         id = int(ligne[0])
#         nom = str(ligne[1])
#         prix = int(ligne[2])
#         stock = int(ligne[3])
#         idSC = int(ligne[4])
#         image = str(ligne[5])
#         obj = Produit(id,nom,prix,stock,idSC,image) # Création de l'objet
#         tabProduit.append(obj) # Ajout de l'objet au tableau

# def specifierCategorie(donnee:list):
#     for ligne in donnee:
#         id = int(ligne[0])
#         libelle = str(ligne[1])
#         tabCategorie.append(Categorie(id,libelle))
#         listCategorie.append(libelle)

# def specifierSousCategorie(donnee:list):
#     for ligne in donnee:
#         id = int(ligne[0])
#         libelle = str(ligne[1])
#         idC = int(ligne[2])
#         tabSousCategorie.append(SousCategorie(id,libelle,idC))


# ## Récupération des ventes pour la recherche de facture
# conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/ventes.db")
# c = conn.cursor()
# c.execute("Select * From ventes")
# dataVentes = c.fetchall()  # Les ventes sont stockées ici
# conn.close()

# #### Spécification les données de la ventes
# def specifierVentes(donnee:list):
#     for ligne in donnee:
#         id = int(ligne[0])
#         idClient = int(ligne[1])
#         numFact = str(ligne[2])
#         idBoutique = int(ligne[3])
#         tabVentes.append(Vente(id,idClient,numFact,idBoutique))

# #####
# specifierProduit(dataProduit)
# specifierCategorie(dataCategorie)
# specifierSousCategorie(dataSousCategorie)






# class Okay:
#     def __init__(self,root) -> None:
#         self.root = root
#         self.root.geometry("900x700+320+60")
#         self.root.title("LES PRODUITS")
#         self.root.resizable(FALSE,FALSE)
#         self.root.config(bg="white")

#         MainFrame = Frame(self.root, background="cyan")
#         MainFrame.pack(fill=BOTH, expand=1)

#         MyCanva=Canvas(MainFrame, background="white")
#         MyCanva.pack(side=LEFT, fill=BOTH, expand=1)

#         scroll = ttk.Scrollbar(MainFrame, orient=VERTICAL,command=MyCanva.yview)
#         scroll.pack(side=RIGHT, fill=Y)

#         MyCanva.configure(yscrollcommand=scroll.set)
         
#         MyCanva.bind('<Configure>', lambda e: MyCanva.configure(scrollregion= MyCanva.bbox('all')))

#         self.secondFrame = Frame(MyCanva, background="white")

#         MyCanva.create_window((0,0), window= self.secondFrame, anchor='nw')

#         btn_mall = customtkinter.CTkButton(self.secondFrame, text="Admin",font=("Consolas",16,"bold") ,width=8,bg_color="white",fg_color='white',text_color="black",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
#         btn_mall.grid(row=0, column=0, pady=10)

#         self.lbl_titre = Label(self.secondFrame,text="LISTE DES PRODUITS", font=('algerian',22),bg="white", height=2)
#         self.lbl_titre.place(x=270, y=0)

#         # Souligner le texte 
#         f = tkFont.Font(self.lbl_titre, self.lbl_titre.cget("font"))
#         f.configure(underline = True)
#         self.lbl_titre.configure(font=f)

#         self.lbl_filtre = Label(self.secondFrame, text="Filtre : ", font=("regular",16,), bg="white")
#         self.lbl_filtre.grid(row=1, column=1, pady=10)

#         self.txt_filtre = ttk.Combobox(self.secondFrame, font=("times new roman",12,"bold"),values=listShop,width=13, state="readonly" )
#         self.txt_filtre.place(x=350, y=60)
#         self.txt_filtre.set("Mode")

#         self.lbl_id = ttk.Entry(self.secondFrame, width=10, font=("times new roman",17), foreground="brown",justify='center')
#         self.lbl_id.grid(row=2,column=0,sticky=W,padx=(90,0))
#         self.lbl_id.insert(END, "ID")
#         self.lbl_id.config(state="readonly")

#         self.lbl_nom = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17),foreground="brown", justify='center')
#         self.lbl_nom.grid(row=2,column=1,sticky=W)
#         self.lbl_nom.insert(END, "NOM")
#         self.lbl_nom.config(state="readonly")

#         self.lbl_id = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17), foreground="brown",justify='center')
#         self.lbl_id.grid(row=2,column=2,sticky=W,)
#         self.lbl_id.insert(END, "S-CATEGORIE")
#         self.lbl_id.config(state="readonly")

#         self.lbl_nom = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17),foreground="brown", justify='center')
#         self.lbl_nom.grid(row=2,column=3,sticky=W)
#         self.lbl_nom.insert(END, "CATEGORIE")
#         self.lbl_nom.config(state="readonly")

#         self.findCategorieByShop()


        
#     def findCategorieByShop(self):

#         for i in range(len(tabProduit)):

#             e = ttk.Entry(self.secondFrame, width=10, font=("times new roman",17), justify='center', background="white")
#             e.grid(row=i+4, column=0,sticky=W, padx=(90,0))
#             e.insert(END, tabProduit[i].id)
#             e.config(state="readonly")

#             e2 = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17), justify='center')
#             e2.grid(row=i+4, column=1,sticky=W)
#             e2.insert(END, tabProduit[i].nom)
#             e2.config(state="readonly")

#             scat = self.findSousCategorieById(tabProduit[i].idSousCategorie)
#             cat = self.findCategorieById(scat.idCategorie)

#             e2 = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17), justify='center')
#             e2.grid(row=i+4, column=2,sticky=W)
#             e2.insert(END, scat.libelle)
#             e2.config(state="readonly")

#             e2 = ttk.Entry(self.secondFrame, width=16, font=("times new roman",17), justify='center')
#             e2.grid(row=i+4, column=3,sticky=W)
#             e2.insert(END,cat.libelle )
#             e2.config(state="readonly")


#     def findSousCategorieById(self,id):
#         for i in tabSousCategorie :
#             if i.id == id :
#                 return i
            
#     def findCategorieById(self,id):
#         for i in tabCategorie :
#             if i.id == id :
#                 return i
    
        

# root = Tk()
# Okay(root)
# mainloop()


# # import sqlite3
# # from tkinter import *
# # from tkinter import messagebox,ttk
# # from time import strftime
# # from PIL import ImageTk, Image
# # import customtkinter
# # import tkinter.font as tkFont




# # #==========================================================================================================

# # class Categorie :
# #     def __init__(self,id,libelle) :
# #         self.id = id
# #         self.libelle = libelle
    
# # class SousCategorie:
# #     def __init__(self, id, libelle, idCategorie) :
# #         self.id = id
# #         self.libelle = libelle
# #         self.idCategorie = idCategorie

# # class Produit:
# #     def __init__(self,id, nom, prix, stock, idSousCategorie,image) -> None:
# #         self.id = id
# #         self.nom = nom
# #         self.prix = prix
# #         self.stock = stock
# #         self.idSousCategorie = idSousCategorie
# #         self.image = image

# # class Vente :
# #     def __init__(self,id,idClient,numFact,idBoutique):
# #         self.id = id
# #         self.idClient = idClient
# #         self.numFacture = numFact
# #         self.idBoutique = idBoutique

# # #### Classe pour aider dans gestion de stock, faire migrer id et stock de produit vers paiement
# # class Stock:
# #     def __init__(self, id, stock):
# #         self.id = id
# #         self.stock = stock

# # ## Classe pour aider dans la facture 

# # class Facture:
# #     def __init__(self, produit, qte, montant, tva) -> None:
# #         self.produit = produit
# #         self.qte = qte
# #         self.montant = montant
# #         self.tva = tva


# # ### Tableau contenant les données Contient objet 
# # tabCategorie = [] 
# # tabSousCategorie = []
# # tabProduit = []
# # tabVentes = []
# # ### et liste Objet contient les noms des objets
# # # Nom des objets
# # listCategorie = []
# # listSousCategorie = []
# # listProduit = []
# # listShop = ["Mode","Bijouterie","Maison","Sport","Restaurant","Alimentation"]

# # ## Récupération des données depuis la base de données
# # conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/mode.db")
# # c = conn.cursor()

# # c.execute("Select * From produit")
# # dataProduit = c.fetchall()  # Les produits sont stockées ici

# # c.execute("Select * From categorie")
# # dataCategorie = c.fetchall()

# # c.execute("Select * From souscategorie")
# # dataSousCategorie = c.fetchall()

# # conn.close()

# # #### Spécification de chaque donnée

# # def specifierProduit(donnee:list):
# #     for ligne in donnee:
# #         id = int(ligne[0])
# #         nom = str(ligne[1])
# #         prix = int(ligne[2])
# #         stock = int(ligne[3])
# #         idSC = int(ligne[4])
# #         image = str(ligne[5])
# #         obj = Produit(id,nom,prix,stock,idSC,image) # Création de l'objet
# #         tabProduit.append(obj) # Ajout de l'objet au tableau

# # def specifierCategorie(donnee:list):
# #     for ligne in donnee:
# #         id = int(ligne[0])
# #         libelle = str(ligne[1])
# #         tabCategorie.append(Categorie(id,libelle))
# #         listCategorie.append(libelle)

# # def specifierSousCategorie(donnee:list):
# #     for ligne in donnee:
# #         id = int(ligne[0])
# #         libelle = str(ligne[1])
# #         idC = int(ligne[2])
# #         tabSousCategorie.append(SousCategorie(id,libelle,idC))


# # ## Récupération des ventes pour la recherche de facture
# # conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/ventes.db")
# # c = conn.cursor()
# # c.execute("Select * From ventes")
# # dataVentes = c.fetchall()  # Les ventes sont stockées ici
# # conn.close()

# # #### Spécification les données de la ventes
# # def specifierVentes(donnee:list):
# #     for ligne in donnee:
# #         id = int(ligne[0])
# #         idClient = int(ligne[1])
# #         numFact = str(ligne[2])
# #         idBoutique = int(ligne[3])
# #         tabVentes.append(Vente(id,idClient,numFact,idBoutique))

# # #####
# # specifierProduit(dataProduit)
# # specifierCategorie(dataCategorie)
# # specifierSousCategorie(dataSousCategorie)



# # class ListerProd:
# #     def __init__(self,root) -> None:
# #         self.root = root
# #         self.root.geometry("900x700+320+30")
# #         self.root.title("LES PRODUITS")
# #         self.root.resizable(FALSE,FALSE)
# #         self.root.config(bg="white")

# #         self.TopFrame=LabelFrame(self.root,bg="white", background='white', height=100)
# #         self.TopFrame.pack(fill='both', expand="yes" ,padx=10,pady=10)
    
# #         self.MainFrame=LabelFrame(self.root,bg="white",background='white')

# #         self.MyCanva=Canvas(self.MainFrame,background='white')
# #         self.MyCanva.pack(side=LEFT, fill=BOTH)
        
# #         scroll = ttk.Scrollbar(self.MainFrame, orient=VERTICAL,command=self.MyCanva.yview)
# #         scroll.pack(side=RIGHT, fill="y")

# #         self.MyCanva.configure(yscrollcommand=scroll.set)

# #         self.MyCanva.bind('<Configure>', lambda e: self.MyCanva.configure(scrollregion= self.MyCanva.bbox('all')))

# #         self.myFrame = Frame(self.MyCanva,background='white')
# #         self.MyCanva.create_window((0,0),window=self.myFrame, anchor='nw')
# #         self.MainFrame.pack(fill="both", expand="yes" ,padx=10,pady=10)


# #         self.boutique = StringVar()

# #         btn_mall = customtkinter.CTkButton(self.TopFrame, text="Admin",font=("Consolas",16,"bold") ,width=8,bg_color="white",fg_color='white',text_color="black",hover_color='gray', cursor="hand2", border_color="black", border_width=1 )
# #         btn_mall.place(x=15,y=13)

# #         self.lbl_titre = Label(self.TopFrame,text="LISTE DES PRODUITS", font=('algerian',22),bg="white", height=2)
# #         self.lbl_titre.place(x=270, y=0)

# #         # Souligner le texte 
# #         f = tkFont.Font(self.lbl_titre, self.lbl_titre.cget("font"))
# #         f.configure(underline = True)
# #         self.lbl_titre.configure(font=f)

# #         self.lbl_filtre = Label(self.TopFrame, text="Filtre : ", font=("regular",16,), bg="white")
# #         self.lbl_filtre.place(x=100, y=70)

# #         self.txt_filtre = ttk.Combobox(self.TopFrame, font=("times new roman",12,"bold"),textvariable=self.boutique,values=listShop,width=13, state="readonly" )
# #         self.txt_filtre.place(x=180, y=70)
# #         self.txt_filtre.bind("<<ComboboxSelected>>", self.findProduitByShop)
# #         self.txt_filtre.set("Mode")



# #         self.lbl_id = ttk.Entry(self.TopFrame, width=10, font=("times new roman",17), foreground="brown",justify='center')
# #         self.lbl_id.grid(row=0,column=0,sticky=W,)
# #         self.lbl_id.insert(END, "ID")
# #         self.lbl_id.config(state="readonly")

# #         self.lbl_nom = ttk.Entry(self.TopFrame, width=16, font=("times new roman",17),foreground="brown", justify='center')
# #         self.lbl_nom.grid(row=0,column=1,sticky=W)
# #         self.lbl_nom.insert(END, "NOM")
# #         self.lbl_nom.config(state="readonly")

# #         self.lbl_id = ttk.Entry(self.TopFrame, width=16, font=("times new roman",17), foreground="brown",justify='center')
# #         self.lbl_id.grid(row=0,column=2,sticky=W,)
# #         self.lbl_id.insert(END, "S-CATEGORIE")
# #         self.lbl_id.config(state="readonly")

# #         self.lbl_nom = ttk.Entry(self.TopFrame, width=16, font=("times new roman",17),foreground="brown", justify='center')
# #         self.lbl_nom.grid(row=0,column=3,sticky=W)
# #         self.lbl_nom.insert(END, "CATEGORIE")
# #         self.lbl_nom.config(state="readonly")



# #     # def interAdmin(self):
# #     #     self.root.destroy()
# #     #     self.root.quit()
# #     #     app = Tk()
# #     #     Admin(app)
# #     #     app.mainloop()  


# #     def findProduitByShop(self,even= ""):
# #         if self.boutique.get() == "Mode":
# #             base= "mode"
# #         elif self.boutique.get() == "Bijouterie" :
# #             base= "bijouterie"
# #         elif self.boutique.get() == "Maison" :
# #             base= "maison"
# #         elif self.boutique.get() == "Sport" :
# #             base= "sport"
# #         elif self.boutique.get() == "Restaurant" :
# #             base= "restaurant"
# #         elif self.boutique.get() == "Alimentation" :
# #             base= "alimentation"

# #         conn = sqlite3.connect(f"C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/{base}.db")
# #         c = conn.cursor()
# #         c.execute("Select * From produit")
# #         dataProduit = c.fetchall()
# #         c.execute("Select * From categorie")
# #         dataCategorie = c.fetchall()
# #         c.execute("Select * From souscategorie")
# #         dataSousCategorie = c.fetchall()
# #         conn.close()
# #         # self.effacerTab()
# #         tabProduit.clear()
# #         specifierProduit(dataProduit)
# #         specifierCategorie(dataCategorie)
# #         specifierSousCategorie(dataSousCategorie)
# #         self.faireTabProduit() 


# #     def findSousCategorieById(self,id):
# #         for i in tabSousCategorie :
# #             if i.id == id :
# #                 return i
            
# #     def findCategorieById(self,id):
# #         for i in tabCategorie :
# #             if i.id == id :
# #                 return i

# #     def faireTabProduit(self):
# #         for i in range(len(tabProduit)):

# #             e= ttk.Label(self.myFrame,text=tabProduit[i].id ,width=10, font=("times new roman",17), justify='center', background="white")
# #             e.grid(row=i+1, column=0,sticky=W)

# #             e2 = ttk.Label(self.myFrame,text=tabProduit[i].nom ,width=16, font=("times new roman",17), justify='center')
# #             e2.grid(row=i+1, column=1,sticky=W)

# #             scat = self.findSousCategorieById(tabProduit[i].idSousCategorie)
# #             cat = self.findCategorieById(scat.idCategorie)

# #             e2 = ttk.Label(self.myFrame,text=scat.libelle ,width=16, font=("times new roman",17), justify='center')
# #             e2.grid(row=i+1, column=2,sticky=W)
        

# #             e2 = ttk.Label(self.myFrame, text=cat.libelle,width=16, font=("times new roman",17), justify='center')
# #             e2.grid(row=i+1, column=3,sticky=W)



# # root = Tk()
# # ListerProd(root)
# # root.mainloop()

