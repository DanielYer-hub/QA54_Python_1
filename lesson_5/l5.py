def save_shopping_list(items):
    with open("shopping_list.csv","w",encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")
items = [
    "Milk",
    "Bread",
    "Apples",
    "Coffee"
]
save_shopping_list(items)

with open("shopping_list.csv","r",encoding="utf-8") as file:
    print(file.read())


#2
def read_students(filename):
    with open("students.csv","r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student:{row['name']}({row['age']})")
read_students("students.csv")




