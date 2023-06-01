import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

#Параметри за умовою
n = 115 #кількість значень
mu = 5  #математичне сподівання
sigma = 1.9  #стандартне відхилення

#Згенерована вибірка
sample = [4, 8, 5, 7, 4, 4, 4, 6, 8, 4, 5, 1, 7, 3, 6, 2, 5, 6, 5, 6, 2, 4, 5, 2, 6, 7, 6, 5, 3, 7, 6, 4, 7, 2, 6, 4, 4, 6, 8, 4, 3, 3, 5, 8, 4, 7, 5, 7, 5, 3, 8, 7, 5, 7, 4, 5, 7, 3, 4, 2, 6, 4, 3, 4, 7, 6, 7, 5, 5, 2, 5, 2, 5, 4, 7, 6, 0, 7, 2, 7, 4, 6, 8, 4, 10, 6, 6, 4, 5, 4, 2, 4, 7, 3, 4, 4, 3, 8, 4, 5, 7, 8, 6, 8, 3, 6, 5, 7, 6, 7, 5, 4, 3, 4, 2]

#Вибіркове середнє
def average(sample):
    total_sum = sum(sample)
    count = len(sample)
    return total_sum / count

#Медіана
def median(sample):
    sorted_sample = sorted(sample)
    length = len(sorted_sample)
    middle = length // 2

    if length % 2 == 0:  # парна кількість елементів
        return (sorted_sample[middle - 1] + sorted_sample[middle]) / 2
    else:  # непарна кількість елементів
        return sorted_sample[middle]

#Мода
def mode(sample):
    sample_list = list(sample)
    unique_samples = set(sample_list)
    frequencies = []

    for s in unique_samples:
        freq = sample_list.count(s)
        frequencies.append((s, freq))

    max_freq = 0
    for s, freq in frequencies:
        if freq > max_freq:
            max_freq = freq

    if max_freq == 1:
       return "Моди вибірки немає"

    mode = []
    for s, freq in frequencies:
        if freq == max_freq:
            mode.append(s)
    return mode

#Вибіркова дисперсія
def variance(sample):
    n = len(sample)
    average = sum(sample) / n
    var = sum((x - average) ** 2 for x in sample) / n
    return var

#Середньоквадратичне відхилення
def standart_dev(sample):
    return math.sqrt(variance(sample))

#Виводимо результати
print(f"Вибіркове середнє: {average(sample)}")
print(f"Медіана: {median(sample)}")
print(f"Мода: {mode(sample)}")
print(f"Вибіркова дисперсія: {variance(sample)}")
print(f"Вибіркове середньоквадратичне відхилення: {standart_dev(sample)}")

#Будуємо графіки
plt.figure(figsize=(18, 12))

#Гістограма частот
plt.subplot(231)
plt.hist(sample, bins='auto', color='green', alpha=0.83, rwidth=0.75)
plt.title('Гістограма частот')

#Полігон частот
plt.subplot(232)
sns.kdeplot(sample, color='blue')
plt.title('Полігон частот')

#Діаграма розмаху
plt.subplot(234)
sns.boxplot(sample, color='lightblue')
plt.title('Діаграма розмаху')

#Кругова діаграма
plt.subplot(235)
bins = pd.cut(sample, bins=10)  # розбиваємо дані на 10 інтервалів
labels, counts = np.unique(bins, return_counts=True)
plt.pie(counts, labels=labels, autopct='%1.1f%%', colors=sns.color_palette("Set2"))
plt.title('Кругова діаграма')

#Діаграма Парето
plt.subplot(236)
counts = bins.value_counts().sort_values(ascending=False)
counts.plot(kind='bar', color='purple')
plt.title('Діаграма Парето')

plt.tight_layout()
plt.show()