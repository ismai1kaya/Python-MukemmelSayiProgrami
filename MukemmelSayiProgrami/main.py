print("---------------\nMükemmel Sayı Programı\n"
      "----------------")

alinan_deger = int(input("Lütfen bir sayi giriniz:"))

i = 1
toplam = 0

while(i < alinan_deger):
    if(alinan_deger % i == 0):
        toplam+=i
    i+=1

if(toplam == alinan_deger):
    print("{} Mükemmel sayıdır...".format(alinan_deger))
else:
    print("{} Mükemmel sayi değildir...".format(alinan_deger))
