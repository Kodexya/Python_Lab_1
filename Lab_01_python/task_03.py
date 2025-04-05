# Задание 3

# Запрашиваем число n у пользователя
n = int(input("Введите число n: "))

# Выводим все числа от n до 1 в обратном порядке
print("Числа от n до 1:")
current = n
while current >= 1:
    print(current)
    current -= 1

# Вычисляем факториал числа n
factorial = 1
current = 1
while current <= n:
    factorial *= current
    current += 1

# Выводим факториал
print(f"Факториал числа n: {factorial}")