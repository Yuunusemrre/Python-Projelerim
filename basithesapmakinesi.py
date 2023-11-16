ilkSayi = int(input("İlk Sayiyi Giriniz: "))
ikinciSayi = int(input("İkinci Sayiyi Giriniz: "))
islem = input("""Yapmak İstediginiz İslemi Giriniz.
(Toplama: + , Cıkartma: - , Carpma: * , Bolme: / )
""")

if (islem == "+"):
    print("Sonuc: "+str(ilkSayi + ikinciSayi))
elif (islem == "-"):
    print("Sonuc: "+str(ilkSayi - ikinciSayi))
elif (islem == "*"):
    print("Sonuc: "+str(ilkSayi * ikinciSayi))
elif (islem == "/"):
    print("Sonuc: "+str(ilkSayi / ikinciSayi))
else:
    print("Hatali giris yaptiniz.")