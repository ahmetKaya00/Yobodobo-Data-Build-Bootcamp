def save_note(note):
    with open("notlar.txt", "a", encoding="utf-8") as file:
        file.write(note + "\n")

def list_notes():
    with open("notlar.txt", "r", encoding="utf-8") as file:
        notes = file.readlines()
        for note in notes:
            print(note.strip())

while True:
    print("1. Not Ekle")
    print("2. Notları Listele")
    print("3. Çıkış")
    choice = input("Seçiminizi yapın: ")

    if choice == "1":
        note = input("Notunuzu girin: ")
        save_note(note)
        print("Not kaydedildi.")
    elif choice == "2":
        print("Notlar:")
        list_notes()
    elif choice == "3":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")