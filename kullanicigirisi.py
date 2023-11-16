print("""
**********************************
     Kullanici Girisi Programı
**********************************
 """)
      
sys_kullanici_adi = "Divâne"
sys_parola = "1234"
girishakki = 3

while True:
    kullanici_adi = input("Kullanici Adinizi Giriniz: ")
    parola = input("Parolanizi Giriniz: ")
    if (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanici Adiniz Hatali!")    
        girishakki -= 1
    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatali!")    
        girishakki -= 1
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanici Adi Ve Parola Hatali!")    
        girishakki -= 1
    else:
        print("Sisteme Başarıyla Giris Yapildi.")
        break
    if (girishakki == 0):
        print("Giris Hakkiniz Bitti.")
        break
        