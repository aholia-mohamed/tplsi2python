def admis(liste):
    final_list=[]
    list_non_admis=[]
    list_premier=[]
    moyenne=0
    for c in liste:
        if c[1] >=10:
            list_non_admis.append(c[0])
        moyenne+=c[1]   
    final_list.append(tuple(list_non_admis))

    max=liste[0][1]
    indice=0         
    for i in range(len(liste)):   
        if max<liste[i][1]:
            indice=i
    list_premier.append(liste[indice]) 
    final_list.append(tuple(list_premier))

    final_list.append(moyenne/len(liste))
    print(final_list)


admis([("mohamed",16), ("amine", 8), ("zied",12), ("zara", 18)])