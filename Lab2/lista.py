import sys
from collections import OrderedDict, Counter

global lista
lista = []

def wypisz():
    fin = ""
    ocurs = OrderedDict(Counter(lista))
    for num, oc in sorted(ocurs.items()):
        fin += ''.join(str("{}:{},".format(num, oc)))
    return fin

def zapisz(arg):
    # lista.append(arg)
    for num in arg:
        lista.append(int(num))

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        zapisz(int(arg))

    print(wypisz())