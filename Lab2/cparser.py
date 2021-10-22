import re, sys, getopt


def getString(file):
    f = open(file, "r")
    return f.read()

def parseOneLine(file):
    coms = "// "
    func = "Functions found: "
    for line in re.findall('\/\*[\w\n\s]+\*\/', getString(file)):
        for l in line.split('\n'):
            ch = l.strip()
            if ch not in ['/*','*/']:
                coms += ''.join(str(ch + " "))
    coms += '\n'
    for line in re.findall('[int|void|char|short|unsigned|long|float|double]\s\w+\s\(', getString(file)):
        func += ''.join(str(line[2:-2] + "() "))
    print(coms)
    print(func)

def parseEachLine(file):
    coms = ""
    func = ""
    for line in re.findall('\/\*[\w\n\s]+\*\/', getString(file)):
        for l in line.split('\n'):
            ch = l.strip()
            if ch not in ['/*','*/']:
                coms += ''.join(str("\n//" + ch))

    for line in re.findall('[int|void|char|short|unsigned|long|float|double]\s\w+\s\(', getString(file)):
        func += ''.join(str("\nFound function " + line[2:-2] + "()"))
    print(coms)
    print(func)


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "x", ['option='])

    file_name = "example.c"

    if opts[0][1] == "nowrap":
        parseOneLine(file_name)
    elif opts[0][1] == "wrap":
        parseEachLine(file_name)
