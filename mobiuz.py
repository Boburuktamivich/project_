import time
import json

def yuklash():
    fayl_nomi = 'kontaktlar.json'
    try:
        with open(fayl_nomi, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def saqlash(ruyxat):
    fayl_nomi = 'kontaktlar.json' 
    with open(fayl_nomi, "w") as f:
        json.dump(ruyxat, f, indent=4)

kontaktlar = yuklash()

hisob = 0
trafik = 0
while True:
    #menyu
    print("\n1 - Mobiuz-Info")
    print("2 - Sozlamalar")
    print("3 - chiqish")

    move = int(input(">>> "))
    if move == 1:
        while True:
            print("\n1 - Balans")
            print("2 - Boshqa")
            print("3 - Kontaktlar")
            print("4 - Ko'ngilochar")
            print("5 - Yangiliklar")
            print("6 - Ob-havo")
            print("7 - Astrologiya")
            print("8 - Foydali")
            print("9 - Ta'lim")
            print("10 - Info")
            print("11 - chiqish")

            a = int(input(">>> "))

            if a == 1:
                #Balans menyu
                while True:
                    print("\n1 - Hisobni tekshirish")
                    print("2 - Trafik qoldig'ini tekshirish")
                    print("3 - Va'da qilingan to'lov")
                    print("4 - Internet")
                    print("5 - chiqish")

                    b = int(input(">>> "))
                    if b == 1:
                        print("Kuting... ")
                        time.sleep(3)
                        print(f"sizning hisob ta'rifingiz: {hisob}")
                    elif b == 2:
                        print("Kuting... ")
                        time.sleep(3)
                        print(f"sizning trafik qoldig'ingiz: {trafik}")
                    elif b == 3:
                        while True:
                          print("\n1 - 2500 so'm")
                          print("2 - 5 000 so'm")
                          print("3 - 10 000 so'm")
                          print("4 - 15 000 so'm")
                          print("5 - Boshqa")
                          print("6 - chiqish")

                          qarz = int(input(">>> "))
                          if qarz == 1:
                              surov = input("Buyurtma tasdiqlansinmi? (ha/yuq): ")
                              if surov == 'ha':
                                  print("Kuting... ")
                                  time.sleep(3)
                                  hisob += 2_500
                                  print("sizning hisobingizga 2 500 so'm tushdi")
                              else:
                                  print("Rad etildi!")

                          elif qarz == 2:
                              surov = input("Buyrutma tasdiqlansinmi? (ha/yuq): ")
                              if surov == 'ha':
                                  print("Kuting... ")
                                  time.sleep(3)
                                  hisob += 5_000
                                  print("sizning hisobingizga 5 000 so'm tushdi")
                              else:
                                  print("Rad etildi!")

                          elif qarz == 3:
                              surov = input("Buyurtma tasdiqlansinmi? (ha/yuq): ")
                              if surov == 'ha':
                                  print("Kuting... ")
                                  time.sleep(3)
                                  hisob += 10_000
                                  print("sizning hisobingizga 10 000 so'm tushdi")
                              else:
                                  print("Rad etildi!")

                          elif qarz == 4:
                              surov = input("Buyurtma tasdiqlansinmi? (ha/yuq): ")
                              if surov == 'ha':
                                  print("Kuting... ")
                                  time.sleep(3)
                                  hisob += 15_000
                                  print("sizning hisobingizga 15 000 so'm tushdi")
                              else:
                                  print("Rad etildi!")
                        
                          elif qarz == 5:
                              miqdor = int(input("miqdoqni kiriting>>> "))
                              surov =  input("Buyurtma tasdiqlansinmi? (ha/yuq): ")
                              if surov == 'ha':
                                  print("Kuting... ")
                                  time.sleep(3)
                                  hisob += miqdor
                                  print(f"sizning hisobingizga {miqdor} so'm tushdi")
                              else:
                                  print("Rad etildi!")
                          elif qarz == 6:
                              break
                          else:
                              print("Noto'g'ri buyruq! qayta kiriting!")
                    
                    elif b == 4:
                        while True:
                            print("\n1 - Oylik")
                            print("2 - Kunlik")
                            print("3 - Chiqish")

                            c = int(input(">>> "))
                            if c == 1:
                                while True:
                                    print("\n1 - 300 mb")
                                    print("2 - 500 mb")
                                    print("3 - 1000 mb")
                                    print("4 - 2000 mb")
                                    print("5 - 3000 mb")
                                    print("6 - 5000 mb")
                                    print("7 - 10000 mb")
                                    print("8 - 20000 mb")
                                    print("9 - 30000 mb")
                                    print("10 - 50000 mb")
                                    print("11 - chiqish")
                                    
                                    tanlov = int(input('>>> '))
                                    if tanlov == 1:
                                        print("To'plam narxi - 8000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 8000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 8000
                                                trafik += 300
                                                print("sizga 300 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")

                                    elif tanlov == 2:
                                        print("To'plam narxi - 9000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 9000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 9000
                                                trafik += 500
                                                print("sizga 500 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")

                                    elif tanlov == 3:
                                        print("To'plam narxi - 11000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 11000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 11000
                                                trafik += 1000
                                                print("sizga 1000 mb tushdi!")
                                                print(f"Hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 4:
                                        print("To'plam narxi - 17000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 17000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 17000
                                                trafik += 2000
                                                print("sizga 2000 mb tushdi!")
                                                print(f"Hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 5:
                                        print("To'plam narxi - 25 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 25000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 25000
                                                trafik += 3000
                                                print("sizga 3000 mb tushdi!")
                                                print(f"Hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 6:
                                        print("To'plam narxi - 33 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 33000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 33000
                                                trafik += 5000
                                                print("sizga 5000 mb tushdi!")
                                                print(f"Hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 7:
                                        print("To'plam narxi - 50000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 50000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 50000
                                                trafik += 10000
                                                print("sizga 10000 mb tushdi!")
                                                print(f"Hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")

                                    elif tanlov == 8:
                                        print("To'plam narxi - 55 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 50000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 55000
                                                trafik += 20000
                                                print("sizga 20000 mb tushdi!")
                                                print(f"Hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")

                                    elif tanlov == 9:
                                        print("To'plam narxi - 65 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 65000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 65000
                                                trafik += 30000
                                                print("sizga 30000 mb tushdi!")
                                                print(f"Hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 10:
                                        print("To'plam narxi - 75 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 75000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 75000
                                                trafik += 50000
                                                print("sizga 50000 mb tushdi!")
                                                print(f"Hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    elif tanlov == 11:
                                        break
                                    else:
                                        print("NOto'g'ri buyruq! Qayta urinib ko'ring!")
                                    
                            if c == 2:
                                while True:
                                    print("\n1 - 200 mb")
                                    print("2 - 300 mb")
                                    print("3 - 500 mb")
                                    print("4 - 1000 mb")
                                    print("5 - 2000 mb")
                                    print("6 - 3000 mb")
                                    print("7 - 5000 mb")
                                    print("8 - 10000 mb")
                                    print("9 - Chiqish")

                                    tanlov = int(input('>>> '))
                                    if tanlov == 1:
                                        print("To'plam narxi - 2 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 2000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 2000
                                                trafik += 200
                                                print("sizga 300 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 2:
                                        print("To'plam narxi - 3 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 3000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 3000
                                                trafik += 300
                                                print("sizga 300 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                        
                                    elif tanlov == 3:
                                        print("To'plam narxi - 5 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 5000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 5000
                                                trafik += 500
                                                print("sizga 500 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 4:
                                        print("To'plam narxi - 10 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 10000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 10000
                                                trafik += 1000
                                                print("sizga 1000 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 5:
                                        print("To'plam narxi - 20 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 20000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 20000
                                                trafik += 2000
                                                print("sizga 300 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 6:
                                        print("To'plam narxi - 30 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 30000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 30000
                                                trafik += 3000
                                                print("sizga 3000 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")

                                    elif tanlov == 7:
                                        print("To'plam narxi - 50 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 50000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 50000
                                                trafik += 5000
                                                print("sizga 5000 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")

                                    elif tanlov == 8:
                                        print("To'plam narxi - 100 000 so'm")
                                        surov = input("buyurtma tasdiqlansinmi? (ha/yuq): ").lower()
                                        if surov == 'ha':
                                            if hisob >= 100000:
                                                print("Kuting... ")
                                                time.sleep(3)
                                                hisob -= 100000
                                                trafik += 10000
                                                print("sizga 10000 mb tushdi!")
                                                print(f"hisobingiz: {hisob}")
                                            else:
                                                print("Yetarli mablag' mavjud emas! hisobingizni to'ldiring!")
                                        else:
                                            print("Rad etildi")
                                    
                                    elif tanlov == 9:
                                        break
                                    else:
                                        print("Noto'g'ri buyruq! qayta kiriting")

                            if c == 3:
                                break        

                    elif b == 5:
                        break
                    else:
                        print("Noto'g'ri buyruq! qayta kiriting!")
            
            elif a == 2:
                while True:
                    print("\n1 - Sizga qo'ng'iroq qilishdi")
                    print('2 - AntiAON')
                    print("3 - Menga qo'g'iroq qil")
                    print("4 - Mobi Music")
                    print("5 - Mobi cinema+TV")
                    print("6 - Chiqish")

                    d = input(">>> ")
                    if d == '1':
                        print("Xizmat narxi - 5 000 so'm")
                        surov = input("Xizmatni yoqishni istaysizmi? (ha/yuq): ").lower()
                        if surov == 'ha':
                            if hisob >= 5000:
                                print("Kuting... ")
                                time.sleep(5)
                                hisob -= 5000
                                print("Siz Obuna bo'ldingiz")
                            else:
                                print("Kuting... ")
                                time.sleep(5)
                                print("Sizda yetarli mablag' mavjud emas!")
                        elif surov == 'yuq':
                            print('Rad etildi!')
                        else:
                            print("Notug'ri buyruq! iltimos faqat ha yoki yuq deb kiriting!")

                    elif d == '2':
                        print("Xizmat narxi - 5 000 so'm")
                        surov = input("Xizmatni yoqishni istaysizmi? (ha/yuq): ").lower()
                        if surov == 'ha':
                            if hisob >= 5000:
                                print("Kuting... ")
                                time.sleep(5)
                                hisob -= 5000
                                print("Siz Obuna bo'ldingiz")
                            else:
                                print("Kuting... ")
                                time.sleep(5)
                                print("Sizda yetarli mablag' mavjud emas!")
                        elif surov == 'yuq':
                            print('Rad etildi!')
                        else:
                            print("Notug'ri buyruq! iltimos faqat ha yoki yuq deb kiriting!")
                    
                    elif d == '3':
                        print("Xizmat narxi - 5 000 so'm")
                        surov = input("Xizmatni yoqishni istaysizmi? (ha/yuq): ").lower()
                        if surov == 'ha':
                            if hisob >= 5000:
                                print("Kuting... ")
                                time.sleep(5)
                                hisob -= 5000
                                print("Siz Obuna bo'ldingiz")
                            else:
                                print("Kuting... ")
                                time.sleep(5)
                                print("Sizda yetarli mablag' mavjud emas!")
                        elif surov == 'yuq':
                            print('Rad etildi!')
                        else:
                            print("Notug'ri buyruq! iltimos faqat ha yoki yuq deb kiriting!")
                    
                    elif d == '4':
                        print("Xizmat narxi - 5 000 so'm")
                        surov = input("Xizmatni yoqishni istaysizmi? (ha/yuq): ").lower()
                        if surov == 'ha':
                            if hisob >= 5000:
                                print("Kuting... ")
                                time.sleep(5)
                                hisob -= 5000
                                print("Siz Obuna bo'ldingiz")
                            else:
                                print("Kuting... ")
                                time.sleep(5)
                                print("Sizda yetarli mablag' mavjud emas!")
                        elif surov == 'yuq':
                            print('Rad etildi!')
                        else:
                            print("Notug'ri buyruq! iltimos faqat ha yoki yuq deb kiriting!")
                    
                    elif d == '5':
                        print("Xizmat narxi - 5 000 so'm")
                        surov = input("Xizmatni yoqishni istaysizmi? (ha/yuq): ").lower()
                        if surov == 'ha':
                            if hisob >= 5000:
                                print("Kuting... ")
                                time.sleep(5)
                                hisob -= 5000
                                print("Siz Obuna bo'ldingiz")
                            else:
                                print("Kuting... ")
                                time.sleep(5)
                                print("Sizda yetarli mablag' mavjud emas!")
                        elif surov == 'yuq':
                            print('Rad etildi!')
                        else:
                            print("Notug'ri buyruq! iltimos faqat ha yoki yuq deb kiriting!")
                    
                    elif d == '6':
                        break
                    else:
                        print("Noto'g'ri buyruq! qayta kiriting!")
            elif a == 3:

                while True:
                  print("\n1 - Kontakt qo'shish")
                  print("2 - Kontaktlarni ko'rish")
                  print("3 - Kontaktni o'chirish")
                  print("4 - Chiqish")

                  e = int(input(">>> "))

                  if e == 1:
                    ism = input("Ismni kiriting: ")
                    tel = input("Raqamni kiriting: ")
                    for i in tel:
                      if i.isalpha():
                        print("Raqamni noto'g'ri kiritdingiz! Yana urinib ko'ring!\n")
                        break
                      elif len(tel) != 13:
                        print("Raqam formati noto'g'ri! Yana urinib ko'ring!\n")
                        break
                      else:
                        kontaktlar[ism.title()] = tel
                        saqlash(kontaktlar)
                        print(f"{ism.title()} kontaktlar ro‘yxatiga kiritildi!\n")
                        break

                  elif e == 2:
                    if not kontaktlar:
                      print("Kontaktlaringiz yo‘q!")
                    else:
                      print("\nKontaktlaringiz ro‘yxati:")
                      for index, (ism, tel) in enumerate(kontaktlar.items(), 1):
                          print(f"{index}. {ism} - {tel}")

                  elif e == 3:
                    if not kontaktlar:
                      print("O‘chirish uchun kontakt yo‘q!")
                    else:
                       uchirish = input("O‘chirish uchun ismni kiriting: ").title()
                    if uchirish in kontaktlar:
                      del kontaktlar[uchirish]
                      print(f"{uchirish} kontaktlaringizdan o‘chirildi!")
                    else:
                      print("Bunday ism kontaktlaringizda yo‘q!")
                  elif e == 4:
                      break
                  else:
                      print("Notug'ri buyruq! qayta urinib ko'ring!")



            elif a == 11:
                break
    elif move == 3:
        print("Dastur tugadi!")       
        break






