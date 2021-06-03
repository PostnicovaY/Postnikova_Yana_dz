import sys
import os

if sys.argv == [os.path.basename(__file__)]:
    print("Нет аргументов")
    exit(1)
elif len(sys.argv) < 2:
    print("Недостаточно аргументов")
    exit(1)
else:
    with open("data.csv", "a", encoding="UTF-8") as file:
        file.write(f'\n{sys.argv[1].split(",")[0]},{sys.argv[1].split(",")[1]}')