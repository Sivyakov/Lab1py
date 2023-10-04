#1
integer_array = [12349, 2349, 549, 1949, 975, 486, 1248, 5749]
for number in integer_array:
    if number % 100 == 49:
        print(number)


#2
matrix = [
    [1,     2,      3,      4],
    [5,     6,      7,      8],
    [9,     10,     11,    12],
    [13,    14,     15,     16]
]
n = len(matrix)
upper_quarter_sum = 0
for i in range(n // 2):
    for j in range(i + 1, n - i - 1):
        upper_quarter_sum += matrix[i][j]
print(f"Сумма элементов верхней четверти: {upper_quarter_sum}")

#3
heights = list(map(int, input("Введите рост каждого человека в строю через пробел: ").split()))
petes_height = int(input("Введите рост Пети: "))
position = 1
for height in heights:
    if petes_height <= height:
        position += 1
    else:
        break
print("Петя должен встать на позицию:", position)
#5
countries_cities = {
    "Россия": ["Москва", "Санкт-Петербург", "Новосибирск"],
    "США": ["Нью-Йорк", "Лос-Анджелес", "Чикаго"],
    "Франция": ["Париж", "Марсель", "Лион"]
}

cities = ["Москва", "Лос-Анджелес", "Париж"]

for city in cities:
    for country, city_list in countries_cities.items():
        if city in city_list:
            print(f"{city} находится в стране {country}")

