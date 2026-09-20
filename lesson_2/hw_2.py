#Task1
cart = ["milk", "sold out", "bread", "sold out", "coffee"]
cart = [item for item in cart if item != "sold out"]
print(cart)

#Task2
temp = [21,28,19,31,25,27]
result =[n for n in temp if n>25]
print(result)

result2 = []
for n in temp:
    if n >0:
        result2.append(n)
print(result)

#Task3
def fix_balances(balances):
    for i in range(len(balances)):
        if balances[i] <0:
            balances[i]=0
    return balances
print(fix_balances([120, -30, 50, -5, 0, 200]))

#Task4
def unique_items(items):
    result3 = []
    for item in items:
        if item not in result3:
            result3.append(item)
    return result3
print(unique_items(["red", "blue", "red", "green", "blue"]))

