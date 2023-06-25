import math
import os


print()
print("################################")
print("#                              #")
print("#  Практична робота номер 4.   #")
print("#    Генерація файлу kml       #")
print("#                              #")
print('################################')
print()
def read_coordinates_and_magnitudes(filename):
    Mag = []
    List_count = 0

    with open(filename, 'r') as f:
        try:
            AY = float(f.readline())
            AX = float(f.readline())
            BY = float(f.readline())
            BX = float(f.readline())
        except ValueError:
            print("Неправильний формат чисел у початкових координатах.")
            return None

        while True:
            Zn = f.readline()
            if not Zn:
                break
            try:
                Mag.append(float(Zn))
                List_count += 1
            except ValueError:
                print("Неправильний формат числа. Пропускаю...")
                continue

    return AX, AY, BX, BY, Mag, List_count

def calculate_parameters(AX, AY, BX, BY, Mag, List_count):
    Tmax = max(Mag)
    Tmin = min(Mag)
    Ts = Tmin + (Tmax - Tmin) / 2
    coef = int(input("Введіть кофіціент: 1, або 2 ")) / 100000
    delta_X = BX - AX
    delta_Y = BY - AY
    delta = math.sqrt(delta_X ** 2 + delta_Y ** 2) / List_count
    kut = math.atan2(delta_Y, delta_X)

    return Tmax, Tmin, Ts, coef, delta_X, delta_Y, delta, kut

def generate_kml_file(file_name2, AX, AY, BX, BY, Mag, List_count, Tmax, Tmin, Ts, coef, delta_X, delta_Y, delta, kut):
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
        for i in range(List_count):
            coordinates += (
                    str(i * delta * math.cos(kut) - (Mag[i] - Ts) * coef * math.sin(kut) + AX) + ',' +
                    str(i * delta * math.sin(kut) + (Mag[i] - Ts) * coef * math.cos(kut) + AY) + ',0 '
            )

        f.write('       <coordinates>' + coordinates + '</coordinates>\n')
        f.write('          </LineString>\n')
        f.write('      </Placemark>\n')
        f.write('  </Document>\n')
        f.write('</kml>\n')

    # Запуск щойно створеного файлу
    os.startfile(file_name2)

# Приклад використання функцій:
filename = input("Введіть назву файлу: ")+'.txt'
result = read_coordinates_and_magnitudes(filename)
if result is not None:
    AX, AY, BX, BY, Mag, List_count = result
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

    file_name2 = input('Введіть назву файлу.kml: ')+'.kml'
    generate_kml_file(file_name2, AX, AY, BX, BY, Mag, List_count, Tmax, Tmin, Ts, coef, delta_X, delta_Y, delta, kut)