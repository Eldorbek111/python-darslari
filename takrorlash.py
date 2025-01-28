# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:59:59 2025

@author: Eldorbek
"""

# =============================================================================
# cars = ["toyota","mazda","hyundai","gm","kia"]
# for car in cars:
#     if car == "gm":
#         print(car.upper())
#     else:
#         print(car.title())
# =============================================================================


# =============================================================================
admin = "Ali"
foydalanuvchi = input("iltimos ismingizni kiriting!!>>> ")
if foydalanuvchi == admin:
    print("Xush kelibsiz, Admin. Foydalanuvchi ro'yhatiga kirishni hohlaysizmi?")
# else:
#     print(f"Xush kelibsiz: {foydalanuvchi}")
# =============================================================================


# =============================================================================
# 
# son_1 = input("Birinchi sonni kiriting: >>> ")
# son_2 = input("Ikkinchi sonni kiriting: >>> ")
# if son_1 == son_2:
#     print("Ikkita son bir biriga teng")
# else:
#     print("Siz kiritgan sonlar bir biriga teng emas")
#     
# =============================================================================




son = int(input("Ixtiyoriy son kiriting:>>> "))
if son<0:
    print("siz kiritgan son manfiy")
else:
    print("Siz kiritgan son musbat")