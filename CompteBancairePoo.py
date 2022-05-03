class CompteBancaire:
    NBCOMP=0
    def __init__(self,cin,nom,prenom,credit,debit,adresse="Monastir"):
        self.__cin=cin
        CompteBancaire.NBCOMP+=1
        self.__rib=CompteBancaire.NBCOMP
        self.__nom=nom
        self.__prenom=prenom
        self._credit=credit
        self._debit=debit
        self.adresse=adresse
       

    @property 
    def get_cin(self):
        return self.__cin
 
    def set_cin(self,x):
        try:
            self.__cin=x
        except:
             print("cet attribut ne peut pas etre modifié")

    @property
    def get_rib(self):
        return self.__rib
   
    def set_rib(self,x):
        try:
            self.__rib=x
        except:
            print("cet attribut ne peut pas etre modifié")

    @property
    def get_nom(self):
        return self.__nom
 
    def set_nom(self,x):
        try:
            self.__nom=x
        except:
             print("cet attribut ne peut pas etre modifié")

    @property
    def get_prenom(self):
        return self.__prenom

    def set_prenom(self,x):
        try:
            self.__prenom=x
        except :
            print("cet attribut ne peut pas etre modifié")

    def solde(self):
        return self._debit - self._credit 

    def deposer(self,montant):
        self._debit+=montant

    def retirer(self,montant):
        self._debit-=montant  

    def __str__(self):
        return f"cin:{self.__cin} , nom:{self.__nom} , prenom: {self.__prenom} , rib: {self.get_rib} , solde: {self.solde()} "      


class CompteEpargne(CompteBancaire):
    def __init__(self,cin,nom,prenom,credit,debit,adresse,taux):
        super().__init__(cin,nom,prenom,credit,debit,adresse)
        self.taux=taux
    def calculInteret(self):
        return self.taux*super().solde()    

    
ce = CompteEpargne(1,"ahol","moha",500,4555,"Monastir",0.5)    
print(ce.calculInteret())






