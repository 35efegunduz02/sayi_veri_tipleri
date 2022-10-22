# boş bir liste tanımlayalım
liste = []
print(liste)
print(type(liste))
okul = "sancaktepe teknoloji anadolu imam hatip lisesi"
kelimeler = okul.split()
print(kelimeler)

# belirli sıradaki kelimeleri yazdıralım
print(kelimeler[0])
print(kelimeler[1])
print(kelimeler[2])
print(kelimeler[3])
print(kelimeler[4])
print(kelimeler[5])

print(kelimeler[-1])
print(kelimeler[-6])


ad = "efe gündüz"
print(ad[0]) #e
print(ad[4:]) #gündüz
print(ad[0:12:2])
print(ad[-7:-14:-1])
print(ad[::-1])


# listeler içerisinde farklı türden veriler olabilir
liste = [1, 12.3, "python", True, [1, 2, 3]]
print(liste[-1][-1])
print(liste[4][-1])
print(liste[4][2])

# iki listeyi birleştirme
liste2 = [1,2,3]
liste3 = [4,5,6]
liste4 = liste2 +liste3
liste5 = liste3 + liste2
print(liste4)
print(liste5)