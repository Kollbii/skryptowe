import sys

def is_prime(num):
    try:
        num = int(num)
        if num < 1:
            return False

        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True
    except:
        return False

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if is_prime(arg):
            print(arg)

# $> python .\skrypt.py 1 23 10 13 0 2 -101 text -99
