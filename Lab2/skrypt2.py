import re, sys

def extract(text: str):
    for num in re.findall('[-]?[0-9]+', text):  # [0-9]+ - All single digits. 
        yield int(num)
    # for string in re.findall('[^-\s+0-9][a-zżźćńąśłęóA-ZŻŹĆŃĄŚŁĘÓ]+', text):
    for string in re.findall('[^\W|^\d|^\s+]+', text):  # Testing from left to right '|'. \W == [^a-zA-Z0-9_]. \d - any digits. \s matches white space like [ \t\n\r\f\v]
        yield str(string).strip()

def start():
    while True:
        try:
            for element in extract(str(sys.stdin.readline())):
                if type(element) == int:
                    print("\tLiczba: {}".format(element))
                elif type(element) == str:
                    print("\tWyraz: {}".format(element))
        except KeyboardInterrupt:
            print("Error/Exit msg")
            break

if __name__ == "__main__":
    start()