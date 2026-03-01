file = open("veri.txt", "w", encoding="utf-8")
file.write("Merhaba Dünya\n")
file.write("Python programlama dili\n")
file.close()

file = open("veri.txt", "r", encoding="utf-8")
icerik = file.read()
print(icerik)
file.close()

with open("veri.txt", "w", encoding="utf-8") as file:
    file.write("Dosya işlemleri\n")

with open("veri.txt", "r", encoding="utf-8") as file:
    icerik = file.read()
    print(icerik)

with open("veri.txt", "a", encoding="utf-8") as file:
    file.write("Python ile dosya işlemleri\n")