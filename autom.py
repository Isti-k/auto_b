from Auto import Auto

def fajlbeolvasas():
    kocsik=[]
    fajl=open("auto.txt","r",encoding="utf-8")
    fajl.readline()
    lista=fajl.readlines()
    fajl.close()

    for i in range(0,len(lista),1):
        aktsor=lista[i].strip().split("$")
        auto=Auto(aktsor[0],aktsor[1])
        kocsik.append(auto)

    return kocsik

def tabla(lista,i):
    print(f"{lista[i].nev}: {len(lista[i].nev)} hosszú.")

def kiir(lista,i):
    fajl=open("kiir.txt","w",encoding="utf-8")
    fajl.write("kiir.txt")
    fajl.close()

def flotta(lista):
    print(f"{len(lista)} hosszú.")

