print(5>3)

age = 20
if age >= 18:
    print("Reşitsiniz.")

score= 69
if score >= 90:
    print("Mükemmel!")
elif score >= 80:
    print("Çok İyi!")
elif score >= 70:
    print("İyi!")
else:
    print("Daha çok çalışmalısınız.")

if age >= 18 and age < 65:
    print("Çalışma yaşındasınız.")
elif age >= 65:
    print("Emeklilik yaşındasınız.")

is_student = False
if not is_student:
    print("Öğrenci değilsiniz")

try:
    score = int(input("Sınav notunuzu girin: "))
    if score >= 90:
        print("Mükemmel!")
    elif score >= 80:
        print("Çok İyi!")
    elif score >= 70:
        print("İyi!")
    else:
        print("Daha çok çalışmalısınız.")
except:
    print("Geçersiz giriş! Lütfen bir sayı girin.")