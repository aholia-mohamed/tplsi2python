def inverse(chaine):
    ch=chaine[::-1]
    print(ch)

def inverse_mot(chaine):
    result=""
    liste_chaine=chaine.split(" ")
    for elt in liste_chaine:
        result=elt+" "+result
    print(result)

inverse("bonjour")
inverse_mot("bonsoir la bas")