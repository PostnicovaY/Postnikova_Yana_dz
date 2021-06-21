class Sklad:
    name = 'Главный'
    data = {
        'printers': {
            'amount': 0,
            'list': []
        },
        'scanners': {
            'amount': 0,
            'list': []
        },
        'kseroks': {
            'amount': 0,
            'list': []
        },
        'orgtechnic': {
            'amount': 0,
            'list': []
        },
    }

    def __str__(self):
        return self.name + ':\n' + '{\n' + ''.join(f'\t{key}: {self.data[key]}\n' for key in self.data.keys()) + '}'

    def __init__(self, name):
        self.name = name

    def add_technic(self, o):
        self.data[o.type_str()].amount += 1
        self.data[o.type_str()].list.append(o)

    def check_technic(self, o):
        if o in self.data[o.type_str()].list:
            return True
        else:
            return False

class Orgtechnic:
    model = ''
    is_color = False
    is_wifi = False

    def __init__(self, model, is_color, is_wifi):
        self.model = model
        self.is_wifi = is_wifi
        self.is_color = is_color

    def __str__(self):
        return f'{self.model}:\n' \
               f'\t{("Черно-белый", "Цветной")[self.is_color]}\n' \
               f'\tWifi {("отсутствует", "в наличии")[self.is_wifi]}\n'

    def type_str(self):
        return 'orgtechnic'

class Printer(Orgtechnic):
    is_laser = False

    def __init__(self, model, is_color, is_wifi, is_laser):
        self.model = model
        self.is_wifi = is_wifi
        self.is_color = is_color
        self.is_laser = is_laser

    def __str__(self):
        f'{self.__str__()}'
        f'{("Струйный", "Лазерный")[self.is_laser]}\n'

    def type_str(self):
        return 'printers'

class Scanner(Orgtechnic):
    is_auto = False

    def __init__(self, model, is_color, is_wifi, is_auto):
        self.model = model
        self.is_wifi = is_wifi
        self.is_color = is_color
        self.is_auto = is_auto

    def __str__(self):
        f'{self.__str__()}'
        f'{("Нет автоподачи", "Есть автоподача")[self.is_auto]}\n'

    def type_str(self):
        return 'scanners'

class Kseroks(Orgtechnic):
    max_copies = '99'

    def __init__(self, model, is_color, is_wifi, max_copies):
        self.model = model
        self.is_wifi = is_wifi
        self.is_color = is_color
        self.max_copies = max_copies

    def __str__(self):
        f'{self.__str__()}'
        f'Максимальное кол-во копий за цикл: {self.max_copies}\n'

    def type_str(self):
        return 'kseroks'