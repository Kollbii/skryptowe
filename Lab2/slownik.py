import sys
from collections import OrderedDict, Counter

global slownik
slownik = {}

def wypisz():
    fin = ""
    ocurs = OrderedDict(Counter(slownik))
    for num, oc in sorted(ocurs.items()):
        fin += ''.join(str("{}:{},".format(num, oc)))
    return fin

def zapisz(arg):
    for num in arg:
        try:
            slownik[int(num)] += 1
        except KeyError:
            slownik[int(num)] = 1

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        zapisz(int(arg))

    print(wypisz())