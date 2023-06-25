print()
print("################################")
print("#       Добров Валентин        #")
print("#   Екзаменаційний Білет  2.   #")
print("#      Завдання  №3            #")
print("#      Вхідні файлу: 7.txt     #")
print("#                              #")
print('################################')
print()
def calculate_min_max(filename):
    with open(filename, 'r') as file:
        # Читаємо всі рядки з файлу та перетворюємо їх на числа
        numbers = [float(line.strip()) for line in file]

    if numbers:
        # Обчислюємо максимальне та мінімальне значення
        maximum = max(numbers)
        minimum = min(numbers)

        # Відображення результатів

        print(" Максимальне значення:", maximum)
        print("Мінімальне значення:", minimum)
        print()

        print('# Відображення мак, мін значень по #')
        print('# вхідним даним з файлу (7.txt) є вдалим #')
    # У різі якщо файл порожній.
    else:
        print("Файл порожній.")

# Приклад виклику функції з файлом "data.txt"
calculate_min_max("7.txt")