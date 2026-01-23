from itertools import count

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f'Task 01: {adwentures_of_tom_sawer}')

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f'Task 02: {adwentures_of_tom_sawer}')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(f'Task 03: {adwentures_of_tom_sawer}')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count = 0
for i in adwentures_of_tom_sawer:
    if i == "h":
        count += 1
print(f'Task 04: {count}')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
countUpWords = 0
words_list = adwentures_of_tom_sawer.split()
for word in words_list:
    if word[0].isupper():
        countUpWords += 1
print(f'Task 05: {countUpWords}')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
words_list = adwentures_of_tom_sawer.split()
occur = 0
for word in range(len(words_list)):
    if words_list[word] == 'Tom':
        occur += 1
        if occur == 2:
            print(f'Task 06: {word}')
            break

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
print(f'Task 07: {adwentures_of_tom_sawer_sentences}')

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f'Task 08: {adwentures_of_tom_sawer_sentences[3].lower()}')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
adwentures_of_tom_sawer_sentences_initial = adwentures_of_tom_sawer.split('.')
for sentence in adwentures_of_tom_sawer_sentences_initial:
    if sentence.strip().startswith("By the time"):
        print(f'Task 09: The sentence starts with \'By the time\' is present on {adwentures_of_tom_sawer_sentences_initial.index(sentence)} index')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
for i in range(len(adwentures_of_tom_sawer_sentences)):
    adwentures_of_tom_sawer_sentences[i] = adwentures_of_tom_sawer_sentences[i].strip()
adwentures_of_tom_sawer_sentences = [s for s in adwentures_of_tom_sawer_sentences if s]
lastSentence = adwentures_of_tom_sawer_sentences[-1]
print(lastSentence)
print(f'Task 10: word count in the last sentence is {len(lastSentence.split())}')