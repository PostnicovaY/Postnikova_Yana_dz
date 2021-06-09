import requests
import re

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
logs_path = "logs.txt"
ip_data_path = "ip_data.txt"


def get_data(url, logs):
    response = requests.get(url, stream=True)

    with open(logs, "wb") as file:
        for line in response.iter_lines():
            file.write(line + b"\n")

    print("Logs are loaded\n")


def clear_data(path, line_number):
    with open("temp.txt", "w") as temp, open(path, "r") as file:
        index = 0

        for line in file:
            if line_number > index:
                temp.write(line)
            else:
                break
            index += 1
    with open("temp.txt", "r") as temp, open(path, "w") as file:
        for line in temp:
            file.write(line)


def parse_data(record):
    pattern = re.compile(
        r"(([0-9]{1,3}\.){3}[0-9]{1,3}) - - \[(.+)] \"([A-Z]+) (/.+) (HTTP|HTTPS)/1\.[0-9]\" ([0-9]{3}) ([0-9]+) \".*")

    # ищем совпадения с помощбю шаблона
    soup = re.match(pattern, record)
    # И если они есть, вынимаем нужные данные
    if soup:
        return soup.group(1), soup.group(3), soup.group(4), soup.group(5), soup.group(6), soup.group(7), soup.group(8)
    else:
        print(record)
        return None


def add_line(path, new_line):
    # Простой код для добавления новой строки в файл
    with open(path, "a") as file:
        file.write(new_line)


# Получаем логи
get_data(url, logs_path)

# Часть удаляем, ибо их много
clear_data(logs_path, 1000)

# Чистим файл с ответом
with open(ip_data_path, "w") as ip_data:
    ip_data.write("")

# Открываем файл с логами и проверяем каждую строку
with open(logs_path) as logs:
    i = 0
    parsed_data = []
    for log in logs:
        # Парсим строку
        temp = parse_data(log)
        if temp is None:
            i += 1
            continue
        else:
            parsed_data.append(temp)
            add_line(ip_data_path, "(" + " ".join(f"'{str(e)}', " for e in temp).strip()[:-1] + ")")

        i += 1
print(f'{i} logs checked')
print(parsed_data)
