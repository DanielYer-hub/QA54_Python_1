# Task1
def clean_name(name):
    return name.strip().title()


print(clean_name("   anna smith   "))
# Anna Smith
print(clean_name("DAVID COHEN"))
# David Cohen
print()


# Task2
def normalize_email(email):
    return email.strip().lower()


print(normalize_email("  Anna.Smith@Example.COM  "))
# anna.smith@example.com
print()


# Task3
def is_python_file(filename):
    return filename.lower().endswith(".py")


print(is_python_file("lesson.py"))
# True
print(is_python_file("HOMEWORK.PY"))
# True
print(is_python_file("notes.txt"))
# False
print()


# Task4
def fix_message(message):
    return message.replace("bad", "good")


message = "bad weather, bad mood"
result = fix_message(message)
print(result)
# good weather, good mood
print(message)
# bad weather, bad mood
message = fix_message(message)
print(message)
print()


# Task5
def count_letter(text, letter):
    return text.lower().count(letter.lower())


print(count_letter("Programming", "g"))
# 2
print(count_letter("Mississippi", "I"))
# 4
print()


# Task6
def create_login(first_name, last_name):
    # first_name = first_name.strip().lower()
    # last_name = last_name.strip().lower()
    #return first_name + "." + last_name
    return f"{first_name.strip().lower()}.{last_name.strip().lower()}"

print(create_login("  Anna ", " SMITH  "))
# anna.smith
print()


# Task7
def split_name(full_name):
    return full_name.strip().split()

print(split_name("  Anna   Smith  "))
# ["Anna", "Smith"]
print()


# Task8
#var1
def check_password(password):
    if len(password)<8:
        return False
    if " " in password:
        return False
    if password.isalpha():
        return False
    return True

print(check_password("python123"))
# True
print(check_password("python"))
# False
print(check_password("python 123"))
# False
print()

#var2
def check_password_1(password):
    if len(password)<8:
        return False
    for char in password:
        if char.isspace():
            return False
        if password.isalpha():
            return False
    return True

print(check_password("python123"))
# True
print(check_password("python"))
# False
print(check_password("python 123"))
# False
print()

#var3
def check_password(password):
    return len(password)>8 and " " not in password and not password.isalpha()


print(check_password("python123"))
# True
print(check_password("python"))
# False
print(check_password("python 123"))
# False
print()