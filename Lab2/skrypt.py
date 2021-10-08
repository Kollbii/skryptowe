import re

def extract(text: str):
    for num in re.findall('[-]?[0-9]+', text): # [0-9] - All single digits [0-9]+ - sequence of single digits
        yield int(num)
    for string in re.findall('[^-\s+0-9]\D+', text): # \D -> everything but not number. + -> sequence. Optional [^0-9]+. [^\s-] Not white char and dash.
        yield str(string).strip()  # Optional white chars removal

def start():
    while True:
        try:
            text:str = input()
            for element in extract(text):
                if type(element) == int:
                    print("\tLiczba: {}".format(element))
                elif type(element) == str:
                    print("\tWyraz: {}".format(element))
        except:
            print("Error: Could not detect proper input. Exit CTRL + Z")

if __name__ == "__main__":
    start()