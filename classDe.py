from random import randrange
from tkinter import *
class De:

    def __init__(self):
        self.De = 0

    
    def lancerLeDe(self):

        self.De = randrange(1,6)
        print(self.De)


class Joueur:
    def __init__(self):
        

        
        self.nombreJeton = 0
        self.DeStart = 0
        self.De1= 0
        self.De2= 0
        self.De3= 0
    def lancerDeStart(self):
        self.DeStart = randrange (1,6)
        print(self.DeStart)
    def lancerLesDés(self):
        self.De1 = randrange (1,6)
        self.De2 = randrange (1,6)
        self.De3 = randrange (1,6)




class TableDeJeu(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)


        #Variable des jetons de la banque
        self.banque = 13
        #Varible enregistrant le joueur qui commence
        self.premierJoueur = ""
        
        #Initialisation du joueur 1
        self.j1 = Label(self, text="Joueur 1-")
        self.j1.grid(row=0, column=0)
        self.Joueur1 = Joueur()
        self.bouton = []
        self.label = []
        self.bouton.append(Button(self, text="Lancer le dé", command= lambda: self.lancerDeStart(self.Joueur1, 0)))
        
        self.label.append(Label(self, text="Ceci est le label général"))
        self.label[0].grid(row= 0, column=2)
        self.bouton[0].grid(row=0, column=3)
        

        #Initialisaton du joueur 2
        self.j2 = Label(self, text="Joueur 2-")
        self.j2.grid(row=2, column=0)
        self.Joueur2 = Joueur()
        self.bouton.append(Button(self, text="Lancer le dé", command= lambda: self.lancerDeStart(self.Joueur2, 1)))
        self.label.append(Label(self, text="Ceci est le label général"))
        self.label[1].grid(row=2, column=2)
        self.bouton[1].grid(row=2, column=3)
        
        #Initialisation Label général
        self.LabelGeneral = Label(self, text="Ceci est le label général")
        self.LabelGeneral.grid(row=4, column=0)
        #Initialisation bouton général
        self.bouton.append(self.bouton.append(Button(self, text="Démarer la partie", command= lambda: self.lancementDeLaPartie())))
        self.bouton[2].grid(row=6, column=5)

    def lancerDeStart(self, Joueur, x):
        Joueur.DeStart = randrange (1,6)
        lol = "Vous avez fait " + str(Joueur.DeStart) + " au dé de démarage!"
        self.label[x].configure(text = lol)
        print(Joueur.DeStart)
    
    

    def lancementDeLaPartie(self):
        print("Partie lancé")
        if self.Joueur1.DeStart > self.Joueur2.DeStart:
            self.LabelGeneral.configure(text="Joueur 1, vous commencerez à jouer")
            self.demarerLaPartie(self.Joueur1, self.Joueur2)
        elif self.Joueur1.DeStart == self.Joueur2.DeStart:
            self.LabelGeneral.configure(text="Meme nombre, veuillez relancer les dé ainsi que la partie")
        else:
            self.LabelGeneral.configure(text="Joueur 2, vous commencerez à jouer")
            self.demarerLaPartie(self.Joueur2, self.Joueur1)
    def lancerDeDeLaPArtie(self, joueur, x):
        joueur.lancerLesDés()
        self.label[x].configure(text="Dé: " + str(joueur.De1) + " Dé: " + str(joueur.De2) + " Dé: " + str(joueur.De3))

    def resultat(self, joueur1, joueur2):
        poidJ1=0
        poidJ2=0
        j11 = [joueur1.De1,joueur1.De2, joueur1.De3]
        j22 = [joueur2.De1,joueur2.De2, joueur2.De3]

        j11 = sorted(j11, reverse=True)
        j22 = sorted(j22, reverse=True)
        
        if j11 == [4,2,1]:
            poidJ1=8
        elif j22 == [4,2,1]:
            poidJ2=8

        elif j11 == [1,1,1]:
            poidJ1=7
        elif j22 == [1,1,1]:
            poidJ2=7
        elif j11[2] == 1 and j11[1] == 1:
            poidJ1 = j11[0]
        elif j22[2] == 1 and j22[1] == 1:
            poidJ2 = j22[0]
        elif j11[0] == j11[1] and j11[1] == j11[2]:
            poidJ1 = 3
        elif j22[0] == j22[1] and j22[1] == j22[2]:
            poidJ2 = 3
        elif j11 == [6,5,4] or j11 == [5,4,3] or j11 == [4,3,2] or j11 == [3,2,1]:
            poidJ1 = 2
        elif j22 == [6,5,4] or j22 == [5,4,3] or j22 == [4,3,2] or j22 == [3,2,1]:
            poidJ2 = 2
        else:
            if j11[0]+j11[1] + j11[2] > j22[0]+j22[1] + j22[2]:
                poidJ1 = 1
            else:
                poidJ2 =1
        
        if poidJ1 > poidJ2:
            self.LabelGeneral.configure(text="Bravo joueur 1, vous avez gagner. Joueur 2, vous prenez " + str(poidJ1) + "jetons")
            self.Joueur2.nombreJeton = self.Joueur2.nombreJeton + poidJ1
            print("test jeton J2 " + str(self.Joueur2.nombreJeton))
            self.score.configure(text="Joueur1: " + str(self.Joueur1.nombreJeton) + "   Joueur2: " + str(self.Joueur2.nombreJeton))
        else:
            self.LabelGeneral.configure(text="Bravo joueur 2, vous avez gagner. Joueur 1, vous prenez " + str(poidJ2) + "jetons")
            self.Joueur1.nombreJeton = self.Joueur1.nombreJeton + poidJ2
            print("test jeton J1 " + str(self.Joueur1.nombreJeton))
            self.score.configure(text="Joueur1: " + str(self.Joueur1.nombreJeton) + "   Joueur2: " + str(self.Joueur2.nombreJeton))


        print(poidJ1)
        


    def demarerLaPartie(self, joueur1, joueur2):

        
        #On refait graphiquemment la fenêtre

        self.LabelGeneral.grid(row=0, column=0)

        #Label joueur 1 ligne 2
        self.j1.grid(row=2, column=0)
        self.label[0].grid(row=2, column=2)
        self.bouton[0].grid(row=2, column=3)
        #Label joueur2 ligne 3
        self.j2.grid(row=3, column=0)
        self.label[1].grid(row=3, column=2)
        self.bouton[1].grid(row=3, column=3)

        #Enlever le bouton lancer la partie
        self.bouton[2].configure(text="Continuer la partie!", command= lambda: self.resultat(self.Joueur1, self.Joueur2) )

        #Renomage des bouttons de lancer le dé a lancer les dés et changer la fonction
        self.bouton[0].configure(text="Lancer les dés", command= lambda: self.lancerDeDeLaPArtie(self.Joueur1, 0))
        self.bouton[1].configure(text="Lancer les dés", command= lambda: self.lancerDeDeLaPArtie(self.Joueur2, 1))
        
        #Creation d'un label pour le score
        self.score = Label(self, text="Joueur1: " + str(self.Joueur1.nombreJeton) + "   Joueur2: " + str(self.Joueur2.nombreJeton))
        self.score.grid(row=5, column=1)

        
    


   

            
        
    

    
