import sys

try:
    print(sys.argv[1])

except IndexError:
    print("Zapomniałeś podać nazwę pliku")

with open(sys.argv[1]) as f:
    i = 0
    for line in f:
        print(i, line, end="")
        i += 1

