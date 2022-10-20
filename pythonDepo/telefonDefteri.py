tel=[]
while True:
    print(*"TELEFON DEFTERİ")
    print("1. Ekle")
    print("2. Sil")
    print("3. Listele")
    print("4. Çıkış")
    sec=input("Seçiniz:")
    if sec=="4":
        break
    elif sec=="1":
        print(*"EKLE")
        adi=input("Adınız:")
        soyadi=input("Soyadınız:")
        telno=input("Telefon Numaranız:")
        tel.append([adi,soyadi,telno])
    elif sec=="2":
        print(*"SİL")
        kayitno=int(input("Silmek İstediğniz Kayıt Numarası:"))
        del tel[kayitno-1]
    elif sec=="3":
        print(*"LİSTELE")
        print("{:<5}{:<15}{:<15}{:<15}".format("Sıra","Adı","Soyadı","Telefon Numarası"))
        sira=0
        for kayit in tel:
            sira+=1
            print("{:<5}{:<15}{:<15}{:<15}".format(sira,kayit[0],kayit[1],kayit[2]))
        input("Devam etmek için enter'a bas")