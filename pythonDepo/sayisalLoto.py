import random

yeni_sayi = 0
sayisal_loto = []
girilen_sayilar = []
kazanan_sayilar = 0

while (len(sayisal_loto) < 6):
    yeni_sayi = random.randrange(1, 100)
    if (yeni_sayi not in sayisal_loto):
        sayisal_loto.append(yeni_sayi)

while (len(girilen_sayilar) < 6):
    yeni_sayi = int(input("1 ile 100 arası sayı giriniz: "))
    if (yeni_sayi not in girilen_sayilar and (yeni_sayi <= 100 or yeni_sayi > 0)):
        girilen_sayilar.append(yeni_sayi)

for sayi in sayisal_loto:
    for asayi in girilen_sayilar:
        if (sayi == asayi):
            kazanan_sayilar += 1

print("Tutturduğunuz sayı " + str(kazanan_sayilar))

print("Sayısal Loto Numaraları")

print(sayisal_loto)

