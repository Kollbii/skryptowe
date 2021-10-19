import sys, lista, slownik

if __name__ == "__main__":
    args = sys.argv[1:]

    if args[0] == "--lista":
        lista.zapisz(args[1:])
        print(lista.wypisz())
    elif args[0] == "--slownik":
        slownik.zapisz(args[1:])
        print(slownik.wypisz())
    else:
        print("Avalible options: --lista --slownik")

# >$ python skrypt3.py --lista 1 1 3 1 23 23 45
# >$ python skrypt3.py --slownik 1 1 3 1 23 23 45