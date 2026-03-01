print("Merhaba dünya!")

name = "Ahmet"
age = 30
isTrue = True
print("Ad:", name)
print("Yaş:", age)  
print("Doğru mu?", isTrue)

age1 = "5"
print("Yaş:", age)
age2 = 5
print("Yaş:", age)

#total = age1 + age2 #HATA: TypeError: unsupported operand type(s) for +: 'str' and 'int'

name = input("Adınızı girin: ")
print("Merhaba, " + name + "!")

number1 = int(input("Bir sayı girin: "))
number2 = int(input("Başka bir sayı girin: "))
total = number1 + number2
total2 = number1 * number2
total3 = number1 / number2
total4 = number1 - number2
total5 = number1 % number2
total6 = number1 ** number2
total7 = number1 // number2
print("Toplam:", total)
print("Çarpım:", total2)
print("Bölüm:", total3)
print("Fark:", total4)
print("Modül:", total5)
print("Üs:", total6)
print("Tam Bölüm:", total7)

name = input("Adınızı girin: ")
age = int(input("Yaşınızı girin: "))

future_age = age + 5
print("Merhaba, " + name + "! 5 yıl sonra yaşınız " + str(future_age) + " olacak.")