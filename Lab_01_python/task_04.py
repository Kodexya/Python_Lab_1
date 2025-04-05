# Задание 4
import random

# Создаем список из 10 случайных чисел
random_list = [random.randint(1, 100) for i in range(10)]

# Выводим список
print("Список случайных чисел:", random_list)

# Находим и выводим максимальное и минимальное значение
max_value = max(random_list)
min_value = min(random_list)
print(f"Максимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")

# Вычисляем и выводим сумму всех элементов списка
sum_of_elements = sum(random_list)
print(f"Сумма всех элементов списка: {sum_of_elements}")

# Сортируем список по возрастанию и выводим его
random_list.sort()
print("Отсортированный список:", random_list)