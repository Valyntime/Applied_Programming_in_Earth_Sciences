import numpy as np
import matplotlib.pyplot as plt



# Відкрити дата, прочитати й закинути у список set1.
# створюємо новий список set2.
# закинути формулу Кальмана, заипуємо отриманий рeзультат у set2.
# воодимо список 2.

print()
print("################################")
print("#                              #")
print("#  Практична робота номер 1.   #")
print("#      Формула Кальмана        #")
print("#                              #")
print('################################')
print()
print("Вітаю оберіть сетап")
box1= input("З графіком або без (Так/Ні):  ")
if (box1 == "Н") or (box1 == "н") or (box1=='Y') or (box1=='y'):
        f= input()
        f = open('data.txt')
        f1 = open('data_out_1.csv','w')
        g =0
        k =0.1
        Zn = f.readline()
        fir = float(Zn)

        while True:
                Zn = f.readline()
                if not Zn:
                        break
                dd= float(Zn)
                fir=k*dd+(1-k)*fir
                g += 1
                o = str(g)+'; '+str(dd)+'; '+str(fir)+'\n'
                o = o.replace('.',',')
                f1.write(o)
        f.close()
        f1.close()

elif (box1 == "N") or (box1 == "n") or (box1=='Т') or (box1=='т'):
        # Розташування файлу
        print('Розташування файлу')
        print("якщо файл знаходиться в тій самій директорії")
        print("Приклад: test.txt")
        print("якщо файл знаходиться в іншому каталозі")
        print('Приклад: "C:/users/Python/test.txt"')

        # Read data
        data0 = input("Назва файлу:     ")
        data = np.genfromtxt(data0+".txt")
        # Фільтер Кальмена
        k= input(("Ведіь коефіцієнт (0-1): "))
        k= float(k)
        k = k # Фактор згладжування
        m = data[0] # Початкове значення м
        # Застосовуємо фільтр Кальмана
        filter_data = []
        for v in data:
                mi = k*v+(1-k)*m
                filter_data.append(mi)
                m = mi
        # Зберігання даних у файлі cvs
        name_out_put_txt = input("Вкажіть назву файлу без рзширення. Приклад: dataoutput   ")
        np.savetxt(name_out_put_txt + ".csv", np.column_stack((data, filter_data)), delimiter=',')
        # Побудова графіка
        plt.plot(data, label='Raw Data', marker = 'o' )
        plt.plot(filter_data, label="Filtered Data", marker= '^' )
        plt.legend()
        plt.show()




