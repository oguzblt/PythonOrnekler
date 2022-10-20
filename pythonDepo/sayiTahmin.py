from random import randrange

rand = randrange(1, 100)
sayac = 0

while True:
    sayac = sayac + 1
    sayi = int(input("1 ile 100 arasında değer girin (0 çıkış):"))
    if (sayi == 0):
        print("Oyunu iptal ettiniz")
        break
    elif sayi < rand:
        print("Yüksek söyle.")
        continue
    elif sayi > rand:
        print("Düşük söyle.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))