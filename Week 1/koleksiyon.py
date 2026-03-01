students = ["Ali", "Ayşe", "Mehmet", "Fatma"]
print(students[0])  # Ali
print(students[-1])  # Fatma
students.append("Ahmet")
print(students)  # ['Ali', 'Ayşe', 'Mehmet', 'Fatma', 'Ahmet']
students.insert(2, "Zeynep")
print(students)  # ['Ali', 'Ayşe', 'Zeynep', 'Mehmet', 'Fatma', 'Ahmet']
students.remove("Mehmet")
print(students)  # ['Ali', 'Ayşe', 'Zeynep', 'Fatma', 'Ahmet']
students.pop(1)
print(students)  # ['Ali', 'Zeynep', 'Fatma', 'Ahmet']

for student in students:
    print(student)

coordinates = (10, 20)
print(coordinates[0])  # 10
print(coordinates[1])  # 20
#coordinates.append(30)  # HATA: AttributeError: 'tuple' object has no attribute 'append'

person = {"name": "Ahmet", "age": 30, "city": "Istanbul"}
print(person["name"])  # Ahmet
print(person["age"])   # 30
person["age"] = 31
print(person)  # {'name': 'Ahmet', 'age': 31, 'city': 'Istanbul'}
person["country"] = "Turkey"
print(person)  # {'name': 'Ahmet', 'age': 31, 'city': 'Istanbul', 'country': 'Turkey'}

for key, value in person.items():
    print(key + ":", value)

numbers = {1, 2, 3, 4, 5,5,3,2}
print(numbers)  # {1, 2, 3, 4, 5}