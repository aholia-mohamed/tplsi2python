
def dict_ch(chaine):

    dicto={}

    for c in chaine:
        if not dicto.get(c):
            dicto[c]=chaine.count(c)

    return dicto    

d=dict_ch("programme")  
print(d)  