class Date:
    date = '01-01-1970'

    def __init__(self, str):
        self.date = str
        self.day = str.split('-')[0]
        self.month = str.split('-')[1]
        self.year = str.split('-')[2]

    def __str__(self):
        return '{\n' + f'\tday: {self.day}\n\tmonth: {self.month}\n\tyear: {self.year}\n' + '}'

    @classmethod
    def date_to_int(cls, a):
        a.day = int(cls.date.split('-')[0])
        a.month = int(cls.date.split('-')[1])
        a.year = int(cls.date.split('-')[2])

    @staticmethod
    def date_validation(date):
        if type(date.day) is str:
            date.date_to_int()
        if date.day > 31 or date.day < 1 or date.day > 12 or date.day < 1 or date.year < 1970:
            raise ValueError
        else:
            return True

a = Date("16-11-1994")
print(a)
print(Date.date_to_int(a))
print(Date.date_validation(a))
print(type(a.day))