# Задание 5
import random

# Генерируем список из 20 случайных чисел от 1 до 100
random_list = [random.randint(1, 100) for _ in range(20)]

# Выводим все четные числа из списка
even_numbers = [num for num in random_list if num % 2 == 0]
print("Четные числа из списка:", even_numbers)

# Выводим все числа, которые делятся на 3
divisible_by_3 = [num for num in random_list if num % 3 == 0]
print("Числа, делящиеся на 3:", divisible_by_3)

# Вычисляем и выводим среднее арифметическое всех чисел в списке
average = sum(random_list) / len(random_list)
print(f"Среднее арифметическое всех чисел в списке: {average}")