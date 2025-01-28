# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:33:06 2025

@author: Eldorbek
"""
# =============================================================================
# yosh = int(input("Yoshingizni kiriting!! >>> "))
# if yosh<=4:
#     print("Kirish bepul")
# elif yosh<=12:
#     print("Kirish 5000 UZS")
# elif yosh<=18:
#     print("Kirish 8000 UZS")
# else:
#     print("Kirish 10000 UZS")
# =============================================================================


# =============================================================================
# kun = input("Bugun haftaning qaysi kuni: >>> ")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni ishinga bor yaramas")
# =============================================================================




kun = input("Bugun haftaning qaysi kuni:>>> ")
harorat = int(input("Xarorat nechi:>>> "))
if kun.lower() == "yakshanba" or kun.lower() == "shanba" and harorat>=30:
    print("Cho'milishga ketdik")
elif kun.lower() == "yakshanba" or kun.lower() == "shanba" and harorat<30:
    print("Bugun uyda dam olamiz")
