import sys
import os


def get_path():
    if sys.argv == [os.path.basename(__file__)]:
        return 'users.csv', 'hobby.csv', 'result.csv'
    elif len(sys.argv) <= 3:
        return None
    else:
        return (os.path.realpath(sys.argv(i)) for i in range(1, 3))

pathes = get_path()
(users_path, hobby_path, result_path) = pathes
if pathes is None:
    print('Недостаточно аргументов')
    exit(0)
try:
    with open(users_path, "r", encoding="UTF-8") as users, open(hobby_path, "r", encoding="UTF-8") as hobbies, open(
            result_path, "w", encoding="UTF-8") as result:
        for user in users:
            hobby = hobbies.readline()
            if hobby:
                result.write(f'({user[:-1].replace(","," ")},{hobby[:-1].split(",")})\n')
            else:
                result.write(f'({user[:-1]},None)\n')
        if hobby:
            exit(1)
except:
    print('Файл не существует!')