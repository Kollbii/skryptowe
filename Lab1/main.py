from fractions import Fraction

def sum(arg1, arg2):
    if type(arg1) is complex or type(arg2) is complex:
        return complex(arg1.real + arg2.real, arg1.imag + arg2. imag)
    
    if type(arg1) is Fraction or type(arg2) is Fraction:
        return Fraction(arg1 + arg2)

    return float(arg1) + float(arg2)

if __name__ == '__main__':
    print(sum(3.0, -1))
    print(sum(Fraction(11, 35), Fraction(24, 35)))
    print(f"__name__ = {__name__}")