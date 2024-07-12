
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

