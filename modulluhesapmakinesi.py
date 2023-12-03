print("""************************************
*          Hesap Makinesi          *               
*                                  *
*  Toplama: 1                      *
*  Cikartma: 2                     *
*  Carpma: 3                       *
*  Bolme: 4                        *
*  Us Alma: 5                      *
*  Karakok Alma: 6                 *
*  Faktoriyel: 7                   *
*  Cikmak İcin q'ya Tiklayiniz.    *
************************************""")

import math
import time

while True:
    islem = input("İsleminizi seciniz: ")

    if (islem == "q"):
        print("Cikis yapiliyor.")
        time.sleep(1)
        print("Tekrar bekleriz...")
        break
    elif (islem == "1"):
        sayi1 = int(input("Sayiyi giriniz: "))
        sayi2 = int(input("Sayiyi giriniz: "))
        print("Isleminiz yapiliyor.")
        time.sleep(1)
        print("{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2))
    elif (islem == "2"):
        sayi1 = int(input("Sayiyi giriniz: "))
        sayi2 = int(input("Sayiyi giriniz: "))
        print("Isleminiz yapiliyor.")
        time.sleep(1)
        print("{} - {} = {}".format(sayi1,sayi2,sayi1-sayi2))
    elif (islem == "3"):
        sayi1 = int(input("Sayiyi giriniz: "))
        sayi2 = int(input("Sayiyi giriniz: "))
        print("Isleminiz yapiliyor.")
        time.sleep(1)
        print("{} * {} = {}".format(sayi1,sayi2,sayi1*sayi2))
    elif (islem == "4"):
        sayi1 = int(input("Sayiyi giriniz: "))
        sayi2 = int(input("Sayiyi giriniz: "))
        print("Isleminiz yapiliyor.")
        time.sleep(1)
        print("{} / {} = {}".format(sayi1,sayi2,sayi1/sayi2))
    elif (islem == "5"):
        sayi1 = int(input("Sayiyi giriniz: "))
        sayi2 = int(input("Sayiyi giriniz: "))
        print("Isleminiz yapiliyor.")
        time.sleep(1)
        print("{} ussu {} = {}".format(sayi1,sayi2,math.pow(sayi1,sayi2)))
    elif (islem == "6"):
        sayi1 = int(input("Sayiyi giriniz: "))
        print("Isleminiz yapiliyor.")
        time.sleep(1)
        print("{} sayisinin karekoku = {}".format(sayi1,math.sqrt(sayi1)))
    elif (islem == "7"):
        sayi1 = int(input("Sayiyi giriniz: "))
        print("Isleminiz yapiliyor.")
        time.sleep(1)
        print("{} sayisinin faktoriyeli = {}".format(sayi1,math.factorial(sayi1)))
    else:
        print("Hatali islem secimi!")
        time.sleep(3)
        