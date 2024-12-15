# #işareti yorum satırıdır.
#SAYILAR VE STRINGLERE GİRİŞ
print("Merhaba Burak!")
print(type("Selam"))
print(type(9.9))
print(9)
print("--------------------------")
#STRINGLERE YAKINDAN BAKALIM
# ' YA DA "" STRINGTIR.
print(type(123)) #tırnaksız sayı yazıldığında int olarak döner 
print(type("123")) #tırnak içine aldığımızda string olarak döndü
print("a" + "b") #bu şekilde yazdığımızda birleşir. eğer arada boşluk istersen  b nin yanına bir boşluk eklenebilir.
# print("a" - "b") işleminde eksi burada hatalıdır iki string arasına koyulmaz. + bir araya gelmek için kullanılır.
print("a "*5) #bu işlem 5 kere a yazdırmaya yarar. eğer bölüm / işareti ekleseydik hata alırdık.
print("--------------------------")
#STRING METODLARI -len()
a = "Geleceğe yazanlar"
print(a) #atama yapmak
print(len(a)) # len burada uzunluğu verir.
b=9
c=8
print(b*c) #çarpma işlemi
print("--------------------------")
#STRING METODLARI upper() & lower()
x= "naber"
print(x.upper())
print(x.lower())
print(x.islower()) 
print("----------------------------")
#STRING METODLARI replace()
y= "geleceği yazanlar"
print(y.replace("e","a"))  #değiştirilmek istenileni birinciye ne ile değişeceğini ikinciye yazman gerekir.
print("-------------------------------")
#STRING METODLARI -strip()
u = " geleceği yazanlar*"
print(u.strip("*")) #strip burada başta ve sonda olanları siler
#eğer belirli şeyi silmek istersek içine belirtiriz.
print("---------------------------------")
#STRING GENEL BAKIS
k = "geleceği yazanlar"
print(k.capitalize()) # cümlenin ilk harfini büyütür.
print(k.title())  # her kelimenin ilk harfini büyütür.
print("-----------------------------------")
#SUBSTRINGLER
o = "geleceği yazanlar"
print(o[0]) #alacağı harfi kapalı paratezde verdi.
print(o[0:3]) # : işareti 'e kadar ifadesini verir.
print("-------------------------------------")
#DEĞİŞKENLER
#TYPE DÖNÜŞÜMLERİ
#input kullanıcıdan bilgi almak için
print("Adınız nedir: ")
esek = input()
print("Hoş Geldiniz ",esek)
#---------------------------------
print("Lütfen birinci sayıyı giriniz: ")
toplama1= input()
print("Lütfen ikinci sayıyı giriniz: ")
toplama2= input()

toplam = int(toplama1) * int(toplama2)
print("İki sayının toplamı=", toplam)
print(toplam)
print("---------------------------------")
#print
print("geleceği","yazanlar", sep = "_") #burada iki boşluk arasına bir şey koymak istersek eğer sep parametresi ile işlem yapabiliriz.

