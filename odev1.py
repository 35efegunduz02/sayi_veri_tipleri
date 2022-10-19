url = "https://teknolojiaihl.meb.k12.tr"

# 1- "url" içinde kaç karakter olduğunu yazdır.
print(len(url))

# 2- "url" içindeki "meb" sözcüğünü ekrana yazdırın.
print(url[23])
print(url[24])
print(url[25])
# 3- "url" içindeki "k12" sözcüğünü ekrana yazdırın.
print(url[27])
print(url[28])
print(url[29])
# 4- Kullanıcıdan adını, en sevdiği yemeği alın ve cümle içinde yazdırın.
# ÖRNEK CÜMLE: Adınız: Eren. En sevdiğiniz yemek: Pırasa
ad = input("isminiz: ")
yemek = input("en sevdiğiniz yemek: " )
print("isminiz: "+ ad + " , en sevdiğiniz yemek: "+ yemek)
# 5- Öğrencinin 2 sınav notunu alın. Notunu hesaplayıp cümle içinde yazdırın.
# 1. sınav oranı: %35
# 2. sınav oranı: %65
# ÖRNEK CÜMLE: 1. sınav: 70 puan, 2. sınav: 90 puan, Notunuz: 83.0
x = 0.35
y = 0.65
print( (70*x)+(90*y))
# 6- Kullanıcının adını alın ve yan yana 100 defa yazdırın.
isim = input("isminiz: ")
print(isim*100)