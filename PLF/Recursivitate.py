class Nod:
    def __init__(self, e):
        self.e = e
        self.urm = None


class Lista:
    def __init__(self):
        self.prim = None


def creareLista():
    lista = Lista()
    lista.prim = creareLista_rec()
    return lista


def adaugaInceput(lista, e):
    nod = Nod(e)
    nod.urm = lista.prim
    lista.prim = nod;
    return lista


from copy import deepcopy


def sublista(lis):
    lista = deepcopy(lis)
    if eVida(lista) == True:
        return None
    else:
        lista.prim = lista.prim.urm
        return lista


def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.urm = creareLista_rec()
        return nod


def primElem(lista):
    return lista.prim.e


def eVida(lista):
    if lista.prim == None:
        return True
    else:
        return False


def tipar(lista):
    if lista == None or primElem(lista) == None:
        print("Lista vida")
    else:
        tipar_rec(lista.prim)


def tipar_rec(nod):
    if nod != None:
        print(nod.e)
        tipar_rec(nod.urm)


def adaugaSfarsit(lista,elem):
    if eVida(lista):
        lista = Lista()
        lista.prim = Nod(elem)
        return lista

    subLista = sublista(lista)
    return adaugaInceput(adaugaSfarsit(subLista, elem),primElem(lista))


def concatenare(lis1, lis2):
    if eVida(lis1) == False:
        sub = sublista(lis1)
        return adaugaInceput(concatenare(sub, lis2), primElem(lis1))

    if eVida(lis2) == False:
        sub = sublista(lis2)
        return adaugaInceput(concatenare(lis1, sub), primElem(lis2))

    return Lista()

def main():
    list = creareLista()

    tipar(adaugaSfarsit(list, 10))

    print("Introduceti elementele primei liste")
    lista1 = creareLista()
    print("Introduceti elementele celei de-a doua liste")
    lista2 = creareLista()

    tipar(concatenare(lista1, lista2))

main()

