islem = input("Hangi işlem?\n Toplama\n Çıkarma\n Bölme\n Çarpma\n Sonuç: ")

while True:
    if islem == "Toplama":
        sayi_toplama = int(input("Sayı: "))
        sayi_toplama2 = int(input("Sayı: "))
        sonuc = sayi_toplama+sayi_toplama2
        print("Sonuç: ",sonuc)
        islem = input("Hangi işlem?\n Toplama\n Çıkarma\n Bölme\n Çarpma\n Sonuç: ")
    elif islem == "Çıkarma":
        sayi_cikarma = int(input("Sayı: "))
        sayi_cikarma2 = int(input("Sayı: "))
        sonuc_cikarma = sayi_cikarma-sayi_cikarma2
        print("Sonuç: ",sonuc_cikarma)
        islem = input("Hangi işlem?\n Toplama\n Çıkarma\n Bölme\n Çarpma\n Sonuç: ")
    elif islem == "Bölme":
        sayi_bölme = int(input("Sayı: "))
        sayi_bölme2 = int(input("Sayı: "))
        sonuc_bölme = sayi_bölme/sayi_bölme2
        print("Sonuç: ",sonuc_bölme)
        islem = input("Hangi işlem?\n Toplama\n Çıkarma\n Bölme\n Çarpma\n Sonuç: ")
    elif islem == "Çarpma":
        sayi_carpma = int(input("Sayı: "))
        sayi_carpma2 = int(input("Sayı: "))
        sonuc_carpma = sayi_carpma*sayi_carpma2
        print("Sonuç: ",sonuc_carpma)
        islem = input("Hangi işlem?\n Toplama\n Çıkarma\n Bölme\n Çarpma\n Sonuç: ")
    else:
        print("Hata!")
