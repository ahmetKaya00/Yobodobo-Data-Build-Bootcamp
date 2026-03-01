import random
print("Merhaba Ahmet")
print("Merhaba Mehmet")

for i in range(5):
    print("Merhaba Dünya!", i)

i = 0
while i < 5:
    print("Merhaba Dünya!", i)
    i += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

secret = random.randint(1, 20)

while True:
    guess = int(input("1 ile 20 arasında bir sayı tahmin edin: "))
    if guess == secret:
        print("Tebrikler! Doğru tahmin.")
        break
    elif guess < secret:
        print("Daha yüksek bir sayı deneyin.")
    elif guess > secret:
        print("Daha düşük bir sayı deneyin.")

