from tkinter import *
import tkinter.messagebox

#remarque : on réalise une bataille de carte classique en un seul tour (une fois le paquet de 26 cartes épuisé le programme s'arrête)

class Jeu_de_carte (object):

    #definition des attributs de classe
    
    def __init__(self):
        self.couleur = ["Trefle","Carreau","Pique","Coeur"]
        self.valeur = ["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","As"]
        
    #définition des méthodes

    #création d'un paquet de 52 cartes    
    def creer_paquet (self): 
        self.paquet_total= []
        for i in self.couleur :
            for j in self.valeur :
                self.paquet_total.append (str(j) + " de " + str(i))

    #mélange aléatoire
    def melanger (self): 
        import random
        random.shuffle(self.paquet_total)

    #séparation en deux, un paquet de 26 cartes pour le joueur et l'ordi
    def distribuer (self):
        self.paquet_joueur = []
        self.paquet_ordi = []
        self.paquet_joueur = self.paquet_total[:26]
        self.paquet_ordi = self.paquet_total[26:]

class Bataille (object):

    def __init__(self):

        #import des deux paquets de 26 cartes mélangées de la classe Jeu_de_carte
        self.a = Jeu_de_carte ()
        self.a.creer_paquet ()
        self.a.melanger ()
        self.a.distribuer ()

        #création de l'interface graphique
        self.window = Tk() #création de l'interface dans une fenêtre avec le module Tkinter
        self.window.title("Bataille") #titre fenêtre
        self.window.iconbitmap("cartes/logo.ico") #logo de la fenêtre de jeu
        self.window.config(bg ='#1D813A') #choix de la couleur du fond (bg = background)
        self.window.geometry("850x400") #dimension de la fenêtre d'affichage

        #création de variables et de listes
        self.list_comparaison = [] #liste des cartes qui s'affrontent au centre à chaque tour
        self.score_joueur = 0 #score joueur
        self.score_ordi = 0 #score ordi
        self.compt=0 #compteur du nombre de batailles d'affilée
          

    def debut (self):

        #création du plateau de jeu en haut
        self.window_top = tkinter.Frame(self.window, bg="#8C2323") #création de la fenêtre pour le plateau de jeu
        self.window_top.pack(side="top",padx=5,pady=5) #affichage du plateau de jeu
        self.dos_carte = tkinter.PhotoImage(file = "cartes/dos.gif") #import de l'image de dos de carte
        self.case_vide = tkinter.PhotoImage(file = "cartes/vide.gif") #import de l'image de case vide
        self.paquet_joueur = tkinter.Label (self.window_top,image=self.dos_carte) #placement de l'image sur le plateau en haut
        self.paquet_joueur.pack (side="left", padx = 5, pady = 5) #affichage de l'image --> paquet du joueur
        self.carte_joueur = tkinter.Label (self.window_top,image=self.case_vide) #placement de l'image sur le plateau en haut
        self.carte_joueur.pack (side="left", padx = 10, pady = 5) #affichage de l'image --> zone de jeu du joueur
        self.carte_ordi = tkinter.Label (self.window_top,image=self.case_vide) #placement de l'image sur le plateau en haut
        self.carte_ordi.pack (side="left", padx = 10, pady = 5) #affichage de l'image --> zone de jeu de l'ordi
        self.paquet_ordi = tkinter.Label (self.window_top,image=self.dos_carte) #placement de l'image sur le plateau en haut
        self.paquet_ordi.pack (side="left", padx = 5, pady = 5) #affichage de l'image --> paquet de l'ordi

 
        #création du tableau des scores au centre
        self.window_mid = tkinter.Frame(self.window,bg="black") #création de la fenêtre tableau des scores
        self.window_mid.pack(side="top",padx=30,pady=5) #affichage du tableau des scores
        self.window_mid_gauche = tkinter.Frame(self.window_mid,bg="white") #sous-fenêtre pour le score joueur
        self.window_mid_gauche.pack(side="left",padx=5,pady=5) #affichage de la sous-fenêtre score joueur
        #création du texte joueur :
        self.text_joueur = tkinter.Label(self.window_mid_gauche, text="JOUEUR"+"\n"+str(len (self.a.paquet_joueur))+ " cartes restantes" + "\n" + str(self.score_joueur)+ " points",fg = 'black',bg = 'white', font=('courier', 15, 'bold'))
        self.text_joueur.pack (side="left", padx=85, pady=10) #affichage du texte score joueur
        self.window_mid_droite = tkinter.Frame(self.window_mid,bg="white") #création de la sous-fenêtre pour le score ordi
        self.window_mid_droite.pack(side="left",padx=5,pady=5) #affichage de la sous-fenêtre score ordi
        #création du texte ordi :
        self.text_ordi = tkinter.Label(self.window_mid_droite, text="ORDI"+"\n"+str(len (self.a.paquet_ordi))+ " cartes restantes" + "\n" + str(self.score_ordi)+ " points",fg = 'black',bg = 'white', font=('courier', 15, 'bold'))
        self.text_ordi.pack (side="left", padx=60, pady=10) #affichage du texte score ordi

        #création de la barre des tâches en bas
        self.window_bot = tkinter.Frame(self.window,bg="white") #création de la fenêtre barre des tâches
        self.window_bot.pack(side="bottom",padx=10,pady=10) #affichage de la fenêtre barre des tâches
        self.fleche_rejouer = tkinter.PhotoImage(file = "cartes/fleche_rejouer.gif") #import image flèche "rejouer"
        self.fleche_jouer = tkinter.PhotoImage(file = "cartes/fleche_jouer.gif") #import image flèche "continuer"/"tour suivant"
        self.bouton_rejouer = tkinter.Button(self.window_bot,relief="raised",image=self.fleche_rejouer,command=self.rejouer) #création bouton "rejouer"
        self.bouton_rejouer.pack(side="left",padx=20,pady=10) #affichage bouton "rejouer"
        self.bouton_jouer = tkinter.Button(self.window_bot,relief="raised",image=self.fleche_jouer,command=self.jeu_jouer) #création bouton "continuer"
        self.bouton_jouer.pack(side="left",padx=20,pady=10) #affichage bouton "continuer"
         

    def jeu_jouer (self):
        
        while len(self.a.paquet_joueur)!= 0 : #tant que le joueur a encore des cartes 
            self.list_comparaison.append(self.a.paquet_joueur.pop(0)) #extraction de la dernière carte de la liste paquet_joueur pour la comparer en l'ajoutant dans la liste list_comparaison
            self.list_comparaison.append(self.a.paquet_ordi.pop(0)) #extraction de la dernière carte de la liste paquet_ordi pour la comparer en l'ajoutant dans la liste list_comparaison
            
            if self.a.valeur.index(self.list_comparaison[0].split()[0])>self.a.valeur.index(self.list_comparaison[1].split()[0]): #cas où le joueur remporte le pli (possède une carte de valeur supérieure à celle de l'ordi)
                #extraction de l'image correspondant à la carte du joueur :
                self.carte_joueur_jeu = tkinter.PhotoImage(file ="cartes/" + self.list_comparaison[0].split ()[0].lower () + "_" + self.list_comparaison[0].split ()[2].lower () + ".gif")
                self.carte_joueur.config (image=self.carte_joueur_jeu) #affichage de la carte joueur
                #extraction de l'image correspondant à la carte de l'ordi :                 
                self.carte_ordi_jeu = tkinter.PhotoImage(file ="cartes/" + self.list_comparaison[1].split ()[0].lower () + "_" + self.list_comparaison[1].split ()[2].lower () + ".gif")
                self.carte_ordi.config (image=self.carte_ordi_jeu) #affichage de la carte ordi
                self.list_comparaison = [] #réinitilalisation de la liste de comparaison
                #score joueur (1 carte = 1 points):
                if self.compt != 0: #si ce gain intervient suite à une ou plusieurs batailles successives
                    self.score_joueur += 6+4*(self.compt-1) #le joueur remporte les 6 cartes jouées (2 cartes de face égales + 2 cartes faces cachées + 2 cartes de fin de première bataille) + 4 pour chaque nouvelle bataille (2 cartes de dos + 2 cartes de fin de bataille)
                else : #sinon (cas le plus courant)
                    self.score_joueur += 2 #le joueur remporte le pli des deux cartes jouées 
                self.text_joueur.config (text="JOUEUR"+"\n"+str(len (self.a.paquet_joueur))+ " cartes restantes" + "\n" + str(self.score_joueur)+ " points") #affichage du score joueur et nombre de cartes restantes
                self.text_ordi.config (text="ORDI"+"\n"+str(len (self.a.paquet_ordi))+ " cartes restantes" + "\n" + str(self.score_ordi) + " points") #affichage score ordi et nombre de cartes restantes
                self.compt=0 #remise à 0 du compteur de batailles successives
                
            
            elif self.a.valeur.index(self.list_comparaison[0].split()[0])<self.a.valeur.index(self.list_comparaison[1].split()[0]): #cas où l'ordi remporte le pli (structuresimilaire à joueur)
                #extraction de l'image correspondant à la carte du joueur :
                self.carte_joueur_jeu = tkinter.PhotoImage(file ="cartes/" + self.list_comparaison[0].split ()[0].lower () + "_" + self.list_comparaison[0].split ()[2].lower () + ".gif")
                self.carte_joueur.config (image=self.carte_joueur_jeu) #affichage de la carte joueur
                #extraction de l'image correspondant à la carte de l'ordi : 
                self.carte_ordi_jeu = tkinter.PhotoImage(file ="cartes/" + self.list_comparaison[1].split ()[0].lower () + "_" + self.list_comparaison[1].split ()[2].lower () + ".gif")
                self.carte_ordi.config (image=self.carte_ordi_jeu) #affichage de la carte ordi
                self.list_comparaison = [] #réinitilalisation de la liste de comparaison
                #score ordi :
                if self.compt != 0 :
                    self.score_ordi += 6+4*(self.compt-1)     
                else :
                    self.score_ordi += 2
                #affichage du score :
                self.text_joueur.config (text="JOUEUR"+"\n"+str(len (self.a.paquet_joueur))+ " cartes restantes" + "\n" + str(self.score_joueur) + " points")
                self.text_ordi.config (text="ORDI"+"\n"+str(len (self.a.paquet_ordi))+ " cartes restantes" + "\n" + str(self.score_ordi)+ " points")
                self.compt=0 #remise à 0 du compteur de batailles successives
                
              
            else: #bataille : cas où les cartes sont égales
                    #extraction de l'image correspondant à la carte du joueur :
                    self.carte_joueur_jeu = tkinter.PhotoImage(file ="cartes/" + self.list_comparaison[0].split ()[0].lower () + "_" + self.list_comparaison[0].split ()[2].lower () + ".gif")
                    self.carte_joueur.config (image=self.carte_joueur_jeu) #affichage de la carte joueur
                    #extraction de l'image correspondant à la carte de l'ordi:
                    self.carte_ordi_jeu = tkinter.PhotoImage(file ="cartes/" + self.list_comparaison[1].split ()[0].lower () + "_" + self.list_comparaison[1].split ()[2].lower () + ".gif")
                    self.carte_ordi.config (image=self.carte_ordi_jeu) #affichage de la carte ordi
                    self.text_joueur.config (text="JOUEUR"+"\n"+str(len (self.a.paquet_joueur))+ " cartes restantes" + "\n" + str(self.score_joueur) + " points") #affichage du score joueur (inchangé) et nombre de cartes restantes
                    self.text_ordi.config (text="ORDI"+"\n"+str(len (self.a.paquet_ordi))+ " cartes restantes" + "\n" + str(self.score_ordi)+ " points") #affichage du score ordi (inchangé) et nombre de cartes restantes
                    tkinter.messagebox.showinfo(message="BATAILLE !") #affichage d'un message signalant la bataille dans une fenêtre pop-up
                    if len(self.a.paquet_joueur)!=0: # exclusion du cas particulier d'une bataille au dernier tour (listes paquet_joueur et paquet_ordi vides on ne peut donc pas utiliser .pop())
                        self.list_comparaison = [] #réinitialisation de la liste de comparaison
                        self.a.paquet_joueur.pop(0) #on retire une carte du paquet joueur (la carte face cachée)
                        self.a.paquet_ordi.pop(0) #on retire une carte du paquet ordi (la carte face cachée)
                        self.compt +=1 #le compteur du nombre de batailles successives

            break #sortie de la boucle while

        if len(self.a.paquet_joueur) == 0: #une fois le paquet de 26 cartes épuisé
                    if self.score_joueur > self.score_ordi :
                        tkinter.messagebox.showinfo(message="Gagné !") #message pop-up de victoire du joueur
                    elif self.score_joueur < self.score_ordi :
                        tkinter.messagebox.showinfo(message="Perdu !") #message pop-up de victoire de l'ordi
                    else :
                        tkinter.messagebox.showinfo(message="Égalité !") #message pop-up d'égalité


    def rejouer (self): #recommencer
        self.window.destroy( ) #détruire la partie précédente
        root = Bataille()
        root.debut () #exécution du script à partir du début

if __name__ =='__main__': #exécution directe du script au lancement du programme
    root = Bataille()
    root.debut()

