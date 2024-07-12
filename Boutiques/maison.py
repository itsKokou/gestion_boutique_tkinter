import sqlite3
from tkinter import *
from tkinter import messagebox,ttk
from time import strftime
from PIL import ImageTk, Image #Gerer des images pour qu'elles s'affichent
from Boutiques.classModel import *





#==========================================================================================================



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

## Récupération des données depuis la base de données
conn = sqlite3.connect("C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/maison.db")
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
specifierVentes(dataVentes)


#===================================================================================================================================

class Maison:
    id = 3
    taxe =0
    net = 0
    brut = 0
    paiement = False
    tabStock = []
    tabFacture = []
    livraison = False
    adresse = ""
    numero = ""

    def __init__(self,root) -> None:
        self.root = root
        self.root.title("Articles de Maison")
        self.root.geometry("1520x780+0+0") #Taille de l'interface 
        self.root.resizable(FALSE,FALSE)
        self.root.config(bg="white")

        ### Variables à utiliser dans le programme 
        self.produitId = IntVar()
        self.categorie = StringVar()
        self.souscategorie = StringVar()
        self.produit = StringVar()
        self.prix = IntVar()
        self.stock = IntVar()
        self.qte = IntVar()
        self.taxe = DoubleVar()
        self.totalbrut = IntVar()
        self.totalnet = DoubleVar()
        self.factSaisie = StringVar()
        self.clickSurGenerer = False
        self.livrer = IntVar()
        self.livrer.set(0)

        self.title = Label(self.root, text="ARTICLES DE MAISON", font=("Algerian",32), bg="#00d1ff", fg="black")
        self.title.pack(side=TOP, fill=X) # fill=X ==> Pour remplir l'axe des abscisses

        
        self.lbl_heure = Label(self.root, font=("times new roman",14),bg="#00d1ff",fg="black")
        self.lbl_heure.place(x=0,y=25,width=120, height=20)
        

        lbl_date = Label(self.root,text=strftime("%d/%m/%Y") ,font=("times new roman",14),bg="#00d1ff",fg="black")
        lbl_date.place(x=1380,y=25,width=120, height=20)

        Main_Frame = Frame(self.root,bd=2, relief=GROOVE, bg="white")
        Main_Frame.place(x=0,y=54, width=1521,height=750)

        ##### Sections Produit et choix
        Produit_Frame = LabelFrame(Main_Frame,text="Produit",font=("times new roman", 17), bg="white" )
        Produit_Frame.place(x=10,y=5,width=480,height=170)

        lbl_categorie = Label(Produit_Frame, text="Catégorie :",font=("times new roman",15,"bold"), bg="white")
        lbl_categorie.grid(row=0,column=0, sticky=W,padx=5, pady=2)

        txt_categorie = ttk.Combobox(Produit_Frame, font=("times new roman",12,"bold"),textvariable=self.categorie,values=listCategorie ,width=12, state="readonly" )
        txt_categorie.grid(row=0,column=1, sticky=W,padx=5, pady=2)
        txt_categorie.set("Selectionner")
        txt_categorie.bind("<<ComboboxSelected>>", self.chargerSousCategorie)

        lbl_souscategorie = Label(Produit_Frame, text="Sous-Catégorie :",font=("times new roman",15,"bold"), bg="white")
        lbl_souscategorie.grid(row=1,column=0, sticky=W,padx=5, pady=2)

        self.txt_souscategorie = ttk.Combobox(Produit_Frame, font=("times new roman",12,"bold"),textvariable=self.souscategorie ,width=12, state="readonly" )
        self.txt_souscategorie.grid(row=1,column=1, sticky=W,padx=5, pady=2)
        self.txt_souscategorie.bind("<<ComboboxSelected>>", self.chargerProduit)

        lbl_nomProduit = Label(Produit_Frame, text="Produit :",font=("times new roman",15,"bold"), bg="white")
        lbl_nomProduit.grid(row=2,column=0, sticky=W,padx=5, pady=2)

        self.txt_nomProduit = ttk.Combobox(Produit_Frame, font=("times new roman",12,"bold"),textvariable=self.produit ,width=12, state="readonly" )
        self.txt_nomProduit.grid(row=2,column=1, sticky=W,padx=5, pady=2)
        self.txt_nomProduit.bind("<<ComboboxSelected>>", self.chargerPrix)

        lbl_livraison = Label(Produit_Frame,text="Livraison :",font=("times new roman",15,"bold"), bg="white")
        lbl_livraison.grid(row=3, column=0, sticky=W,padx=5, pady=2)

        self.txt_livraison= Checkbutton(Produit_Frame,text="", font=("times new roman",15),bg="white", variable= self.livrer, command=self.changerEtatLivraison)
        self.txt_livraison.grid(row=3, column=1, sticky=W,padx=5, pady=2)

        lbl_prix = Label(Produit_Frame, text="Prix :",font=("times new roman",15,"bold"), bg="white")
        lbl_prix.grid(row=0,column=2, sticky=W,padx=5, pady=2)

        txt_prix = ttk.Entry(Produit_Frame, font=("times new roman",10),textvariable=self.prix, width=12, state="readonly")
        txt_prix.grid(row=0,column=3, sticky=W,padx=5, pady=2)

        lbl_quantite = Label(Produit_Frame, text="Quantité :",font=("times new roman",15,"bold"), bg="white")
        lbl_quantite.grid(row=1,column=2, sticky=W,padx=5, pady=2)

        self.txt_quantite = ttk.Entry(Produit_Frame, font=("times new roman",10),textvariable=self.qte, width=12)
        self.txt_quantite.grid(row=1,column=3, sticky=W,padx=5, pady=2)
    

        self.Produit_Image_Frame = Frame(Main_Frame, bg="white" )
        self.Produit_Image_Frame.place(x=520,y=15,width=350,height=160)

        self.produit_image = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/blanc.png"))
        self.lbl_produit_image = Label(self.Produit_Image_Frame, image=self.produit_image, height=150, width=330, bg="white") # Conteneur de l'image
        self.lbl_produit_image.place(x=0,y=0)

        ##### Image de la Boutique
        self.vue_image = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/maisons.jpg"))
        self.lbl_image = Label(image=self.vue_image,width=860 ,height=380, bg="white") # Conteneur de l'image
        self.lbl_image.place(x=15,y=242)
        
        #### Aperçu Facture 
        lbl_facture = LabelFrame(Main_Frame,text="Facture", font=("times new roman",15,"bold"),bg="white")
        lbl_facture.place(x=900, y=74, width=600, height=500)

        scroll_y = Scrollbar(lbl_facture, orient=VERTICAL) # Side bar au cas où la facture est longue
        scroll_y.pack(side=RIGHT, fill=Y) # prend l'axe des Y : emplacement

        self.textarea = Text(lbl_facture, font=("times new roman",13,"bold"), bg="white", fg="blue", yscrollcommand= scroll_y.set)
        scroll_y.config(command=self.textarea.yview) # le rendre visible
        self.textarea.pack(fill=BOTH, expand=1)
        
        #### Footer : Total 
        footer_Frame = LabelFrame(Main_Frame, text="Bouton", font=("times new roman", 15), bg="white")
        footer_Frame.place(x=10, y=574, width=1493, height=146) 

        lbl_totalbrut = Label(footer_Frame,text="Total Brut :", font=("times new roman",18,"bold"), bg="white")
        lbl_totalbrut.grid(row=0,column=0, sticky=W, padx=5, pady=2)

        txt_totalbrut = ttk.Entry(footer_Frame,textvariable=self.totalbrut ,font=("times new roman",18), width=15, state="readonly")
        txt_totalbrut.grid(row=0,column=1,sticky=W, padx=5, pady=2)

        lbl_taxe = Label(footer_Frame,text="Taxe :", font=("times new roman",18,"bold"), bg="white")
        lbl_taxe.grid(row=1,column=0, sticky=W, padx=5, pady=2)

        txt_taxe = ttk.Entry(footer_Frame,textvariable=self.taxe ,font=("times new roman",18), width=15, state="readonly")
        txt_taxe.grid(row=1,column=1,sticky=W, padx=5, pady=2)

        lbl_totalnet = Label(footer_Frame,text="Total Net :", font=("times new roman",18,"bold"), bg="white")
        lbl_totalnet.grid(row=2,column=0, sticky=W, padx=5, pady=2)

        txt_totalnet = ttk.Entry(footer_Frame,textvariable=self.totalnet ,font=("times new roman",18), width=15, state="readonly")
        txt_totalnet.grid(row=2,column=1,sticky=W, padx=5, pady=2)

        ######## Boutons
        Btn_Frame = Frame(footer_Frame, bg="white")
        Btn_Frame.place(x=370, y=15)

        ajoutPanier = Button(Btn_Frame, text="Ajouter Au\nPanier",width=10 ,height=2,command=self.ajouterPanier ,font=("times new roman",18,"bold"), bg="green",cursor="hand2")
        ajoutPanier.grid(row=0, column=0, sticky=W, padx=15, pady=2)

        generer = Button(Btn_Frame, text="Générer\n Facture", width=10, height=2,command=self.genererFacture ,font=("times new roman",18,"bold"), bg="cyan",cursor="hand2")
        generer.grid(row=0, column=1,sticky=W, padx=15, pady=2)

        valide = Button(Btn_Frame, text="Valider\n Panier", width=10, height=2,command=self.ValiderPanier ,font=("times new roman",18,"bold"), bg="yellow",cursor="hand2")
        valide.grid(row=0, column=3,sticky=W, padx=15, pady=2)

        reini = Button(Btn_Frame, text="Réinitialiser",width=10, height=2,command=self.reinitialiser ,font=("times new roman",18,"bold"), bg="#ff7a00",cursor="hand2")
        reini.grid(row=0, column=4,sticky=W, padx=15, pady=2)

        retour = Button(Btn_Frame, text="Retour",width=10 ,height=2, command=self.retourner, font=("times new roman",18,"bold"), bg="gray",cursor="hand2")
        retour.grid(row=0, column=5,sticky=W, padx=15, pady=2)

        quitte = Button(Btn_Frame, text="Quitter",width=10 ,height=2, command=self.quitter, font=("times new roman",18,"bold"), bg="red",cursor="hand2")
        quitte.grid(row=0, column=6,sticky=W, padx=15, pady=2)

        #### Recherche 
        self.champRechercheFacture(Main_Frame)
        


        self.bienvenue()
        self.heure()
        self.listMontant = []
        


    def heure(self):
        h = strftime("%H:%M:%S") # récuperer l'heure
        self.lbl_heure.config(text=h) # met l'heure dans le label 
        self.lbl_heure.after(1000,self.heure) # chaque 1000 milliseconde, la fonction se relance

    #---------------------LES FONCTIONS-----------------------------------------------

    def findSousCategorieByIdCategorie(self,id):
        for i in tabSousCategorie:
            if i.idCategorie == id :
                listSousCategorie.append(i.libelle)

    def findProduitByIdSC(self,id):
        for i in tabProduit:
            if i.idSousCategorie == id :
                listProduit.append(i.nom)

    def findCategorieId(self,libelle):
        for i in tabCategorie:
            if i.libelle == libelle :
                return i.id 
    
    def findSousCategorieId(self,libelle):
        for i in tabSousCategorie:
            if i.libelle == libelle :
                return i.id 
    
    def findProduit(self,nom):
        for i in tabProduit :
            if i.nom == nom :
                return i
    
   
    

    # Fonctions qui gère les champs select (combobox)

    def chargerSousCategorie(self, even=""):
        listSousCategorie.clear()
        id = self.findCategorieId(self.categorie.get())
        self.findSousCategorieByIdCategorie(id)
        self.txt_souscategorie.config(values=listSousCategorie)
        self.txt_souscategorie.current(0)
        listProduit.clear()
        self.txt_nomProduit.config(values=listProduit)
        self.txt_nomProduit.set("")
        self.prix.set(0)
        self.qte.set(0)
        blanc = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/blanc.png"))
        self.lbl_produit_image.config(image=blanc)
        self.lbl_image.config(image=self.vue_image)


    def chargerProduit(self, even=""):
        listProduit.clear()
        id = self.findSousCategorieId(self.souscategorie.get())
        self.findProduitByIdSC(id)
        self.txt_nomProduit.config(values=listProduit)
        self.txt_nomProduit.current(0)
        self.prix.set(0)
        self.qte.set(0)
        blanc = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/blanc.png"))
        self.lbl_produit_image.config(image=blanc)
        self.lbl_image.config(image=self.vue_image)

    def chargerPrix(self, even=""):
        prod = Produit(1,"",0,0,0,"")
        prod = self.findProduit(self.produit.get())
        self.prix.set(prod.prix)
        self.qte.set(1)
        self.stock.set(prod.stock)
        self.produitId.set(prod.id)

        import os 
        if os.path.isfile(f"C:/Users/winny/Desktop/Projet Python POO/images/maison/{prod.image}") :
            self.produit_image = ImageTk.PhotoImage(Image.open(f"C:/Users/winny/Desktop/Projet Python POO/images/maison/{prod.image}"))
            self.lbl_produit_image.config(image=self.vue_image)
            self.lbl_image.config(image=self.produit_image)
        else :
            messagebox.showinfo("ERROR IMAGE", "L'image du produit est indisponible pour le moment")
        

    # ---------------- Fonctions pour les boutons-------------- 

    def retourner(self):
        from Boutiques.mall import Mall
        self.root.destroy()
        self.root.quit()
        Maison.tabStock.clear()
        Maison.tabFacture.clear()
        Maison.paiement = False
        Maison.adresse = ""
        Maison.numero = ""
        Maison.livraison = False
        self.clickSurGenerer = False
        self.listMontant.clear()
        root = Tk()
        Mall(root)
        root.mainloop()
        

    def quitter(self):
        op = messagebox.askyesno("Quitter", "Vous partez déjà ? ")
        if op == True:
            messagebox.showinfo("Bye", "Au revoir !")
            self.lbl_heure.after_cancel(self.lbl_heure)
            self.root.destroy()
            self.root.quit()
            Maison.tabStock.clear()
            Maison.paiement = False
            Maison.tabFacture.clear()
            Maison.adresse = ""
            Maison.numero = ""
            Maison.livraison = False


   
    def bienvenue(self):
        self.textarea.delete(1.0, END) # Pour supprimer le contenu
        self.textarea.insert(END, "\n\t\t     ** Bienvenue Dans La MAISON **")
        self.textarea.insert(END, "\n\t\t\t  ------------------------")
        self.textarea.insert(END, "\n\n\t\t                Aperçu de Votre Facture")
        self.textarea.insert(END, "\n\n***************************************************************")
        self.textarea.insert(END, "\nProduits\t\tQuantité\t\tMontant\t\tTVA")
        self.textarea.insert(END, "\n***************************************************************")
        



        
    def ajouterPanier(self):
        if self.produit.get() =="" :
            messagebox.showerror("Error", "Veuillez choisir au moins un produit !!!") 
        elif self.txt_quantite.get().isdigit() == False :
            messagebox.showerror("Error", "Veuillez saisir un entier comme quantité !!! ") 
        elif self.qte.get() == 0 :
            messagebox.showerror("Quantité Incorrecte", "Veuillez choisir une quantité supérieure à 0 ! ") 
        elif self.qte.get() >= self.stock.get() :
            messagebox.showerror("Rupture de Stock", "Veuillez choisir une quantité inférieure ! ") 
        else :
            montant = self.qte.get()*self.prix.get()
            self.listMontant.append(montant)
            self.totalbrut.set(sum(self.listMontant))
            self.taxe.set(self.totalbrut.get()*0.18)
            self.totalnet.set(self.totalbrut.get()+self.taxe.get())
            self.textarea.insert(END, f"\n{self.produit.get()}\t\t{self.qte.get()}\t\t{montant}\t\t{montant*0.18}")

            Maison.brut = self.totalbrut.get()
            Maison.taxe = self.taxe.get()
            Maison.net = self.totalnet.get()

            #Enregistrer les achats pour la facture
            fact = Facture(self.produit.get(),self.qte.get(),montant,montant*0.18)
            Maison.tabFacture.append(fact)

            # Gère le stock ici mais pas encore dans la base de données
            newStock = self.stock.get()-self.qte.get()
            objStock = Stock(self.produitId.get(),newStock)
            Maison.tabStock.append(objStock)

            listProduit.clear()
            self.txt_nomProduit.config(values=listProduit)
            self.txt_nomProduit.set("")
            self.prix.set(0)
            self.qte.set(0)
            blanc = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/blanc.png"))
            self.lbl_produit_image.config(image=blanc)
            self.lbl_image.config(image=self.vue_image) 

           




    def  genererFacture(self):
        if self.clickSurGenerer == False :
            if self.totalbrut.get() == 0 :
                messagebox.showerror("Error", "Veuillez choisir au moins un produit !!!") 
            else :
                s = 0
                if Maison.livraison == True:
                    self.textarea.insert(END, "\n***************************************************************")
                    self.textarea.insert(END, f"\Livraison : \t\t\t\t\t\t{2500.0}")
                    s= 2500
                self.textarea.insert(END, "\n***************************************************************")
                self.textarea.insert(END, f"\nTotal Brut : \t\t\t\t\t\t{self.totalbrut.get()+s}")
                self.textarea.insert(END, f"\nTaxe : \t\t\t\t\t\t{self.taxe.get()}")
                self.textarea.insert(END, f"\nTotal Net : \t\t\t\t\t\t{self.totalnet.get()+s}")
                self.textarea.insert(END, "\n***************************************************************")
                self.clickSurGenerer = True
        else : 
            messagebox.showinfo("Facture", "Votre facture a déjà été générée !!!") 

    def reinitialiser(self):
        if self.souscategorie.get() =="" :
            messagebox.showinfo("Infos", "Chef, tu n'as encore rien fait !!!") 
        else:
            op = messagebox.askyesno("Attention", "Confirmer la réinitilisation ?")
            if op == True :
                self.textarea.delete(1.0,END)
                self.bienvenue()
                self.produit.set("")
                self.categorie.set("Selectionner")
                self.souscategorie.set("")
                self.prix.set("")
                self.produitId.set(0)
                self.qte.set(0)
                self.stock.set(0)
                self.totalbrut.set(0)
                self.totalnet.set(0)
                self.taxe.set(0)
                listSousCategorie.clear()
                self.txt_souscategorie.config(values=listSousCategorie)
                blanc = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/blanc.png"))
                self.lbl_produit_image.config(image=blanc)
                self.lbl_image.config(image=self.vue_image)  
                # Vider le tableau de produit dont on devait gérer le stock
                Maison.tabStock.clear()
                Maison.paiement = False
                Maison.tabFacture.clear()
                Maison.adresse = ""
                Maison.numero = ""
                Maison.livraison = False
                self.clickSurGenerer = False
                self.listMontant.clear()

    
    def ValiderPanier(self):
        if self.totalbrut.get() == 0 :
            messagebox.showerror("Error", "Veuillez choisir au moins un produit !!!") 
        else :
            self.root.destroy()
            self.root.quit()
            if(Maison.livraison == False):
                pass
            else:
                from Boutiques.livraison import Livraison
                app = Tk()
                obj = Livraison(app)
                app.mainloop()

            Maison.paiement = True # Il entame le paiement
            from Boutiques.mall import Mall
            Mall.testProduit = True  # ici il y a au moins un achat en cours 
            if Mall.testConn == False:
                from Boutiques.formConnexion import Form
                app = Tk()
                ob = Form(app)
                #L'image ne vient pas donc on la remet ici 
                imageMall = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/malls.jpg"))
                ob.lbl_image.config(image=imageMall)
                #app.after_cancel(app)
                app.mainloop()
            else : 
                from Boutiques.formPaiement import Paiement 
                app = Tk()
                ob = Paiement(app)
                app.mainloop()

    @classmethod
    def Facture(clss):
        from Boutiques.mall import Mall
        d = strftime("%d%m%Y") 
        h = strftime("%H%M%S")
        num = d+h 
        nomFichier =f"FACT{num}.txt"

        from Boutiques.mall import Mall 
        Mall.nomFact = nomFichier
        with open(f"C:/Users/winny/Desktop/Projet Python POO/Factures/{nomFichier}","w",encoding='UTF-8') as f:
            f.write("--------------------------------------------------------------------------------")
            f.write("\n********************************************************************************")
            f.write("\n*******************************  .WINZIZ'S MALL.  ******************************")
            f.write("\n****************************  ZIMO SUR PLANETE MARS  ***************************")
            f.write("\n*****************************  (+221) 77 182 54 14  ****************************")
            f.write("\n*****************************  wz-mall@contact.com  ****************************")
            f.write("\n**********************************  LA MAISON  *********************************")
            f.write("\n********************************************************************************")
            f.write("\n--------------------------------------------------------------------------------")
            f.write(f"""\n{f'{strftime("%d/%m/%Y")} à {strftime("%Hh %Mmin %Ss")}':^80}""")
            f.write("\nInformation du CLIENT-----------------------------------------------------------")
            f.write(f"\nLogin  :  {Mall.user.login}")
            f.write(f"\nPrénom :  {Mall.user.prenom}")
            f.write(f"\nNom    :  {Mall.user.nom}")
            f.write("\n--------------------------------------------------------------------------------")
            f.write(f"\nFacture N : FACT{num}")
            f.write("\n--------------------------------------------------------------------------------")
            f.write("\n********************************************************************************")
            f.write(f"""\n{"PRODUIT":<20}{"QUANTITÉ":<20}{"MONTANT":<20}{"TVA":<20}""")
            f.write("\n********************************************************************************")
            f.write("\n--------------------------------------------------------------------------------")
            ### Boucle produit
            for i in Maison.tabFacture :
                f.write(f"""\n{i.produit:<20}{i.qte:<20}{i.montant:<20}{i.tva:<20}""")
                f.write("\n--------------------------------------------------------------------------------")
            if Maison.livraison == True:
                f.write("\n********************************************************************************")
                f.write(f"""\n{"Livraison : ":<20}{2500.0:>40}""")
                f.write(f"""\n{"Adresse : ":<20}{Maison.adresse:>40}""")
                f.write(f"""\n{"Numéro du destinataire : ":<30}{Maison.numero:>30}""")
            f.write("\n********************************************************************************")
            f.write(f"""\n{"TOTAL BRUT : ":<60}{Maison.brut+2500}""")
            f.write(f"""\n{"TAXE : ":<60}{Maison.taxe}""")
            f.write(f"""\n{"TOTAL NET : ":<60}{Maison.net+2500}""")
            f.write("\n*****************************  MERCI ET À BIENTÔT ******************************")

        #### Insertion dans la base de données Ventes 
        vente = Vente(len(tabVentes),Mall.user.id,f"FACT{num}",Maison.id)
        tabVentes.append(vente)
        conn = sqlite3.connect(f"C:/Users/winny/Desktop/Projet Python POO/BasesDeDonnes/ventes.db")
        c = conn.cursor()
       
        param = {"i": Mall.user.id, "l":f"FACT{num}", "m":Maison.id}
        c.execute("""
            INSERT INTO ventes(idClient,numFacture,idBoutique)
            VALUES(:i,:l,:m)
        """, param)
        conn.commit()
        conn.close()


    def champRechercheFacture(self,Un_Frame):
        from Boutiques.mall import Mall
        if Mall.testConn == True :
            rech_Frame = Frame(Un_Frame,bd=2, bg="white")
            rech_Frame.place(x=900,y=10, width=560, height=70)

            self.lbl_recherche = Label(rech_Frame,text="N° Facture :", font=("times new roman",20,"bold"),bg="white")
            self.lbl_recherche.grid(row=0, column=0, sticky=W, padx=5, pady=2)

            self.txt_recherche = ttk.Entry(rech_Frame, textvariable=self.factSaisie, font=("times new roman",20), width=15)
            self.txt_recherche.grid(row=0, column=1, sticky=W, padx=5, pady=2)

            self.btn_recherche = Button(rech_Frame, text="Rechercher",command=self.rechercherFacturePourAfficher, font=("times new roman",12,"bold"), height=2,width=11, bg="yellow", cursor="hand2")
            self.btn_recherche.grid(row=0, column=2, sticky=W, padx=5, pady=2)


    def rechercheVente(self):
        from Boutiques.mall import Mall
        for v in tabVentes :
            if ( Mall.user.id==v.idClient and self.factSaisie.get().upper()==v.numFacture and v.idBoutique == Maison.id ) :
                return True
    
        return False



    def rechercherFacturePourAfficher(self):
        if self.rechercheVente()==False :
            messagebox.showinfo("Facture", f"Chef, Vous n'avez pas de facture avec ce numéro {self.factSaisie.get().upper()} !")
        else:
    
            root = Tk()
            root.geometry("750x550+320+100")
            root.title("VOTRE FACTURE")
            root.resizable(FALSE,FALSE)

            scroll_y = Scrollbar(root, orient=VERTICAL) # Side bar au cas où la facture est longue
            scroll_y.pack(side=RIGHT, fill=Y) # prend l'axe des Y : emplacement
            area = Text(root ,font=("Consolas",13,"bold"), bg="white", fg="blue", yscrollcommand= scroll_y.set)
            scroll_y.config(command=area.yview) # le rendre visible
            area.pack(fill=BOTH, expand=1)

            with open(f"C:/Users/winny/Desktop/Projet Python POO/Factures/{self.factSaisie.get().upper()}.txt","r",encoding='utf-8') as f:
                data = f.read()
                area.delete(1.0,END)
                area.insert(END,data)
                self.factSaisie.set("")
            root.mainloop()

    def changerEtatLivraison(self):
        if (self.livrer.get()==0):
            Maison.livraison = False
        elif (self.livrer.get()==1):
            Maison.livraison = True

            
            
        
    
                





    


        

#=====================Sortie

# root = Tk()
# obj = Maison(root)
# root.mainloop()





