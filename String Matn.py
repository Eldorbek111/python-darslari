# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:07:55 2025

@author: Eldorbek
"""

#bu kodda print yordamida 2 ta o'zgaruvchini consolda bir qatorda chiqarishga erishdik.'
# =============================================================================
# =============================================================================
# # 
# # shaxar = "Yangiqo'rg'on"
# # viloyat = 'Namangan'
# # print(viloyat,shaxar)
# # =============================================================================
# 
# =============================================================================


#bu kodda matn ichiga stiker qo\'shishni amalga oshirdim
# =============================================================================
# matn = "Men yangi 📱 oldim "
# print(matn)
# =============================================================================


#bu kodda ism degan o'zgaruvchi oldiga matn qo'shib birga consolga chiqarishga erishildi.
# =============================================================================
# ism = "Eldorbek"
# print("Mening ismim " + ism)
# =============================================================================

#Bu kodda 2 ta o'zgaruvchi qiymatlarini qo'shib va ular orasida boshliq qoldirish amalga oshirildi
# =============================================================================
# ism = "Eldorbek"
# familya = "Erkinov"
# print(ism + ' ' +familya)
# =============================================================================
# =============================================================================
# 

# f-string
# Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun f-string usulidan  f"{matn1} {matn2}" ham foydalansak bo'ladi:
# =============================================================================

                                                     #f-stringga misollar
                                                     

#Bu kodda f-string dan foydalanib bir nechta matnni qoshishni amalga oshirdim
# =============================================================================
# ism = "Azamat"
# familya = "Tursunboyev"
# print(f"Do'stimni Ismi {ism}. {ism} {familya}!")
# =============================================================================
 #bu kodda ikkita o'zgaruvchini f-stringdan foydalanib consolga chiqardim
# =============================================================================
# ism = "Eldorbek"
# Ism = "Qodir"
# familya ="Erkinov"
# 
# print(f"Mening ismim {ism}. \nMening do'stimni ismi {Ism}.")
# =============================================================================


                                                    #STRING METODLARI BILAN ISHLASH
# upper() metodi matndagi har bir harfni katta harfga o'zgartiradi.                                                    
#Misol////
# =============================================================================
# ism = "Eldorbek"
# familya = "Erkinov"
# ism_familya = f"{ism} {familya}"
# print(ism_familya.upper())                                                    
# =============================================================================


#lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
#Misol////
# =============================================================================
# ism = "Qodir"
# familya = "Boymurodov"
# ism_familya = f"{ism} {familya}"
# print(ism_familya.lower())
# =============================================================================

#title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi. 
#misol///
# =============================================================================
# ism_familya = "shoxruh jalilov"
# print(ism_familya.title())
# =============================================================================


# =============================================================================
# capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
# =============================================================================


# =============================================================================
#                                INPUT —FOYDALANUVCHI BILAN MULOQOT
# =============================================================================
# =============================================================================
#1-misol
# ism = input("Ismingiz Nima?")
# print("Assalomu aleykum, " +ism)
# =============================================================================
#2-misol
# =============================================================================
# ism = input("Ismingiz nima\n>>>")
# print("Assalomu aleykum, " + ism.title())
# =============================================================================

#3-misol
# =============================================================================
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, "+ tuman + " tumani, " + viloyat+ " viloyati. ")
# =============================================================================


#4-misol

# =============================================================================
# kocha = input("Ko'cha nomini kiriting: ")
# mahalla = input("Mahalla nomini kiriting: ")
# tuman = input("Tumaningizni kiriting: ")
# viloyat = input("Viloyatingizni kiriting: ")
# 
# print("Ko'changiz: " + kocha.title())
# print("Mahallangiz: " + mahalla.title())
# print("Tumaningiz: " + tuman.title())
# print("Viloyatingiz: " + viloyat.title())
# =============================================================================

#5-misol
# =============================================================================
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# 
# manzil = f"{kocha} ko'chasi, \n{mahalla} mahallasi,\n {tuman} tumani, \n{viloyat} viloyati."
# print(manzil.title())
# =============================================================================

