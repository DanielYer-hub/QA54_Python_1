# 1.Напишите три функции
# 1.1 save_test_ids(test_ids) — принимает список ID тестов и сохраняет их в tests.txt. Каждый ID должен находиться на отдельной строке.
# 1.2  add_test_id(test_id) — добавляет один новый ID в конец существующего файла, не удаляя предыдущие записи.
# 1.3  load_test_ids(filename) — читает файл и возвращает список ID. Пустые строки нужно пропускать, пробелы по краям удалять.
# Пример исходного списка->["QA-1001", "QA-1002", "QA-1003"]
# После вызова add_test_id("QA-1004") функция load_test_ids("tests.txt") должна вернуть:
# ["QA-1001", "QA-1002", "QA-1003", "QA-1004"]
# Используйте: def, return, for, list, append(), with open(), режимы w, a, r, strip().
# Проверьте пустой список, повторное добавление записи и чтение файла с пустыми строками.
import csv
import json


def save_test_ids(test_ids):
    with open("tests.txt", "w", encoding="utf-8") as file:
        for test_id in test_ids:
            file.write(test_id + "\n")
test_ids = ["QA-1001", "QA-1002", "QA-1003"]
save_test_ids(test_ids)

def add_test_id(test_id):
    with open("tests.txt","a",encoding="utf-8") as file:
            file.write(test_id + "\n")
add_test_id("QA-1004")

def load_test_ids(filename):
    test_ids = []
    with open("tests.txt","r",encoding="utf-8") as file:
        for line in file:
            test_id = line.strip()
            # if test_id:
            test_ids.append(test_id)
        return test_ids
result = load_test_ids("tests.txt")
print(result)

# 2.Создайте файл results.csv test_id,status,duration_ms
# QA-1001,PASSED,120
# QA-1002,FAILED,230
# QA-1003,PASSED,150
# Напишите функцию get_test_statistics(filename)
#
# Функция должна:
# 1.Прочитать данные из CSV.
# 2.Посчитать общее количество тестов.
# 3.Посчитать количество PASSED и FAILED.
# 4.Найти суммарное время выполнения тестов в миллисекундах.
# 5.Собрать в список ID всех пров…
#Read more
# {
#     "total": 3,
#     "passed": 2,
#     "failed": 1,
#     "total_duration_ms": 500,
#     "failed_ids": ["QA-1002"]
# }
# Используйте: csv.DictReader(), for, if, dict, list, int(), append(), return.
# Считайте, что в корректном входном файле статусы могут быть только PASSED и FAILED, а время — целое неотрицательное число.
# Дополнительно проверьте файл, содержащий только заголовки. Все счётчики должны быть равны нулю, список ошибок — пустой.

def get_test_statistics(filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []
    with open("results.csv","r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total +=1
            total_duration_ms += int(row["duration_ms"])
            if row["status"] == "PASSED":
                passed += 1
            if row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])
        statistics = {
            "total": total,
            "passed": passed,
            "failed": failed,
            "total_duration_ms": total_duration_ms,
            "failed_ids": failed_ids
        }
        return statistics
result = get_test_statistics("results.csv")
print(result)

# 3. Напишите две функции:
# •save_test_config(environment, base_url, timeout) — создаёт config.json и сохраняет параметры тестового окружения.
# •load_test_config(filename) — читает JSON и возвращает словарь с настройками.
# Пример вызова
# save_test_config(
#     "staging",
#     "https://example.com",
#     30
# )
# Ожидаемый JSON {
#     "environment": "staging",
#     "base_url": "https://example.com",
#     "timeout": 30
# }
# 1.Для сохранения используйте json.dump().
# 2.Для чтения используйте json.load().
# 3.Сохраняйте данные с отступами для удобного чтения.
# 4.Проверьте, что после загрузки тип timeout остаётся int.
# 5.Проверьте, что повторное сохранение заменяет старую конфигурацию.
# Используйте: dict, json.dump(), json.load(), with open(), type(), assert

def save_test_config(environment, base_url, timeout):
    test_config = {
        "environment":environment,
        "base_url":base_url,
        "timeout":timeout
    }
    with open("config.json","w",encoding="utf-8") as file:
        json.dump(test_config,file,indent=4)
save_test_config("staging","https://example.com",30)

def load_test_config(filename):
    with open("config.json","r",encoding="utf-8") as file:
        config = json.load(file)
    return config
print(load_test_config("config.json"))





