#with open("test.txt","w",encoding="utf-8") as file:
# file.write("Hello!")

#file = open("test.txt","w",encoding="utf-8")
#file.write("Hello daniel")
#file.close()

# "r" - read (в существующий файл)
# "w" -write(создает и перезаписывает)
# "a"  append (добавляет в конец не стирая содержимое файла)
# "rb", ""wd" pdf, screenshot

# def log_res(test_name,status):
#     with open("test_1.txt","a",encoding="utf-8") as file:
#         file.write(f"{test_name}: {status}\n")
# log_res("test_register","PASSED")
# log_res("test_login","FAILED")
# log_res("test_logout","PASSED")

def log_res(test_name,status):
    with open("test_1.txt","w",encoding="utf-8") as file:
        file.write(f"{test_name}: {status}\n")
log_res("test_register","PASSED")
log_res("test_login","FAILED")
log_res("test_logout","PASSED")

# def log_res(test_name,status):
#     with open("test_1.txt","a",encoding="utf-8") as file:
#         file.write(f"{test_name}: {status}\n")
# log_res("test_register","PASSED")
# log_res("test_login","FAILED")
# log_res("test_logout","PASSED")