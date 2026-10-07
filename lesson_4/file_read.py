with open("user.txt","w",encoding="utf-8")as file:
    file.write("Daniel\n ")
    file.write("Max\n ")

    # read()- весь файл полностью
with open("user.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(len(content))

#readlines() возырват списка где каждый элемент отдельная строка
with open("user.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip())
    print()

#for
with open("user.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())