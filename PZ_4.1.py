#Даны два целых числа А и В (А<В). Найти сумму квадратов всех целых чисел от А до В включительно.

A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
if A >= B:
    print("Значение A должно быть меньше B")
else:
    A <= B
    print("Всё верно")


    num = 0

    if num in range(A, B+1):
        num += num**2
        print("Сумма квадратов всех целых чисел от", A, "до", B, "включительно равна")