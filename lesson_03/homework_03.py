from lesson_01.homework_01 import total_price

alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
azovSea = 37800
blackSea = 436402
total_squares = azovSea + blackSea
print(f'The Azov and Black seas cover {total_squares} km2 together')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
totalGoodsCount = 375291
first_secondGoodsCount = 250449
second_thirdGoodsCount = 222950
firstGoodsCount = totalGoodsCount - second_thirdGoodsCount
secondGoodsCount = first_secondGoodsCount - firstGoodsCount
thirdGoodsCount = second_thirdGoodsCount - secondGoodsCount
print(f'The first store has {firstGoodsCount} goods. \n'
      f'The second store has {secondGoodsCount} goods. \n'
      f'The third store has {thirdGoodsCount} goods.')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payPerMonth = 1179
monthCount = 1.5 * 12
totalPrice = int(payPerMonth * monthCount)
print(f'The PC price is {totalPrice} grn.')

# task 07
"""
 Знайди остачу від діленя чисел:
 a) 8019 : 8     d) 7248 : 6
 b) 9907 : 9     e) 7128 : 5
 c) 2789 : 5     f) 19224 : 9
"""
firstList = [8019, 9907, 2789, 7248, 7128, 19224]
secondList = [8, 9, 5, 6, 5, 9]
for i in range(len(firstList)):
    print(f'Remainder from division {firstList[i]} : {secondList[i]} = {firstList[i] % secondList[i]}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
quantitiesGoods = [4, 2, 4, 1, 3]
pricesGoods = [274, 218, 35, 350, 21]
total = 0
for i in range(len(quantitiesGoods)):
    total += quantitiesGoods[i] * pricesGoods[i]
print(f'Total cost of Irynka\'s birthday party: {total} grn')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photosCount = 232
photoPerPage = 8
pagesNeeded = photosCount // photoPerPage
print(f'Ihor needs {pagesNeeded} pages in album for his photos')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
vacationDistance = 1600
needFuelPer100 = 9
fullTankFuel = 48
totalFuel = vacationDistance / 100 * needFuelPer100
azsStops = totalFuel // fullTankFuel
print(f'Total fuel needed for current vacation: {totalFuel}\n'
      f'Count of AZS stops: {azsStops}')