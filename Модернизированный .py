#modern
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

print("операции")
print("1:сложение")
print("2:вычитание")
print("3:умножение")
print("4:деление")

operation = input("выберите операцию: ")

if operation == "1":
    result = num1 + num2 + num3
    print(result)
elif operation == "2":
    result = num1 - num2 - num3
    print(result)
elif operation == "3":
    result = num1 * num2 * num3
    print(result)
elif operation == "4":
    result = num1 / num2 / num3
    if num2 != 0:
        print(result)
    else: 
        print("ZeroDivisionError")
else:
    print("неверные числа")
