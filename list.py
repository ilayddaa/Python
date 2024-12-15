#VERİ YAPILARI

#LİSTELER
# []
notlar = [90,80,70]
print(type(notlar))

liste = ["a",19.3,99]
print(type(liste))
#1. Değiştirebilir. 2. Kapsayıcıdır.(farklı tipte verileri tutabilir) 3.Sıralıdır.
#del liste
print(liste) # sildiğimiz için liste bulunamadı ve hata verdi.
print("------------------------")
#ELEMAN İŞLEMLERİ
liste1 = [10,20,30]
print(liste1[1])

yeniliste = [10,"a",[30,40,50]]
print(yeniliste[0:2]) # eğer 0dan 2ye kadar dersek 2yi almayız!
print(yeniliste[2][1]) #2. bir listeye denk gelir ve yanındaki kapalaı parantez ile ikinci listeden birinci veriyi çekeriz.
print("------------------------------")
#LİSTELER - ELEMAN DEĞİŞTİRME
liste = ["burak","selin","99","eslem"]
liste[2] = "98"
print(liste)

liste = liste + ["selen"] #bu şekilde yapıldığında listede kalıcı olarak eklenir.
print(liste)

del liste[2] #listede üçüncü veri silindi.
print(liste)
print("-----------------------------")
#LİSTE METODLARI
liste = ["ali","veli","selen"]
liste.append("ilayda") #listeye ilayda adlı veri eklendi.
print(liste)
liste.remove("ilayda") #listeden ilayda adlı veri silindi.
print(liste)
print("--------------------------")
#INSERT 
liste = ["ali", "selen","cansu"]
liste.insert(0,"davut") #silmeden 0. veri yerine yeni bir veri ekler ve sıfırıncı veri birinci veri olarak kalır.
print(liste)
#pop
liste.pop(0) #0.eleman silindi.
print(liste)
print("----------------------------")
#COUNT
liste = ["ali","veli","selen","doruk","ali"]
print(liste.count("ali")) #count işlemi burada tekrarlanan verinin sayını veriyor.

#copy mevut listeyi kopyalar
listeyedek = liste.copy()
print(listeyedek)

#extend iki listeyi birleştirmek için kullanılır.
liste.extend(["a","b",10])
print(liste)

#index
print(liste.index("ali")) #ali'nin kaçıncı indexte olduğunu verir

#reverse
liste.reverse() #elemanları terse çevirir.
print(liste)

#sort
liste = [10,20,40,2]
liste.sort() #küçükten büyüğe sıralar.
print(liste)

#clear
liste.clear()
print(liste) #bütün elemanlar silinir.
print("-------------------------------------------")

#VERİ YAPILARI -TUPLE 
#TUPLE OLUŞTURMA
# kapsayıcıdır. sıralıdır. DEĞİŞTİRİLEMEZ!.
t = ("ali", "veli",1,2,3,4.5,[1,2,3])
t = "ali","veli",1,2,3,4.5,[1,2,3]

#tuple()
t = ("eleman",)
type(t)
print(type)
