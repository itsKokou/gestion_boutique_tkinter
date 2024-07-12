from tkinter import *
from time import strftime
from PIL import ImageTk, Image #Gerer des images pour qu'elles s'affichent
from Boutiques.mode import *
from Boutiques.formConnexion import *

class Mall :
    nomFact = ""
    user = User(0,"","","","",2,1)
    testConn = False # teste si on est connecté
    testProduit = False # Teste si un achat est en cours 
    def __init__(self,root) -> None:
        self.root = root
        self.root.title("Centre Commercial")
        self.root.geometry("1520x780+0+0") #Taille de l'interface 
        self.root.resizable(FALSE,FALSE)
        self.root.config(bg="white")

        self.title = Label(self.root, text="WELCOME TO WINZIZ's MALL", font=("Algerian",32), bg="#00d1ff", fg="black")
        self.title.pack(side=TOP, fill=X)

        self.lbl_heure = Label(self.root, font=("times new roman",14),bg="#00d1ff",fg="black")
        self.lbl_heure.place(x=0,y=27,width=120, height=20)

        self.lbl_date = Label(self.root,text=strftime("%d/%m/%Y") ,font=("times new roman",14),bg="#00d1ff",fg="black")
        self.lbl_date.place(x=0,y=5,width=120, height=20)

        self.btn_seConnecter = Button(self.root, text="Se Connecter",command=self.connexion ,width=12, height=1, font=("times new roman",14,"bold"), bg="orange",cursor="hand2", pady=7)
        self.btn_seConnecter.place(x=1370,y=2)

        if Mall.testConn == True :
            self.btn_seConnecter.config(text="Déconnexion")

        Main_Frame = Frame(self.root,bd=2, relief=GROOVE, bg="white")
        Main_Frame.place(x=0,y=54, width=1521,height=750)

        top_Frame =Frame(Main_Frame, bg="white" )
        top_Frame.place(x=0,y=25 ,width=1521, height=320)

        bottom_Frame =Frame(Main_Frame,  bg="white" )
        bottom_Frame.place(x=0,y=350 ,width=1521, height=320)

        self.image_mode = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/modes.jpg"))
        self.lbl_mode = Label(top_Frame, image = self.image_mode, width=450,height=200) # Conteneur de l'image
        self.lbl_mode.place(x=30, y= 5)

        self.btn_mode = Button(top_Frame, text="Mode",command=self.interMode ,width=12, height=2,font=("times new roman",18,"bold"), bg="cyan",cursor="hand2")
        self.btn_mode.place(x=150, y= 220)

        self.image_bijouterie = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/bijouteries.jpg"))
        self.lbl_bijouterie = Label(top_Frame,image=self.image_bijouterie,width=450 ,height=200)
        self.lbl_bijouterie.place(x=525, y=5)

        self.btn_bijouterie = Button(top_Frame, text="Bijouterie",command=self.interBijouterie ,width=12, height=2,font=("times new roman",18,"bold"), bg="cyan",cursor="hand2")
        self.btn_bijouterie.place(x=645, y= 220)

        self.image_maison = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/maisons.jpg"))
        self.lbl_maison = Label(top_Frame,image=self.image_maison,width=450 ,height=200) 
        self.lbl_maison.place(x=1020, y=5)

        self.btn_maison = Button(top_Frame, text="Maison",command=self.interMaison ,width=12, height=2,font=("times new roman",18,"bold"), bg="cyan",cursor="hand2")
        self.btn_maison.place(x=1140, y= 220)

        #---------------------------------
        self.image_sport = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/sports.jpg"))
        self.lbl_sport = Label(bottom_Frame, image = self.image_sport, width=450,height=200) # Conteneur de l'image
        self.lbl_sport.place(x=30, y= 5)

        self.btn_sport = Button(bottom_Frame, text="Sport",command=self.interSport ,width=12, height=2,font=("times new roman",18,"bold"), bg="cyan",cursor="hand2")
        self.btn_sport.place(x=150, y= 220)

        self.image_restaurant = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/restaurants.jpg"))
        self.lbl_restaurant = Label(bottom_Frame,image=self.image_restaurant,width=450 ,height=200)
        self.lbl_restaurant.place(x=525, y=5)

        self.btn_restaurant = Button(bottom_Frame, text="Restaurant",command=self.interRestaurant ,width=12, height=2,font=("times new roman",18,"bold"), bg="cyan",cursor="hand2")
        self.btn_restaurant.place(x=645, y= 220)

        self.image_alimentation = ImageTk.PhotoImage(Image.open("C:/Users/winny/Desktop/Projet Python POO/images/principal.jpg"))
        self.lbl_alimentation = Label(bottom_Frame,image=self.image_alimentation,width=450 ,height=200) 
        self.lbl_alimentation.place(x=1020, y=5)

        self.btn_alimentation = Button(bottom_Frame, text="Alimentation",command=self.interAlimentation ,width=12, height=2,font=("times new roman",18,"bold"), bg="cyan",cursor="hand2")
        self.btn_alimentation.place(x=1140, y= 220)

        

        self.footer = Label(self.root, text="Always with YOU...", font=("Monotype Corsiva",22,"bold"), bg="#00d1ff", fg="black")
        self.footer.pack(side=BOTTOM, fill=X )

        self.heure()


    #---------------Fonctions 
    def heure(self):
        h = strftime("%H:%M:%S") # récuperer l'heure
        self.lbl_heure.config(text=h) # met l'heure dans le label 
        self.lbl_heure.after(1000,self.heure) # chaque 1000 milliseconde, la fonction se relance

    def interMode(self):
        self.root.destroy()
        self.root.quit()
        root =Tk()
        ob = Mode(root)
        root.mainloop()

    def interBijouterie(self):
        from Boutiques.bijouterie import Bijouterie
        self.root.destroy()
        self.root.quit()
        root =Tk()
        ob = Bijouterie(root)
        root.mainloop()

    def interMaison(self):
        from Boutiques.maison import Maison
        self.root.destroy()
        self.root.quit()
        root =Tk()
        ob = Maison(root)
        root.mainloop()

    def interSport(self):
        from Boutiques.sport import Sport
        self.root.destroy()
        self.root.quit()
        root =Tk()
        ob = Sport(root)
        root.mainloop()

    def interAlimentation(self):
        from Boutiques.alimentation import Alimentation
        self.root.destroy()
        self.root.quit()
        root =Tk()
        ob = Alimentation(root)
        root.mainloop()

    def interRestaurant(self):
        from Boutiques.restaurant import Restaurant
        self.root.destroy()
        self.root.quit()
        root =Tk()
        ob = Restaurant(root)
        root.mainloop()

    def connexion(self):
        if Mall.testConn == False:
            self.root.destroy()
            self.root.quit()        
            root = Tk()
            ob = Form(root)
            root.mainloop()
        else :
            self.root.destroy()
            self.root.quit()
            Mall.testConn =False


        





# app = Tk()
# obj = Mall(app)

# if obj.testConn == True :
#     obj.btn_seConnecter.config(text="Déconnexion")
# app.mainloop()