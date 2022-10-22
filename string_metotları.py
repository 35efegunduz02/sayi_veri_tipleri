okul = "sancaktepe TEKNOLOJİ anadolu imam hatip lisesi"
makale= "HOYA, üniversitelilerin gözünden geleceğin göz sağlığı teknolojilerini görmek için etkileyici bir ‘makale yarışması’ başlattı. Alanında ilk olan ve “Geleceği Gören Teknoloji” ismiyle üniversite öğrencilerine yönelik düzenlenen yarışmada dereceye girenler iPhone 12, Dell Bilgisayar ve Apple tabletin sahibi olacak. Yarışma başvurusu için son tarih 27 Haziran 2022.Sahip olduğu üstün “optik teknolojileri” ile sektör liderlerinden olan HOYA, üniversitelilere özel bir makale yarışması başlattı. Sektöründe ilk olacak yarışmada bilginin üretimi ve teknolojinin gelişmesi arasındaki ilişkiye dikkat çekilirken, üniversitelilerin gözünden geleceğin göz sağlığı teknolojilerinin neler olabileceğine dair makaleleri bekleniyor.Önümüzdeki 50 yılda göz sağlığı teknolojileri nasıl gelişecek?Teknoloji ve bilgi üretimi arasındaki ilişkinin önemine dikkat çekmeyi amaçlayan Geleceği Gören Teknoloji Makale Yarışması’na üniversitelerin her bölümünden ve her sınıfından öğrenciler katılabiliyor. Katılımcılar, 1.000 kelime sınırlaması olan makale yarışmasında gelecek 50 yılda optik cam sektöründe hangi ihtiyaçları karşılamak üzere ne gibi teknolojiler üretileceği, gelişen teknolojinin önümüzdeki yıllarda optik cam sektörü için ne boyutta olacağı, hangi amaçlar için kullanılabileceği, kullanıcıların istek ve beklentilerinin nasıl değişeceği gibi konuyu birçok açıdan değerlendirebilecekler. Sadece Türkçe makalelerin alındığı yarışmada, deneme, köşe yazısı türünde yazılar da kabul edilirken, alıntı kullanılması durumunda kaynaklarının belirtilmesi de önemli olacak."
# tüm karakterleri büyük harf yapalım: upper()
print(okul.upper())

# tüm karakterleri küçük harf yapalım: upper()
print(okul.lower())

# her kelimenin ilk harfini büyük yapalım: title()
print(okul.title())

# karakter dizisinin ilk karakterini büyük
# diğer karakterlerini küçük harf yapalım
print(okul.capitalize())

# belirli bir ifadenin kaç defa yer aldığını bulalım: count()
print((okul.count("e"))+(okul.count("s")))

# metni önce lower ile küçük harflere
# çeviriyoruz ardından ifadenin kaç defa yer aldığını
# buluyoruz büyük küçük harfe duyarlı
print(makale.lower().count("teknoloji"))

# soldaki ve sağki boşluk karakterlerini temizleyelim: strip()      alt gr + tire = |
ad = input("adınız: ")
print(ad.strip() + "|")

# soldaki ve sağdaki belirli karakterlerini temizleyelim: strip("ifade")
urun_kodu = "HEP20221022HEP"
print(urun_kodu.strip("HEP"))

# soldaki boşluk veya belirli ifadeyi temizleyelim: lstrip()
print(ad + "|") #adı boşlukla gönder
print(ad.rstrip() + "|")
print(urun_kodu.lstrip("HEP"))

# karakter dizisini bölelim: split()
print(okul.split())

# böldüğümüz ve listeye dönüşen ifadeleri birleştirelim: join()
kelimeler = okul.split()
print(kelimeler)
print("\n".join(kelimeler))

# ortalayıp çıktı verme
print("eren".center(25))