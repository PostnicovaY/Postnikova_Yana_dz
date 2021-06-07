import os

config_path = r'config.yaml'

def how_many_tabs(a):
    return len(a) - len(a.lstrip())

def recursive_bypass(data, cur):
    # 1) Создаем словарь, значение строки - ключ, все что дальше значение
    # 2) Если : создаем словарь, ключ - значение строки, значение - список, читаем значения до тех пор пока количество табов не равно количество табов в ключе + 1
    # 3) Иначе добавить элемент в список

    key_tabs = how_many_tabs(data[cur])
    key = data[cur].strip()[2:-1]
    value = []
    cur += 1
    while cur < len(data) and how_many_tabs(data[cur]) == key_tabs + 3:
        if ':' in data[cur]:
            (new_value, cur) = recursive_bypass(data, cur)
            value.append(new_value)
        else:
            value.append(data[cur].strip()[2:])
            cur += 1

    return {key: value}, cur

def file_to_list():
    result = []
    with open(config_path, 'r') as config_file:
        for line in config_file:
            result.append(line.rstrip())
    return result

def recursive_creation(dict, path):
    key = list(dict.keys())[0]
    path = os.path.join(path, key)
    try:
        os.mkdir(path)
        for obj in dict[key]:
            if type(obj) == str:
                temp = open(os.path.join(path, obj), 'w+')
                temp.close()
            else:
                recursive_creation(obj, path)
    except:
        print('Такой объект уже есть!')

data = file_to_list()

(parsed_data, cur) = recursive_bypass(data, 0)
recursive_creation(parsed_data, os.path.abspath(os.path.dirname(__file__)))