# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown" }
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Python", "Machine Learning", "Data Science"}
type(s)

# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.

text = "The goal is to turn data info information, and information into insight."

text.upper().replace(",", " ").replace(".", " ").split()

# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakınız.
len(lst)

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
data_list = lst[0:4]
lst
data_list

# Adım 4: Sekizinci indeksteki elemanı siliniz.
lst.pop(8)
lst.remove("N")

# Adım 5: Yeni bir eleman ekleyiniz.
lst.append("Zehra")

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz
lst.insert(8, "N")

# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

# Adım 1: Key değerlerine erişiniz.
dict.keys()

# Adım 2: Value'lara erişiniz.
dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.update({"Daisy": ["England", 13]})
dict

dict["Daisy"][1] = 14
dict

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})
dict

# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")
dict

dict.popitem() #eklenen son ögeyi siler.

# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]
def func(l):
    A = []
    B = []

    for n in l:
   if n % 2 == 0:
       A.append(n)
   else:
       B.append(n)

       return A, B
A, B = func(l)

print("Tek sayılar", B)
print("Çift Sayılar", A)

# Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,". öğrenci: ",x)


for index, derece in enumerate(ogrenciler, 1):
    if index < 4:
        print("Mühendislik Fakültesi {} . öğrenci: {}".format(index,derece))
    if index >= 4 :
        print("Tıp Fakültesi {} . öğrenci: {}".format(index -3, derece))

# Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list(zip(ders_kodu, kredi, kontenjan))

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
  print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

#  Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)
