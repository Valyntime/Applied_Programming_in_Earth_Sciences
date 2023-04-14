# КРОК ЗА КРОКОМ
import pandas as pd
import matplotlib.pyplot as plt
import PyPDF2
from PIL import Image
import numpy as np
from fpdf import FPDF
import pandas as pd
import webbrowser
import os

def read_data(filename):
    # Відкриття файлу на читання
    with open(filename, 'r') as f:
        # Зчитування кожного рядка з файлу, перевірка чи це число, та конвертація в тип float, якщо умова виконується.
        data = [float(line.strip()) for line in f if line.strip().replace('.', '', 1).isdigit()]
        # Повертаємо отримані дані.
    return data

def compute_and_save_histogram(filename, num_bins):
    data = pd.read_csv(filename, header=None)[0]
    # Обчислюємо максимальне та мінімальне значення вибірки
    x_min = min(data)
    x_max = max(data)
    # Обчислюємо приріст для діапазонів
    dx = (x_max - x_min) / num_bins
    # Створюємо списки для зберігання границь та кількості значень в кожному діапазоні
    bins = []
    bins = sorted(bins, key=lambda x: x[0])
    counts = []
    # Обчислюємо кількість значень в кожному діапазоні та зберігаємо
    # границі та цю кількість у відповідні списки
    for i in range(num_bins):
        lower_bound = x_min + i * dx
        upper_bound = lower_bound + dx
        bin_count = len(data[(data >= lower_bound) & (data < upper_bound)])
        bins.append((lower_bound, upper_bound))
        counts.append(bin_count)
    # Зберігаємо результати у текстовий файл
    with open('2maby.txt', 'w') as file:
        file.write(f"Мінімальне значення: {x_min}\n")
        file.write(f"Максимальне значення: {x_max}\n")
        file.write(f"Приріст для діапазонів: {dx}\n")
        file.write("Опис діапазонів:\n")
        for i in range(num_bins):
            file.write(f"{bins[i][0]} - {bins[i][1]}: {counts[i]}\n")
    # Створюємо гістограму та отримуємо інформацію про кількість значень у кожному біні та діапазони бінів
    counts, bins, _ = plt.hist(data, bins=num_bins, edgecolor='black')
    plt.xlabel('Значення')  # Встановлюємо підпис для осі абсцис
    plt.ylabel('Частота')  # Встановлюємо підпис для осі ординат
    plt.title('Гістограма')  # Встановлюємо заголовок гістограми
    plt.savefig('2maby.png')  # Зберігаємо гістограму у зображенні


def create_pdf(data, filename, font_name='DejaVu', font_size=10):
    pdf = FPDF()
    pdf.add_font(font_name, '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font(font_name, '', font_size)
    pdf.add_page()
    pdf.set_text_color(0, 0, 0)
    textl = f"Практична робота 3. " \
            f"Розрахунок гістограми по набору даних"
    pdf.text(60, 10, txt=textl)

    with open("2maby.txt", "r") as file:

        lines = file.readlines()

        for line in lines:
            # Визначення ширини рядка без останнього символу
            line_width = pdf.get_string_width(line[:-1])

            # Визначення ширини сторінки
            page_width = pdf.w - 2 * pdf.l_margin

            # Якщо рядок більший за ширину сторінки, то поділити його на частини
            if line_width > page_width:
                words = line[:-1].split()
                new_line = ""
                for word in words:
                    if pdf.get_string_width(new_line + " " + word) < page_width:
                        new_line += " " + word
                    else:
                        pdf.cell(0, 10, txt=new_line.lstrip())
                        new_line = word
                pdf.cell(0, 10, txt=new_line.lstrip())
            else:
                pdf.cell(0, 10, txt=line[:-1])

            pdf.ln()  # Перехід на новий рядок

    pdf.image('2maby.png', x=25, y=160, w=170)

    pdf.set_text_color(255,140, 0)
    textl = f"Добров В.Д."
    pdf.text(150, 170, txt=textl)
    pdf.output(filename, 'F')

def open_pdf(filename):
    os.startfile(filename)

if __name__ == '__main__':
    data = read_data('data.txt')
    compute_and_save_histogram('data.txt', 10)
    create_pdf(data=None, filename="2maby.pdf", font_name='DejaVu', font_size=10)
    open_pdf("2maby.pdf")



