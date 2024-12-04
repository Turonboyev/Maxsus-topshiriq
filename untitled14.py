# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11jQfSnLecTdcmZA6FVk9bp1VVRBDWqXI
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y, label="Sinus(x)", color="blue")
plt.title("Sinus funksiyasining Grafik")
plt.xlabel("X qiymatlari")
plt.ylabel("Y qiymatlari")
plt.legend()
plt.grid()

x_random = np.random.uniform(0, 10, 50)
y_random = np.random.uniform(0, 10, 50)

plt.subplot(1, 2, 2)
plt.scatter(x_random, y_random, label="Nuqtalar", color="blue")
plt.title("Tasodifiy Nuqtalar Scatter Grafik")
plt.xlabel("X qiymatlari")
plt.ylabel("Y qiymatlari")
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig("graphs.png")
plt.show()

import pandas as pd


url = "https://raw.githubusercontent.com/Zulayho06/Maxsus-topshiriq/main/WHO%20COVID-19%20cases.csv"
df = pd.read_csv(url)


print("DataFrame Ma'lumotlari:")
df.info()


print("\nUstunlar ro'yxati:")
print(df.columns)


print("\nDataFrame'ning bosh qismini ko'rib chiqish:")
print(df.head())


covid_by_country = df.groupby('Country')['Cumulative_cases'].sum().reset_index()


covid_by_country = covid_by_country.sort_values(by='Cumulative_cases', ascending=False)

print("\nEng yuqori tasdiqlangan holatlar bo'yicha 10 ta davlat:")
print(covid_by_country.head(10))


usa_data = df[df['Country'] == 'USA']


print("\nUSA bo'yicha tasdiqlangan COVID-19 holatlari:")
print(usa_data[['Date_reported', 'Cumulative_cases']].tail())



india_data = df[df['Country'] == 'India']


print("\nIndia bo'yicha tasdiqlangan COVID-19 holatlari:")
print(india_data[['Date_reported', 'Cumulative_cases']].tail())

import pandas as pd
from google.colab import files

# 1. Faylni yuklash qismi
print("Zavodlaringiz bilan birga CSV faylni yuklang:")
uploaded = files.upload()  # Bu joyda fayl yuklanadi

# Fayl nomini olish
file_name = list(uploaded.keys())[0]  # Yuklangan fayl nomi avtomatik aniqlanadi

# 2. Yuklangan CSV faylni o'qish
df = pd.read_csv(file_name)  # Bu yerda fayl DataFrame sifatida o'qiladi

# 3. Ma'lumotlarni ekranga chiqarish
print("Yuklangan ma'lumotlar:")
print(df.head())  # Birinchi 5 qatorni ko'rsatadi

# Filtrlash uchun foydalanuvchi parametrlarini kiritadi
print("\nFiltrlash uchun parametrlarni kiriting:")
region = input("Qaysi regionni filtrlashni xohlaysiz? (masalan, 'Asia', 'Europe', 'Americas'): ")
min_population = int(input("Minimal aholini kiriting (millionlarda): "))
min_area = int(input("Minimal maydonni kiriting (km²): "))

# 4. Filtrlash qismi
filtered_df = df[(df['Region'] == region) &
                 (df['Population'] >= min_population) &
                 (df['Area'] >= min_area)]

# Filtrlash natijalari
print("\nFiltrlash natijalari:")
print(filtered_df)

# 5. Natijani yangi CSV faylga saqlash
filtered_df.to_csv("filtered_countries.csv", index=False)
print("\nFiltrlash natijalari 'filtered_countries.csv' fayliga saqlandi.")

# Natijalarni yuklab olish
files.download("filtered_countries.csv")  # Saqlangan faylni yuklab olish

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("0990.jfif")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("1005.jfif")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("1605.jfif")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)