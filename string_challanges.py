# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
count_a = 0
for l in word:
    if l.lower() == 'а':
        count_a += 1
print(f"The amount of a is: {count_a}")


# Вывести количество гласных букв в слове
word = 'Archangelstk'
vowels = 'aeuio'
vowels_count = 0
for l in word:
    if l.lower() in vowels:
        vowels_count += 1
print(vowels_count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for w in sentence.split():
    print(w[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sum_length = 0
for w in sentence.split():
    sum_length += len(w)
print(sum_length/len(sentence.split()))
