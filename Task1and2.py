import requests
import re

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
logs_path = "logs.txt"
ip_data_path = "ip_data.txt"


def get_data(url, logs):
    # Эта функция получает логи с url и записывает их в файл

    # Отправляем GET запрос на url, получаем данные в потоке
    response = requests.get(url, stream = True)

    # открыть (или создать, если не существует) файл журнала в режиме записи.
    # ВНИМАНИЕ! Мы пишем файл в байтовом режиме, потому что в ответ получаем данные в байтах
    with open(logs, "wb") as file:
        # В цикле выкидываем в ответ все строчки
        for line in response.iter_lines():
            # Записываем данные в файл журнала и добавляем символ новой строки в конце каждой записанной строки
            file.write(line + b"\n")

    # Используем выше "with" для закрытия файла после окончания блока
    print("Logs are loaded\n") # Вывод делаю, чтобы проверить, загрузился ли файл

def clear_data(path, line_number):
    with open("temp.txt", "w") as temp, open(path, "r") as file:
        # индекс - счетчик. Он содержит текущий номер строки
        index = 0

        # Зацикливаемся на заданном файле
        for line in file:
            # Если номер текущей строки равен заданному, мы пишем заданную новую строку, иначе мы просто записываем строки из файла (надеюсь, понятно написала)
            if line_number > index:
                temp.write(line)
            else:
                break
            index += 1
    # Здесь мы записываем данные из временного файла в заданный
    with open("temp.txt", "r") as temp, open(path, "w") as file:
        for line in temp:
            file.write(line)

def get_ip(record):
    # Эта функция анализирует данные и возвращает ip из этих данных, если он существует, или возвращает None в других случаях
    # Данные представляют собой одну строку из файла журнала. Пример:
    # 80.91.33.133 - - [17 / May / 2015: 08: 05: 14 +0000] "GET / downloads / product_1 HTTP / 1.1" 304 0 "-" "Debian APT-HTTP / 1.3 (0.8.16 ~ exp12ubuntu10. 16) "

    # Сначала составляем шаблон поиска. IP находится в первой группе ([0-9] {1,3} \.) {3} [0-9] {1,3}).
    # ([0-9] {1,3} \.) - ищет 1-3 цифры, за которыми следует точка. {3} после поиска 3 таких групп.
    # И этот [0-9] {1,3} ищет 1-3 цифры в конце IP-адреса

    pattern = re.compile(r'(([0-9]{1,3}\.){3}[0-9]{1,3}) - - \[.+] \"([A-Z]{3}) ((/.+]*)+) (HTTP|HTTPS).*')

    # Ищем совпадения в данной записи
    soup = re.match(pattern, record)

    # если совпадения найдены, возвращаем IP, иначе возвращаем None
    if soup:
        return soup.group(1)
    else:
        return None


def file_rewrite(path, line_number, new_line):
    # Эта функция перезаписывает одну строку в файле следующим образом:
    # 1) Создаем временный файл со всеми данными, кроме строки, которую мы должны изменить
    # 2) Переписываем старый файл, используя данные из временного файла


    # Здесь открываем оба файла, если временный файл не существует, функция open создаст его из-за режима "w"
    with open("temp.txt", "w") as temp, open(path, "r") as file:
        # индекс - счетчик. Он содержит текущий номер строки (как писала выше)
        index = 0

        # Зацикливаемся на заданном файле
        for line in file:
            # Если номер текущей строки равен заданному, мы пишем заданную новую строку, иначе мы просто записываем строки из файла
            if line_number == index:
                temp.write(new_line)
            else:
                temp.write(line)
            index += 1
    # Здесь мы записываем данные из временного файла в заданный
    with open("temp.txt", "r") as temp, open(path, "w") as file:
        for line in temp:
            file.write(line)


def add_line(path, new_line):
    # Простой код для добавления новой строки в файл. Точка находится в режиме "а" в открытой функции
    with open(path, "a") as file:
        file.write(new_line)


def find_ip(path, ip):
    # Эта функция ищет данный ip в данном файле.
    # Возвращает номер строки, в которой был найден ip, и саму строку

    # файл с ip данными создать нельзя, поэтому весь код делаем в блоке try
    try:
        # Открыть файл, указанный в режиме чтения:
        with open(path, "r") as file:
            index = 0

            # Цикл через файл. Каждая строка выглядит как 123.456.789.012 12\n
            for line in file:
                # Итак, мы разбиваем его пробелом и проверяем первую часть
                if ip == line.split(" ")[0]:
                    # Вернуть номер строки и саму строку без символа новой строки
                    return index, line[:-1]
                # В противном случае просто увеличиваем индекс
                index += 1
            return None
    except IOError:
        return None

# Здесь мы получаем данные
get_data(url, logs_path)

# Здесь мы удаляем некоторые данные для проверки ...
clear_data(logs_path, 1000)

# Очищаем наш файл ip_data, чтобы счетчик был 0
with open(ip_data_path, "w") as ip_data:
    ip_data.write("")

# Открывать сохраненные данные, перебирая строки
with open(logs_path) as logs:
    i = 0
    for log in logs:
        # Получаем ip и сохраняем его
        ip = get_ip(log)
        # Находим этот ip в файле ip_data
        record = find_ip(ip_data_path, ip)
        # Если не найден, добавьте его туда со счетчиком 1 (потому что этот IP встречается впервые)
        if record is None:
            add_line(ip_data_path, f'{ip} 1\n')
        # Если IP найден, увеличиваем счетчик на единицу и перезаписываем файл
        else:
            # record [1] - строка, возвращаемая функцией find_ip.
            # Разделяем его пробелом и получаем второй элемент полученного списка.
            # Преобразовываем строковый тип в int
            count = int(record[1].split(' ')[1])

            # record [0] - содержит номер строки, f'{ip} {count + 1}\n' - новая строка, которая будет записана
            file_rewrite(ip_data_path, record[0], f'{ip} {count + 1}\n')
        i += 1
print(f'{i} logs checked')
# Теперь у нас есть файл ip_data, который содержит все IP-адреса из журналов, и каждая реализация IP в журналах считается
# Теперь ищим спамера:
with open(ip_data_path) as ip_data:
    max_count = 0
    result_ip = ""
    # Для каждого ip в ip_data
    for record in ip_data:
        # Парсим данные из строки
        [ip, count] = record[:-1].split(" ")
        # если его счетчик больше чем max - сохраняем его и ip
        if int(count) > max_count:
            max_count = int(count)
            result_ip = ip
    print(f"User with this IP {result_ip} is spammer! He has sent {max_count} requests!")

# Напишите мне, нормально ли, что комментарии на русском, или надо их на английский переводить?