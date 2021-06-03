import sys
import os

if sys.argv == [os.path.basename(__file__)]:
    with open("data.csv", "r", encoding="UTF-8") as file:
        for line in file:
            print(line.rstrip('\n'))
else:
    with open("data.csv", "r", encoding="UTF-8") as file:
        i = 1
        while i < int(sys.argv[1]):
            file.readline()
            i += 1

        if len(sys.argv) > 2:
            while i < int(sys.argv[2]):
                print(file.readline().rstrip('\n'))
                i += 1
        else:
            for line in file:
                print(line.rstrip('\n'))