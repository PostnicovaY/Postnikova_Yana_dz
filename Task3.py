import re


class ListError(Exception):
    err = 'Вы ввели не числа'

    def __str__(self):
        return self.err

    @staticmethod
    def is_number(s):
        pattern = r'[+-]?[0-9]+(\.[0-9]+)?'
        if re.match(pattern, s) is None:
            return True
        else:
            raise ListError


l = []
s = ''
while True:
    s = input()
    try:
        if s == 'stop':
            break
        if ListError.is_number(s):
            l.append(float(s))
    except ListError as err:
        print(err)

print(l)
list.py