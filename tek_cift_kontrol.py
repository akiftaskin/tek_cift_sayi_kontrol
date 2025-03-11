# Kullanıcıdan giriş alacağız.
sayi = int(input("Bir sayı girin: "))

if sayi < 0:
    print("Negatif sayı girdiniz!")
elif sayi % 2 == 0:
    print(f"{sayi} bir çift sayıdır.")
else:
    print(f"{sayi} bir tek sayıdır.")
