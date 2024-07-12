from tkinter import *
from tkinter import messagebox,ttk
import tempfile   # pour imprimer facture
import random
from time import strftime
from PIL import ImageTk, Image #Gerer des images pour qu'elles s'affichent
import os # pour l'impression

class SuperMarket():
    def __init__(self,root):
        self.root = root
        self.root.title("Super Market")
        self.root.geometry("1520x780+0+0")

        title = Label(self.root, text="KOKOU'S SUPER MARKET ",font=("Algerian",32), bg="#00d1ff", fg="black")
        title.pack(side=TOP, fill=X)

        def heure():
            h = strftime("%H:%M:%S")
            lbl_heure.config(text=h)
            lbl_heure.after(1000,heure) # pour qu'il affiche continuellement l'heure 

        lbl_heure = Label(self.root, text="HH:MM:SS", font=("times new roman",14),bg="#00d1ff",fg="black")
        lbl_heure.place(x=0,y=25,width=120, height=20)

        heure()
        # Variables qu'on va utiliser
        self.client_nom = StringVar()
        self.client_prenom = StringVar()
        self.client_tel = StringVar()
        self.client_mail = StringVar()

        self.num_facture = StringVar() # random
        z = random.randint(500,9999)
        self.num_facture.set(z)

        # recherche d'element 
        self.rech_facture = StringVar()
        self.produit = StringVar()
        self.prix = DoubleVar()
        self.qte = IntVar()
        self.totalbrut = StringVar()
        self.taxe = StringVar()
        self.totalnet = StringVar()

        # Liste catégorie 

        self.list_categorie = ["selectionner","Vêtement", "Montre", "Téléphone"]

        # Sous catégorie vetement
        self.list_souscategorieVetement = ["Pantalon","T-Shirt", "Jogging"]

        self.pantalon = ["Levis", "Dior", "Gucci"]
        self.price_levis = 5000
        self.price_dior = 4000
        self.price_gucci = 8000

        self.tshirt = ["Polo", "Roadster", "Nike"]
        self.price_polo = 2000
        self.price_roadster = 1500
        self.price_nike = 4000

        self.jogging = ["Adidas", "Puma", "Balmain"]
        self.price_adidas = 6000
        self.price_puma = 12000
        self.price_balmain = 8000

        #Sous catégorie Montre
        self.list_souscategorieMontre = ["Rolex","Casio", "Mont Blanc"]

        self.rolex = ["Air-King", "DateJust", "GMT-MASTER II"]
        self.price_airking = 50000
        self.price_datejust = 40000
        self.price_gmtmaster = 80000

        self.casio = ["BABY-G", "Edifice", "Sheen"]
        self.price_babyg = 20000
        self.price_edifice = 15000
        self.price_sheen = 40000

        self.montblanc = ["Boheme", "Heritage", "TimeWalker"]
        self.price_boheme = 60000
        self.price_heritage = 120000
        self.price_timewalker = 230000

        #Sous catégorie Téléphone
        self.list_souscategorieTelephone = ["Tecno","Iphone", "Samsung"]

        self.tecno = ["Camon", "Spark", "Phantom"]
        self.price_camon = 90000
        self.price_spark = 64000
        self.price_phantom = 180000

        self.iphone = ["Iphone 12", "Iphone 13", "Iphone 14"]
        self.price_iphone12 = 280000
        self.price_iphone13 = 350000
        self.price_iphone14 = 600000

        self.samsung = ["Galaxy", "Note", "Ultra"]
        self.price_galaxy = 60000
        self.price_note = 120000
        self.price_ultra = 230000

        

        Main_Frame = Frame(self.root,bd=2, relief=GROOVE, bg="white")
        Main_Frame.place(x=0,y=54, width=1521,height=750)

        # Definition du client
        client_Frame = LabelFrame(Main_Frame,text="Client", font=("times new roman",15), bg="white")
        client_Frame.place(x=10,y=5,width=350,height=170)

        self.lbl_nomClient = Label(client_Frame,text="Nom :", font=("times new roman",15, "bold"), bg="white")
        self.lbl_nomClient.grid(row=0, column=0, sticky=W, padx=5,pady=2)

        self.txt_nomClient = ttk.Entry(client_Frame,textvariable=self.client_nom , font=("times new roman",15))
        self.txt_nomClient.grid(row=0,column=1, sticky=W, padx=5,pady=2)

        self.lbl_prenomClient = Label(client_Frame,text="Prénom :", font=("times new roman",15, "bold"), bg="white")
        self.lbl_prenomClient.grid(row=1, column=0, sticky=W, padx=5,pady=2)

        self.txt_prenomClient = ttk.Entry(client_Frame,textvariable=self.client_prenom , font=("times new roman",15))
        self.txt_prenomClient.grid(row=1,column=1, sticky=W, padx=5,pady=2)

        self.lbl_contact = Label(client_Frame,text="Contact :", font=("times new roman",15, "bold"), bg="white")
        self.lbl_contact.grid(row=2, column=0, sticky=W, padx=5,pady=2)

        self.txt_contact = ttk.Entry(client_Frame, textvariable=self.client_tel , font=("times new roman",15))
        self.txt_contact.grid(row=2,column=1, sticky=W, padx=5,pady=2)

        self.lbl_emailClient = Label(client_Frame,text="Email :", font=("times new roman",15, "bold"), bg="white")
        self.lbl_emailClient.grid(row=3, column=0, sticky=W, padx=5,pady=2)

        self.txt_emailClient = ttk.Entry(client_Frame, textvariable=self.client_mail , font=("times new roman",15))
        self.txt_emailClient.grid(row=3,column=1, sticky=W, padx=5,pady=2)

        # Produits 

        produit_Frame = LabelFrame(Main_Frame, text="Produit",font=("times new roman",15), bg="white")
        produit_Frame.place(x=400,y=5,width=480,height=170)

        self.lbl_categorie = Label(produit_Frame, text="Catégorie :",font=("times new roman",15,'bold'), bg="white" )
        self.lbl_categorie.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_categorie = ttk.Combobox(produit_Frame,font=("times new roman",10),values=self.list_categorie,width=12, state="readonly")
        self.txt_categorie.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.txt_categorie.current(0) # se met sur le premier element par defaut
        self.txt_categorie.bind("<<ComboboxSelected>>", self.fonctionCategorie)

        self.lbl_souscategorie = Label(produit_Frame, text="Sous-Catégorie :",font=("times new roman",15,'bold'), bg="white" )
        self.lbl_souscategorie.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_souscategorie = ttk.Combobox(produit_Frame,font=("times new roman",10),values=[] ,width=12, state="readonly")
        self.txt_souscategorie.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.txt_souscategorie.bind("<<ComboboxSelected>>", self.fonctionSousCategorie)

        self.lbl_nomProduit = Label(produit_Frame, text="Nom Produit :",font=("times new roman",15,'bold'), bg="white" )
        self.lbl_nomProduit.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_nomProduit = ttk.Combobox(produit_Frame,font=("times new roman",10),textvariable=self.produit ,width=12, state="readonly")
        self.txt_nomProduit.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.txt_nomProduit.bind("<<ComboboxSelected>>", self.fonctionNomProduit)

        self.lbl_prix = Label(produit_Frame, text="Prix :",font=("times new roman",15,'bold'), bg="white" )
        self.lbl_prix.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.txt_prix = ttk.Entry(produit_Frame,font=("times new roman",10),textvariable=self.prix ,width=12, state="readonly")
        self.txt_prix.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        self.lbl_qte = Label(produit_Frame, text="Quantité :",font=("times new roman",15,'bold'), bg="white" )
        self.lbl_qte.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.txt_qte = ttk.Entry(produit_Frame,font=("times new roman",10),textvariable=self.qte ,width=12)
        self.txt_qte.grid(row=1, column=3, sticky=W, padx=5, pady=2)


        #### Recherche 
        rech_Frame = Frame(Main_Frame,bd=2, bg="white")
        rech_Frame.place(x=900,y=10, width=560, height=70)

        self.lbl_recherche = Label(rech_Frame,text="N° Facture :", font=("times new roman",20,"bold"),bg="white")
        self.lbl_recherche.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_recherche = ttk.Entry(rech_Frame, textvariable=self.rech_facture, font=("times new roman",20), width=15)
        self.txt_recherche.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.btn_recherche = Button(rech_Frame, text="Rechercher",command=self.rechercher, font=("times new roman",12,"bold"), height=2,width=11, bg="yellow", cursor="hand2")
        self.btn_recherche.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        # Espace facture 

        lbl_facture = LabelFrame(Main_Frame,text="Facture", font=("times new roman",15,"bold"),bg="white")
        lbl_facture.place(x=900, y=74, width=600, height=500)


        scroll_y = Scrollbar(lbl_facture, orient=VERTICAL) # Side bar au cas où la facture est longue
        self.textarea = Text(lbl_facture, font=("times new roman",13,"bold"), bg="white", fg="blue", yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y) # prend l'axe des Y : emplacement
        scroll_y.config(command=self.textarea.yview) # le rendre visible
        self.textarea.pack(fill=BOTH, expand=1) # mettre l'emplacement du textarea après les configs du scroll


        # Footer

        footer_Frame = LabelFrame(Main_Frame, text="Bouton", font=("times new roman", 15), bg="white")
        footer_Frame.place(x=10, y=574, width=1493, height=146) 

        self.lbl_totalbrut = Label(footer_Frame, text="Total Brut :", font=("times new roman",18,"bold"), bg="white")
        self.lbl_totalbrut.grid(row=0,column=0, sticky=W, padx=5, pady=2)

        self.lbl_taxe = Label(footer_Frame, text="Taxe :", font=("times new roman",18,"bold"), bg="white")
        self.lbl_taxe.grid(row=1,column=0, sticky=W, padx=5, pady=2)

        self.lbl_totalnet = Label(footer_Frame, text="Total Net :", font=("times new roman",18,"bold"), bg="white")
        self.lbl_totalnet.grid(row=2,column=0, sticky=W, padx=5, pady=2)

        self.txt_totalbrut = ttk.Entry(footer_Frame, textvariable=self.totalbrut,font=("times new roman",18),width=15 ,state="readonly")
        self.txt_totalbrut.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.txt_taxe = ttk.Entry(footer_Frame, textvariable=self.taxe,font=("times new roman",18),width=15 ,state="readonly")
        self.txt_taxe.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.txt_totalnet = ttk.Entry(footer_Frame, textvariable=self.totalnet,font=("times new roman",18),width=15 ,state="readonly")
        self.txt_totalnet.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        ##### Integrer l'image

        self.vue_image = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/principal.jpg"))
        self.lbl_image = Label(image=self.vue_image,width=860 ,height=380) # Conteneur de l'image
        self.lbl_image.place(x=15,y=242)

        #### Bouton

        Btn_Frame = Frame(footer_Frame, bd=2, bg="white",)
        Btn_Frame.place(x=350, y=0)

        self.ajoutPanier = Button(Btn_Frame, text="Ajouter Card",command=self.ajouter, width=12 ,height=2, font=("times new roman",18,"bold"), bg="green",cursor="hand2")
        self.ajoutPanier.grid(row=0, column=0,sticky=W, padx=5, pady=2)

        self.generer = Button(Btn_Frame, text="Générer\n Facture",command=self.genererFacture, width=12, height=2, font=("times new roman",18,"bold"), bg="cyan",cursor="hand2")
        self.generer.grid(row=0, column=1,sticky=W, padx=5, pady=2)

        self.sauvegarde = Button(Btn_Frame, text="Sauvegarder\n Facture",command=self.sauvegarder, width=12, height=2, font=("times new roman",18,"bold"), bg="gray",cursor="hand2")
        self.sauvegarde.grid(row=0, column=2,sticky=W, padx=5, pady=2)

        self.imprime = Button(Btn_Frame, text="Imprimer\n Facture",command=self.imprimer, width=12, height=2, font=("times new roman",18,"bold"), bg="blue",cursor="hand2")
        self.imprime.grid(row=0, column=3,sticky=W, padx=5, pady=2)

        self.reini = Button(Btn_Frame, text="Réinitialiser",command=self.reinitialiser ,width=12, height=2, font=("times new roman",18,"bold"), bg="#ff7a00",cursor="hand2")
        self.reini.grid(row=0, column=4,sticky=W, padx=5, pady=2)

        self.quitte = Button(Btn_Frame, text="Quitter",command=self.quitter ,width=12, height=2, font=("times new roman",18,"bold"), bg="red",cursor="hand2")
        self.quitte.grid(row=0, column=5,sticky=W, padx=5, pady=2)

        self.l = []

        self.bienvenue()

    ##### Fonctions du systeme
    def bienvenue(self):
        self.textarea.delete(1.0, END) # Pour supprimer le contenu
        self.textarea.insert(END, "\t            Bienvenue Chez KOKOU'S SUPER MARKET")
        self.textarea.insert(END, f"\n\nNuméro Facture : {self.num_facture.get()}")
        self.textarea.insert(END, f"\nPrénom Client : {self.client_prenom.get()}")
        self.textarea.insert(END, f"\nNom Client : {self.client_nom.get()}")
        self.textarea.insert(END, f"\nTéléphone : {self.client_tel.get()}")
        self.textarea.insert(END, "\n***************************************************************")
        self.textarea.insert(END, f"\nProduits\t\tQuantité\t\tMontant\t\tTVA")
        self.textarea.insert(END, "\n***************************************************************")


    def ajouter(self):
        self.n = self.prix.get()
        self.m = self.qte.get() * self.n # prix total de l'article
        self.l.append(self.m)
        if self.produit.get()=="":
            messagebox.showerror("Erreur", "Veuillez sélectionner un produit !")
        else:
            # on insert les information du produit au niveau de la facture
            self.textarea.insert(END, f"\n{self.produit.get()}\t\t{self.qte.get()}\t\t{round(self.m)}\t\t{self.m*0.18}")  # \t ==> tabulation
            self.totalbrut.set(str("%.2f"%(sum(self.l)))) # "Rs.%.2f" ==> 2 chiffres après la virgule
            self.taxe.set(str("%.2f"%((sum(self.l))*0.18)))
            self.totalnet.set(str("%.2f"%(sum(self.l)+(sum(self.l))*0.18)))


    def genererFacture(self):
        if self.produit.get()=="":
            messagebox.showerror("Erreur", "Ajouter au moins un produit !")
        else:
            text = self.textarea.get(9.99, (10.0+float(len(self.l))))
            self.bienvenue()
            text = self.textarea.insert(END,text)
            self.textarea.insert(END, "\n***************************************************************")
            self.textarea.insert(END, f"\nTotal Brut : \t\t\t\t\t\t{self.totalbrut.get()}")
            self.textarea.insert(END, f"\nTaxe : \t\t\t\t\t\t{self.taxe.get()}")
            self.textarea.insert(END, f"\nTotal Net : \t\t\t\t\t\t{self.totalnet.get()}")
            self.textarea.insert(END, "\n***************************************************************")
            

    def sauvegarder(self):
        op = messagebox.askyesno("Sauvegarder", "Voulez-vous sauvegarder la facture ?")
        if op==True:
            self.donneFacture = self.textarea.get(1.0,END)
            f1=open("C:/Users/winny/Desktop/Projet Python POO/factures/"+str(self.num_facture.get())+".txt","w", encoding='utf-8')
            f1.write(self.donneFacture)
            messagebox.showinfo("Sauvegarde", f"LA facture n° {self.num_facture.get()} a été enregistrer avec succès !")
            f1.close()

    
    def imprimer(self):
        fichier = tempfile.mktemp(".txt")
        open(fichier, "w").write(self.textarea.get(1.0,END))
        os.startfile(fichier,"print")

    def reinitialiser(self):
        self.textarea.delete(1.0,END)
        self.client_nom.set("")
        self.client_prenom.set("")
        self.client_tel.set("")
        self.client_mail.set("")
        x=random.randint(500,9999)
        self.num_facture.set(str(x))
        self.rech_facture.set("")
        self.produit.set("")
        self.prix.set(0)
        self.qte.set(0)
        self.l=[]
        self.totalbrut.set("")
        self.taxe.set("")
        self.totalnet.set("")
        self.txt_categorie.current(0)
        self.txt_souscategorie.config(values=[])
        self.txt_souscategorie.set("")
        self.txt_nomProduit.config(values=[])
        self.txt_nomProduit.set("")

        self.bienvenue()

    def quitter(self):
        root.quit()


    # rechercher une facture 
    def rechercher(self):
        trouver = "non"
        for i in os.listdir("C:/Users/winny/Desktop/Projet Python POO/factures/"):
            if i.split(".")[0]==self.rech_facture.get():
                f1 = open(f"C:/Users/winny/Desktop/Projet Python POO/factures/{i}","r", encoding='utf-8')
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                f1.close
                trouver ="oui"
        
        if trouver == "non":
            messagebox.showerror("Erreur", "La facture n'existe pas !")
        


    ######## Fonction qui gère les sous-categorie 
    def fonctionCategorie(self, even=""):
        #["selectionner","vêtement", "Montre", "Téléphone"]
        if self.txt_categorie.get()=="Vêtement" :
            self.txt_souscategorie.config(values=self.list_souscategorieVetement)
            self.txt_souscategorie.current(0)

        elif self.txt_categorie.get()=="Montre" :
            self.txt_souscategorie.config(values=self.list_souscategorieMontre)
            self.txt_souscategorie.current(0)
        
        elif self.txt_categorie.get()=="Téléphone" :
            self.txt_souscategorie.config(values=self.list_souscategorieTelephone)
            self.txt_souscategorie.current(0)


    def fonctionSousCategorie(self,even=""):
        # Vêtement
        if self.txt_souscategorie.get()== "Pantalon" :
            self.txt_nomProduit.config(values=self.pantalon)
            self.txt_nomProduit.current(0)

        elif self.txt_souscategorie.get()== "T-Shirt" :
            self.txt_nomProduit.config(values=self.tshirt)
            self.txt_nomProduit.current(0)
        
        elif self.txt_souscategorie.get()== "Jogging" :
            self.txt_nomProduit.config(values=self.jogging)
            self.txt_nomProduit.current(0)
        
        # Montre
        elif self.txt_souscategorie.get()== "Rolex" :
            self.txt_nomProduit.config(values=self.rolex)
            self.txt_nomProduit.current(0)

        elif self.txt_souscategorie.get()== "Casio" :
            self.txt_nomProduit.config(values=self.casio)
            self.txt_nomProduit.current(0)

        elif self.txt_souscategorie.get()== "Mont Blanc" :
            self.txt_nomProduit.config(values=self.montblanc)
            self.txt_nomProduit.current(0)

        # Téléphone
        elif self.txt_souscategorie.get()== "Tecno" :
            self.txt_nomProduit.config(values=self.tecno)
            self.txt_nomProduit.current(0)

        elif self.txt_souscategorie.get()== "Iphone" :
            self.txt_nomProduit.config(values=self.iphone)
            self.txt_nomProduit.current(0)

        elif self.txt_souscategorie.get()== "Samsung" :
            self.txt_nomProduit.config(values=self.samsung)
            self.txt_nomProduit.current(0)
            

    def fonctionNomProduit(self, event=""):
        #Vetements
        if self.txt_nomProduit.get()== "Levis" :
            #self.txt_nomProduit.config(text=self.price_levis)
            self.prix.set(self.price_levis)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Dior" :
            #self.txt_nomProduit.config(text=self.price_dior)
            self.prix.set(self.price_dior)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Gucci" :
            #self.txt_nomProduit.config(text=self.price_gucci)
            self.prix.set(self.price_gucci)
            self.qte.set(1)
        
        elif self.txt_nomProduit.get()== "Polo" :
            #self.txt_nomProduit.config(text=self.price_polo)
            self.prix.set(self.price_polo)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Roadster" :
            #self.txt_nomProduit.config(text=self.price_roadster)
            self.prix.set(self.price_roadster)
            self.qte.set(1)
        
        elif self.txt_nomProduit.get()== "Nike" :
            #self.txt_nomProduit.config(text=self.price_nike)
            self.prix.set(self.price_nike)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Adidas" :
            #self.txt_nomProduit.config(text=self.price_adidas)
            self.prix.set(self.price_adidas)
            self.qte.set(1)
        
        elif self.txt_nomProduit.get()== "Puma" :
            #self.txt_nomProduit.config(text=self.price_puma)
            self.prix.set(self.price_puma)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Balmain" :
            #self.txt_nomProduit.config(text=self.price_balmain)
            self.prix.set(self.price_balmain)
            self.qte.set(1)
    
        #Montres 
        if self.txt_nomProduit.get()== "Air-King" :
            #self.txt_nomProduit.config(text=self.price_airking)
            self.prix.set(self.price_airking)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "DateJust" :
            #self.txt_nomProduit.config(text=self.price_datejust)
            self.prix.set(self.price_datejust)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "GMT-MASTER II" :
            #self.txt_nomProduit.config(text=self.price_gmtmaster)
            self.prix.set(self.price_gmtmaster)
            self.qte.set(1)
        
        elif self.txt_nomProduit.get()== "BABY-G" :
            #self.txt_nomProduit.config(text=self.price_babyg)
            self.prix.set(self.price_babyg)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Edifice" :
            #self.txt_nomProduit.config(text=self.price_edifice)
            self.prix.set(self.price_edifice)
            self.qte.set(1)
        
        elif self.txt_nomProduit.get()== "Sheen" :
            #self.txt_nomProduit.config(text=self.price_sheen)
            self.prix.set(self.price_sheen)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Boheme" :
           # #self.txt_nomProduit.config(text=self.price_boheme)
            self.prix.set(self.price_boheme)
            self.qte.set(1)
        
        elif self.txt_nomProduit.get()== "Heritage" :
            #self.txt_nomProduit.config(text=self.price_heritage)
            self.prix.set(self.price_heritage)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "TimeWalker" :
            #self.txt_nomProduit.config(text=self.price_timewalker)
            self.prix.set(self.price_timewalker)
            self.qte.set(1)

        #Téléphone
        if self.txt_nomProduit.get()== "Camon" :
            #self.txt_nomProduit.config(text=self.price_camon)
            self.prix.set(self.price_camon)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Spark" :
            #self.txt_nomProduit.config(text=self.price_spark)
            self.prix.set(self.price_spark)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Phantom" :
            #self.txt_nomProduit.config(text=self.price_phantom)
            self.prix.set(self.price_phantom)
            self.qte.set(1)
        
        elif self.txt_nomProduit.get()== "Iphone 12" :
            #self.txt_nomProduit.config(text=self.price_iphone12)
            self.prix.set(self.price_iphone12)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Iphone 13" :
            #self.txt_nomProduit.config(text=self.price_iphone13)
            self.prix.set(self.price_iphone13)
            self.qte.set(1)
        
        elif self.txt_nomProduit.get()== "Iphone 14" :
           # self.txt_nomProduit.config(text=self.price_iphone14)
            self.prix.set(self.price_iphone14)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Galaxy" :
            #self.txt_nomProduit.config(text=self.price_galaxy)
            self.prix.set(self.price_galaxy)
            self.qte.set(1)
        
        elif self.txt_nomProduit.get()== "Note" :
           # self.txt_nomProduit.config(text=self.price_note)
            self.prix.set(self.price_note)
            self.qte.set(1)

        elif self.txt_nomProduit.get()== "Ultra" :
            #self.txt_nomProduit.config(text=self.price_ultra)
            self.prix.set(self.price_ultra)
            self.qte.set(1)

        
        





if __name__ == "__main__":  # Si on import le script, il ne s'executera pas
    root = Tk()
    obj = SuperMarket(root)
    root.mainloop()


