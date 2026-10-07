#1
#  Save a book list
# Напишите функцию save_books(books).
# Функция принимает список строк и создаёт файл books.txt, в который сохраняет названия книг.
# Каждая книга должна быть записана с новой строки.
# Пример:
# books = [
#  	"Harry Potter",
#  	"The Hobbit",
#  	"1984",
#  	"The Little Prince"
#  ]
#
#  save_books(books)
# После выполнения программы файл books.txt должен выглядеть так:
# Harry Potter
#  The Hobbit
#  1984
#  The Little Prince
# Используйте:
# ·       with open(...)
# ·       режим "w"
# ·       цикл for

def save_books(books):
  with open("books.txt","w",encoding="utf-8") as file:
   for book in books:
       file.write(book + "\n")
books = [
 "Harry Potter",
 "The Hobbit",
 "1984",
 "The Little Prince"
]
print(save_books(books))

#2
# Read data from a CSV file
# Создайте файл products.csv со следующим содержимым:
# product,price
#  Coffee,25
#  Tea,18
#  Chocolate,12
# Напишите функцию:
# read_products(filename)
# Функция должна прочитать данные из файла и вывести информацию в следующем формате:
# Product: Coffee (25)
#  Product: Tea (18)
#  Product: Chocolate (12)
# Используйте:
# csv.DictReader()

import csv

def read_products(filename):
    with open("product_csv.csv","r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")
read_products("product_csv.csv")

#3
# Save user information to a JSON file
# Напишите функцию:
# save_user(username, email, country)
# Функция должна создать файл user.json и сохранить в него информацию о пользователе.
# Пример вызова:
# save_user("anna21", "anna@example.com", "Israel")
# Ожидаемое содержимое файла user.json:
# {
#  	"username": "anna21",
#  	"email": "anna@example.com",
#  	"country": "Israel"
#  }
# Используйте:
# ·       словарь dict
# ·       json.dump()

import json
def save_user(username, email, country):
    user = dict(
        username=username,
        email=email,
        country=country
    )
    with open("user.json", "w",encoding="utf-8") as file:
        json.dump(user, file, indent=2)
save_user("anna21", "anna@example.com", "Israel")



#4
# Напишите функцию:
# create_logs_folder()
# Функция должна:
# 1.     Создать папку logs.
# 2.     Создать внутри неё файл app.txt.
# 3.     Записать в файл строку:
# Application started successfully!
# Используйте:
# ·       pathlib.Path
# ·       mkdir()
# ·       with open(...)
# General Requirements
# ·       Используйте encoding='utf-8' при работе с текстовыми файлами.
# ·       Проверьте работу каждой функции на примерах из задания.
# ·       Используйте названия функций, указанные в задании.
# ·       Код должен быть читаемым и аккуратно оформленным.
# ·       После выполнения программы проверьте содержимое созданных файлов.


