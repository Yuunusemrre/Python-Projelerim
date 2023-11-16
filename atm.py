print("""
***********************************
    ATM MAKİNESİNE HOSGELDİNİZ.
***********************************

İSLEMLER;
1. Bakiye Sorgulama
2. Para Yatirma
3. Para Cekme

Programdan çıkmak için 'q'ya basın.

***********************************
""")

bakiye = 1000

while True:
    islem = input("Yapmak istediginiz islemi seciniz: ")
    
    if (islem == "q"):
        print("Yine Bekleriz.")
        break
    elif (islem == "1"):
        print("Guncel Bakiyeniz: {} TL'dir. ".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Yatirmak İstediginiz Tutari Giriniz: "))
        bakiye += miktar
    elif (islem == "3"):
        miktar = int(input("Cekmek İstediginiz Tutari Giriniz: "))
        if (bakiye - miktar < 0):
            print("Yeterli Bakiyeniz Bulunmamaktadır.")
            continue
        bakiye -= miktar
    else:
        print("Gecersiz islem!")