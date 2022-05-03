def saisir_taille():
    nombre_str="0"
    nombre_entier=0
    while not 5<=int(nombre_str)<=50:
        nombre_str=input("Entrer la taille de la liste (comprise entre 5 et 50) : ")
    try:
        nombre_entier=int(nombre_str)
    except:
           print("ERROR!!! Vous devez entrer un nombre entier")   
           return saisir_taille()  
    return nombre_entier

def saisir_elements_list(indice):
    nombre_entier=0
    nombre_str=input("Entrer l'element numéro "+str(indice+1)+" : ")
    try:
        nombre_entier=int(nombre_str)
    except:
           print("ERROR!!! Vous devez entrer un nombre entier")   
           return saisir_elements_list(indice)  
    return nombre_entier


def somme():
    initial_list=[]
    final_list=[]
    result=0
    n=saisir_taille()
    for i in range(n):
        element=saisir_elements_list(i)  
        initial_list.append(element)
    for elt in initial_list:
        result+=elt
        final_list.append(result)
    result=0
    return final_list

liste=somme()
print(liste)

    
       