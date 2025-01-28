# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:09:39 2025

@author: Eldorbek
"""
#bu misolda mevalar degan o'zgaruvchi ichidagi ma'lumotlarni consolga chiqardik
# =============================================================================
# mevalar = ["O'rik" , "Shaftoli" , "uzum" , "olma"]
# print(mevalar)
# 
# =============================================================================

# =============================================================================


# bu misolda moshinalarni indeksi orqali consolga chiqarishga erishdik
# cars = ['damas' , 'labo' , 'cobalt' , 'gentra' , 'bmv']
# print("Birinchi moshina: " + cars[0])
# print("oxirgi moshina: " + cars[-1])
# =============================================================================


#bu misolda append metodi orqali bozorlik degan royhatga makaron degan yangi mahsulotni qo'shdik
# =============================================================================
# bozorlik = ["guruch" , "sabzi" , "un", "yog'"]
# bozorlik.append("makaron")
# =============================================================================



#bu misolda append metodi orqali bo'sh listga mahsulot qo'shdik 
# =============================================================================
# phones = []
# phones.append("iphone")
# phones.append("redmi")
# print("birinchi mahsulot: ", phones[0].title())
# print("ikkinci mahsulot: ", phones[1].upper())
# =============================================================================


#bu misolda insert metodi orqali noutbook degan o'zgaruvchiga yangi mahsulot qo'shdik
#insertni appenddan farqi bunda istalgan indeksga mahsulot qo'shish mumkin appenda esa eng or=xiriga qo'shish imkoni bor xolos
# =============================================================================
# noutbook = ["lenovo" , "acer", "Hp"]
# noutbook.insert(1, "macbook")
# print(noutbook)
# =============================================================================



#bu misolda del metodi orqali 1 indeksda turgan acer mahsulotini o'chrishga erishdik
# =============================================================================
# noutbook = ["lenovo" , "acer", "Hp"]
# del noutbook[1]
# print(noutbook)
# =============================================================================

#bu misolda remove metodi orqali mevalar degan o'zgaruvchi ichidagi olma degan masulotni o'chirishga erishdik
# =============================================================================
# mevalar = ["olma" , "anjir", "Anor", "limon"]
# mevalar.remove("olma")
# print(mevalar)
# =============================================================================

#bu misolda pop metodi orqali bozorlik degan o'zgaruvchini ichidan un degan mahsulotni chiqarib oldik
# =============================================================================
# bozorlik = ["yog'", "un", "shakar", "makaron","guruch"]
# mahsulot = bozorlik.pop(1)
# print("Sotib oldim: ", mahsulot)
# print("Sotib olishim kerak: ", bozorlik)
# =============================================================================

    

#                                            Amaliyot mashqlari

#bu misolda har bir insonga alohida habar yubordik va  uni consolda chiqardik
# =============================================================================
# ismlar = ["Azamat", "Qodir", "Doniyor"]
# print("Bugun o'qishga borasanmi",ismlar[1])
# print("Birga dars qilamizmi",ismlar[0])
# print("Birga qachon dars qilamiz",ismlar[2])
# =============================================================================

#bu misolda 2- indeksdagi 11 raqamini 100ga o'zgartirdik
# =============================================================================
# sonlar = [12,22,11,24,800,-23,12.3]
# sonlar[2] = 100
# print(sonlar)
# =============================================================================

#bu misolda 1 - indeksdagi songa 8 ni qo'shib consolga chiqardik
# =============================================================================
# sonlar = [12,22,11,24,800,-23,12.3]
# sonlar[1] = sonlar[1]+8
# print(sonlar)
# =============================================================================



# =============================================================================
# t_shaxslar = ["Alisher Navoi", "Amir Temur" , "Mirzo Ulug'bek"]
# z_shaxslar = ["bilgets" , "Ilon mack" , "Otabek Maxkamov"]
# tarixy = t_shaxslar.pop(1)
# zamonamiz = z_shaxslar.pop(1)
# print("Men tarixiy shaxslardan " + tarixy + " bilan,\n""Zamonaviy shaxslardan " + zamonamiz + " bilan suxbat qilishni istardim" )
# =============================================================================

#bu misolda append metodi orqali bo'sh listga malumot qo'shdik va remove metodidan foydalanib Bobur degan malumotni o'chirdik
#  va insert metodi yordamida shu o'chirgan Bobur degan malumotimizani yana qaytadan qoshib qoydik listga 
# =============================================================================
# friends = []
# friends.append("Xurshid")
# friends.append("Jasur")
# friends.append("Bobur")
# friends.append("Jamshid")
# friends.append("Yunus")
# friends.append("Dovud")
# 
# friends.remove("Bobur")
# friends.insert(1, "Bobur")
# print(friends)
# 
# =============================================================================


#bu misolda pop metodi yordamida friends listidan malumotlarni chiqarib olib append yordamida mehmonlar degan listga yozdik
# =============================================================================
# friends = ["jasur","Bilol","Jalol","Xurshid","damir","Quvonch","Shoxruh" ]
# mehmonlar = []
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(2))
# mehmonlar.append(friends.pop(4))
# print("Kelgan mehmonlar: ", mehmonlar)
# print("Kelmagan mehmonlar: ", friends)
# =============================================================================
