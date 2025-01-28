# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:25:50 2025

@author: Eldorbek
"""


# =============================================================================
# yosh = int(input("Yoshingiz nechida? >>> "))
# if yosh<=0:
#     narx = 0
# elif yosh <= 12:
#     narx = 5000
# elif yosh <=18:
#     narx = 8000
# else:
#     narx = 10000
# print(f"Sizga kirish puli {narx} so'm")
# =============================================================================

# Lower metodi inputga kiritilgan so'zni hariflarini kichkina harflarga o'zgratiradi 

# =============================================================================
# kun = input("Bugun haftaning qaysi kuni? ")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")
# =============================================================================




# =============================================================================
# kun = input("Bugun qaysi kun? ")
# harorat = float(input("Harorat qanday? "))
# if kun.lower()== "yakshanba" or kun.lower() == "shanba" and harorat>=30:
#     print("cho'milishga ketdik")
# elif kun.lower()== "yakshanba" or kun.lower() == "shanba" and harorat<30:
#     print("Bugun uyda qolamiz")
# else:
#     print("Bugun ish kuni ishingga bor")
# =============================================================================



# =============================================================================
# narx = []
# taom = 15000
# choy = False
# salat = True
# if taom and choy:
#     narx = taom+10000
# elif taom or salat:
#     narx = taom + 5000
# 
# print(f"Jami summa {narx}")
# 
# =============================================================================



# =============================================================================
# narx = 0
# taom = True
# choy = False
# salat =True
# non = True
# kampot = False
# 
# print("Mijoz ushbu narsalarni sotib oldi 👇 ")    
# 
# if taom:
#     print("Taom")
#     narx = narx + 15000
# 
# if choy:
#     print("Choy")
#     narx = narx + 2000
# if salat:
#     print("Salat")
#     narx = narx + 5000
# if non:
#     print("Non")
#     narx = narx + 3000
# if kampot:
#     print("Kampot")
#     narx = narx + 8000    
# 
# print(f"Mijoz to'lashi kerak bo'lgan jami summa: >>> {narx}UZS")
# =============================================================================



#bu misolda in operatori yordamida menuda manti borligini tekshiradi yo'qligi sababli consolda False qiymat chiqadi
# =============================================================================
# menu = ["osh","shashlik","norin","somsa"]
# print("manti" in menu)
# =============================================================================

#bu misolda not in yordamida menu ichida shashlik yoqmi deb soradik va shashlik yoqligi sababli consolga true natijasi chiqdi
# =============================================================================
# menu = ["osh","kabob","lavash","pitsa"]
# print("shashlik" not in menu)
# 
# =============================================================================

# =============================================================================
# menu = ["osh", "manti","norin","somsa"]
# ovqat = input("Nima ovqat buyurtma qilasiz?>>> ")
# if ovqat.lower() in menu:
#     print("Buyurtmangiz qabul qilindi!")
# else:
#     print("Kechirasiz bizda bunday taom hozirda mavjud emas")
# =============================================================================


#bu misolda buyurtmalardan taomga nusha ko'chrib va if yordamida menuda taom borligini tekshiramiza 
#   bo'lsa koncolga nomi bilan shu taom bor degan matn chiqadi
# =============================================================================
# menu = ["osh","shashlik","norin","dolma"]
# buyurtmalar = ["osh","kabob","norin","sho'rva"]
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menyuda {taom} bor")
#     else:
#         print(f"Kechirasiz menyuda {taom} yo'q")
# =============================================================================
