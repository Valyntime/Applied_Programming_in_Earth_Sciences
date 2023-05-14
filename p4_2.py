import math
import os
def generate_kml_file(file_name):
    # Робота з файлом
    with open('1_data_1.txt', 'r') as f:
        Mag = []
        List_count = 0
        AY = float(f.readline())
        AX = float(f.readline())
        BY = float(f.readline())
        BX = float(f.readline())
        Zn = f.readline()
        # Цикл який відповідає за кожний наступний рядок
        while Zn:
            Zn = f.readline()
            # Цей цикл первіряє чи не порожній, наш фалй при умові, що єсимволи.
            if Zn:
                List_count += 1
                Mag.append(float(Zn))
    # Створення Зміни, для обрахунків
    # Помилка десь тут присутні!
    Tmax = max(Mag)
    Tmin = min(Mag)
    # Ts = 50700
    Ts = Tmin - (Tmax - Tmin) / 2
    coef = int(input("Введіть кофіціент: 1, або 2 ")) / 100000
    delta_X = BX - AX
    delta_Y = BY - AY
    delta = math.sqrt(delta_X ** 2 + delta_Y ** 2) / List_count
    kut = math.atan(delta_Y / delta_X)
    # створенння кмл файлу.
    with open(file_name, 'w') as f:
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
        # Цикл який перевіряє що І емнше Загального списку, тобто поки і не стане останньою, координатою у списку.
        while i < List_count:
            # координати збільшуємо, значення заповнюючи спершу по осі Х, а після по осі Y
            coordinates += (
                    str(i * delta * math.cos(kut) - (Mag[i] - Ts) * coef * math.sin(kut) + AX) + ',' +
                    str(i * delta * math.sin(kut) - (Mag[i] - Ts) * coef * math.cos(kut) + AY) + ',0 '
            )
            # Зібльшуємо кількість на один у список координат
            i += 1

        f.write('       <coordinates>' + coordinates + '</coordinates>\n')
        f.write('          </LineString>\n')
        f.write('      </Placemark>\n')
        f.write('  </Document>\n')
        f.write('</kml>\n')

    # Запуск щойно створеного файлу
    os.startfile(file_name)

file_name = input('Введіть назву файлу.kml: ')
generate_kml_file(file_name)
