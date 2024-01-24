import random

def veletlen():
    print("A lista:")
    szamok_lista=[]
    for i in range(50):
        szam=random.randint(1,100)
        szamok_lista.append(szam)
        if i < 49:
            print(szam,end=";")
        else:
            print(szam
                  , end=" \n")
    return szamok_lista

def ottel_oszthato(lista):
    db=1
    for i in range(0,len(lista),1):
        if lista[i] % 5 ==0:
            db+=1
    return db


