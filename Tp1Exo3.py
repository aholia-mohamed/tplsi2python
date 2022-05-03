def saisir():
    longueur_entier=0
    nombre_entier=0
    while not longueur_entier == 3:
        nombre_str=input("entrer un entier de 3 chiffres: ")
        longueur_entier=len(nombre_str)
        
    try:
        nombre_entier=int(nombre_str)
    except:
        print("ERROR!!!! vous devez entrer un nombre entier")
        return saisir()
    return nombre_entier

def cubique(nombre): 
    nombre_entier=nombre 
    result=0

    for c in str(nombre_entier):
        result+=pow(int(c),3 )
    if result == nombre_entier:
        return True
    
    return False

def nbr_cubique():

    list_cubique=[]

    for i in range(100,1000):
        if cubique(i):
            list_cubique.append(i)

    print(list_cubique)
        
nbr_cubique()    