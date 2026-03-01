def selamla():
    print("Merhaba, nasılsın?")

selamla()

def selamla2(name = "Misafir"):
    print("Merhaba, " + name + "!")

selamla2("Ahmet")

def topla(a, b):
    return a + b

sonuc = topla(5, 3)
print("Toplam:", sonuc)

def deger(*args):
    print("Verilen değerler:", args)

deger(1, 2, 3, "Ahmet", [1, 2, 3])

def keyword_args(**kwargs):
    print("Verilen anahtar kelime argümanları:", kwargs)
keyword_args(name="Ahmet", age=30, city="Istanbul")

# Lambda fonksiyonu: tek satırda tanımlanan anonim fonksiyon
kare = lambda x: x ** 2
print("5'in karesi:", kare(5))

# Lambda fonksiyonu: iki sayıyı toplayan anonim fonksiyon
topla_lambda = lambda a, b: a + b
print("3 + 4 =", topla_lambda(3, 4))

x = 15
def fonksiyon():
    x = 5
    x += 5
    print("Fonksiyon içindeki x:", x)

fonksiyon()
print("Fonksiyon dışındaki x:", x)

