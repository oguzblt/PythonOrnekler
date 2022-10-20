while True:
    print(*"TELEFON DEFTERİ")
    print("1. Toplama")
    print("2. Çarpma")
    print("3. Çıkarma")
    print("4. Bölme")
    print("5. Çıkış")
    islem = input("Seçiniz:")
    if islem=="5":
        print("çıkış başarılı")
        break;
    elif islem=="1":
        sayi1=int(input("toplama işlemi için birinci sayıyı yaz: "))
        sayi2=int(input("toplama işlemi için ikinci sayıyı yaz: "))
        print(sayi1,"+",sayi2,"=",sayi1+sayi2,)
    elif islem=="2":
        sayi3=int(input("çarpma işlemi için birinci sayıyı yaz: "))
        sayi4=int(input("çarpma işlemi için ikinci sayıyı yaz: " ))
        print(sayi2,"x",sayi3,"=",sayi3*sayi4)
    elif islem=="3":
        sayi5=int(input("çıkarma işlemi için birinci sayıyı yaz: "))
        sayi6=int(input("çıkarma işlemi için birinci sayıyı yaz: "))
        print(sayi5,"-",sayi6,"=",sayi5-sayi6)
    elif islem=="4":
        sayi7=int(input("bölme işlemi için birinci sayıyı yazınız: "))
        sayi8=int(input("bölme işlemi için ikinci sayıyı yazınız: "))
        print(sayi7,"/",sayi8,"=",sayi7/sayi8)
        input("devam etmek için entera basınız")