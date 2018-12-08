with open('referat.txt', 'r', encoding='utf-8') as tekst:
    content = tekst.read()
    print(content)


with open('referat.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.replace('.', '!')
        print(line + ' The length of the line is: ' + str(len(line)))

def words_count(text_file):
    with open(str(text_file), 'r', encoding='utf-8') as file:
        for line in file:
            length = len(line.split())
            if length >0:
                print(length)


my_file = 'referat.txt'
words_count(my_file)


with open('referat.txt', 'r+', encoding='utf-8') as f:
    list_text = []
    for line in f:
        list_text.append(line.replace('.', '!'))
    updated_text = ''.join(list_text)
    f.seek(0)
    f.write(updated_text)
    f.truncate()


