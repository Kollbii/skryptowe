import getopt, sys, lista, slownik

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "x", ['modul='])

    if opts[0][1] == "lista":
        lista.zapisz(args[1:])
        print(lista.wypisz())
    elif opts[0][1] == "slownik":
        slownik.zapisz(args[1:])
        print(slownik.wypisz())
    else:
        print("Avalible options for --modul= [ lista, slownik]")

# >$ python skrypt3.py --modul=lista 1 1 3 1 23 23 45
# >$ python skrypt3.py --modul=slownik 1 1 3 1 23 23 45
