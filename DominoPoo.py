from random import *

class Piece:

    def __init__(self,val1,val2):
        self.__cote1=val1
        self.__cote2=val2

    def somme_points(self):
        return self.__cote1+self.__cote2

    def a_valeur(self,val):
        if val==self.__cote1 or val==self.__cote2:
            return True
        return False             

    def __repr__(self):
        return f"Domino(coté 1: {self.__cote1} | coté 2: {self.__cote2})"  

    def get_cote1(self):
        return self.__cote1

    def get_cote2(self):
        return self.__cote2    

class Dominos:

    def __init__(self):
        self.__data=[]
        for i in range(28):
            cote1=randint(0,6)
            cote2=randint(0,6)
            self.__data.append(Piece(cote1,cote2))

    def get_data(self):
        return self.__data        
            
    def melanger_pieces(self):
        for i in range(len(self.__data)):
            self.__data[i],self.__data[randint((i+1), len(self.__data))]= self.__data[randint((i+1), len(self.__data))],self.__data[i]
    
    def retirer_piece(self):
        return self.__data.pop()





dominos=Dominos()      
print(dominos.get_data())
print(dominos.retirer_piece())
print(dominos.get_data())




           
