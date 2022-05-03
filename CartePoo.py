from random import *

class Carte:
    DN={1:"as",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"dame",12:"valet",13:"roi"}
    DS={"p":"pique", "ca":"carreau", "c":"coeur", "t":"treffe"}

    def __init__(self,num,symbole):
        self.num=num
        self.symbole=symbole

    def Afficher(self):
        print(f"{Carte.DN[self.num]} de {Carte.DS[self.symbole]}")    

class Cartes:

    def __init__(self):
        self.liste_de_cartes=[]
        for carte in range(1,14):
            for c in Carte.DS.keys():
                card=Carte(carte,c)
                self.liste_de_cartes.append(card)
    def affich(self):
        for elt in self.liste_de_cartes:
            elt.Afficher()
    def tirer_carte(self):
        if len(self.liste_de_cartes)>0:
            intermediaire=choice(self.liste_de_cartes)
            resultat=intermediaire
            self.liste_de_cartes.remove(intermediaire)
            return resultat
        return None    

    @property
    def melanger_cartes(self):
        if len(self.liste_de_cartes) >1:
            shuffle(self.liste_de_cartes)
           
def main():
    c1=Cartes()
    c2=Cartes()   

    c1.melanger_cartes
    c2.melanger_cartes

    score_c1=0
    score_c2=0

    for i in range (0,len(c1.liste_de_cartes)):
        carte1 = c1.tirer_carte()
        carte2 = c2.tirer_carte()

        if carte1.num > carte2.num:
            score_c1+=1
        elif carte1.num < carte2.num:
            score_c2+=1 
        else:
            score_c1+=0
            score_c2+=0      


    if score_c1 > score_c2:
        print(f"c1 a gagné avec un score de {score_c1} points ")
    elif score_c1 < score_c2:
        print(f"c2 a gagné avec un score de {score_c2} points ")  
    else:
        print(f"Egalité avec un score de {score_c1} points des deux cotés")


main()