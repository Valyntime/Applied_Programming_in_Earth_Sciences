import math
import os
# З читування файлів.
def read_coordinates_and_magnitudes(filename):
    Mag = []
    List_count = 0

    with open(filename, 'r') as f:
        try:
            AX = float(f.readline())
            AY = float(f.readline())
            BX = float(f.readline())
            BY = float(f.readline())
        except ValueError:
            print("Невірний формат чисел у початкових координатах.")
            return None

        while True:  # Безкінечний цикл для зчитування магнітуд
            Zn = f.readline()  # Зчитування наступного рядка як значення магнітуди `Zn`
            if not Zn:  # Якщо рядок порожній (кінець файлу), виходимо з циклу
                break
            try:
                Mag.append(float(Zn))  # Додавання числа до списку `Mag`
                List_count += 1  # Інкрементування лічильника `List_count`
            except ValueError:
                print("Невірний формат числа. Пропускаю...")
                continue
    # Повертаємо значення координат і магнітуд у буфер обміну
    return AX, AY, BX, BY, Mag, List_count
# Обрахунки Зміних
def calculate_parameters(AX, AY, BX, BY, Mag, List_count):
    Tmax = max(Mag)
    Tmin = min(Mag)
    Ts = Tmin - (Tmax - Tmin) / 2
    coef = int(input("Введіть кофіціент: 1, або 2 ")) / 100000
    delta_X = BX - AX
    delta_Y = BY - AY
    delta = math.sqrt(delta_X ** 2 + delta_Y ** 2) / List_count
    kut = math.atan(delta_Y / delta_X)
#
    return Tmax, Tmin, Ts, coef, delta_X, delta_Y, delta, kut
# Приклад використання функцій:
filename = input("Введіть назву файлу: ")
result = read_coordinates_and_magnitudes(filename)
if result is not None: # Перевірка, чи отримано коректний результат з функції
    AX, AY, BX, BY, Mag, List_count = result # Предача значень з `result`, й присвоєння їх змінним
    Tmax, Tmin, Ts, coef, delta_X, delta_Y, delta, kut = calculate_parameters(AX, AY, BX, BY, Mag, List_count)

    print("Початкові координати:")
    print("AX =", AX)
    print("AY =", AY)
    print("BX =", BX)
    print("BY =", BY)
    print("Список чисел:", Mag)
    print("Кількість чисел:", List_count)

    print("Максимальне значення (Tmax):", Tmax)
    print("Мінімальне значення (Tmin):", Tmin)
    print("Середнє значення (Ts):", Ts)
    print("Коефіціент (coef):", coef)
    print("Значення delta_X:", delta_X)
    print("Значення delta_Y:", delta_Y)
    print("Значення delta:", delta)
    print("Значення кута (kut):", kut)
def generate_kml_file(file_name2):
    with open(file_name2, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<kml xmlns="http://earth.google.com/kml/2.2">\n')
        f.write('  <Document>\n')
        f.write('      <Placemark>\n')
        f.write('          <name>Mict Potona</name>\n')
        f.write('          <description>Grafik magnita pola</description>\n')
        f.write('          <Style>\n')
        f.write('              <LineStyle>\n')
        f.write('                  <color>7f00ffff</color>\n')
        f.write('                  <width>3</width>\n')
        f.write('              </LineStyle>\n')
        f.write('          </Style>\n')
        f.write('          <LineString>\n')
        f.write('              <extrude>1</extrude>\n')

        coordinates = ''
        i = 0
        while i < List_count:
            coordinates += (
                    str(i * delta * math.cos(kut) - (Mag[i] - Ts) * coef * math.sin(kut) + AX) + ',' +
                    str(i * delta * math.sin(kut) - (Mag[i] - Ts) * coef * math.cos(kut) + AY) + ',0 '
            )
            i += 1

        f.write('       <coordinates>' + coordinates + '</coordinates>\n')
        f.write('          </LineString>\n')
        f.write('      </Placemark>\n')
        f.write('  </Document>\n')
        f.write('</kml>\n')
        print(coordinates)
    # Запуск щойно створеного файлу
    os.startfile(file_name2)
# Приклад використання функції:
file_name2 = input('Введіть назву файлу.kml: ')
generate_kml_file(file_name2)