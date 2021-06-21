class OwnError(Exception):
    err = 'На ноль делить нельзя'

    def __init__(self, text=''):
        self.text = text

    def __str__(self):
        return f'{self.err} {self.text}'


try:
    b = 100
    c = 1
    if c == 0:
        raise OwnError("ЪуЪ")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ответ: {b / c}")