from inspect import signature

def argumenty(root_args): # Get root args
    def decoratorFunc(suma): # Get function
        def wrap(*args, **kwargs): # Get inserted args
            nums = [arg for arg in args]
            # print(nums, root_args, suma.__code__.co_argcount, len(list(signature(suma).parameters)))

            if len(nums) + len(root_args) < len(list(signature(suma).parameters)): # -1 cuz it counts `self`
                raise TypeError("Za ma argumentow")

            c = 0
            while len(nums) < len(list(signature(suma).parameters)):
                nums.append(root_args[c])
                c += 1
            
            suma(*nums)

            # Return if not assigned
            try:
                return root_args[c]
            except IndexError:
                return None

        return wrap
        
    return decoratorFunc

class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        print("%d+%d+%d=%d" % (a,b,c,a+b+c))
    
    def sumaNon(self, a, b, c):
        print("%d+%d+%d=%d" % (a,b,c,a+b+c))

    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        print("%d-%d=%d" % (x,y,x-y))

    def roznicaNon(self, x, y):
        print("%d-%d=%d" % (x,y,x-y))

    def __setitem__(self, name, value):
        if name == "suma":
            self.argumentySuma=value
            self.suma = argumenty(self.argumentySuma)(self.sumaNon)
        if name == "roznica":
            self.argumentyRoznica=value
            self.roznica = argumenty(self.argumentyRoznica)(self.roznicaNon)

# op=Operacje()
# op.suma(1,2,3) #Wypisze: 1+2+3=6
# op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
# op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
# # op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
# op.roznica(2,1) #Wypisze: 2-1=1
# op.roznica(2) #Wypisze: 2-4=-2
# wynik=op.roznica() #Wypisze: 4-5=-1
# print(wynik) #Wypisze: 6

# # #Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
# op['suma']=[1,2]
# # # #oznacza, że   argumentySuma=[1,2]
# print(op.argumentySuma)
# op.suma(1) #Wypisze: 1+1+2=4 

# # # #Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
# op['roznica']=[1,2,3]
# # # #oznacza, że   argumentyRoznica=[1,2,3]
# print(op.argumentyRoznica)
# op.roznica(1)