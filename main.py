import jelszo
import oszthato
import autom


"""print("első feladat")
jelszo.jelszo1()"""

print("második feladat")
lista=oszthato.veletlen()
db=oszthato.ottel_oszthato(lista)
print(f"A listában {db} darab öttel osztható szám van.")

auto_lista=autom.fajlbeolvasas()
autom.tabla(auto_lista,1)
print("")
autom.kiir(auto_lista,2)
print("")
autom.flotta(auto_lista)
