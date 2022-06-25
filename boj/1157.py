word = input().lower()

table = [0] * 26
for alphabet in word:
    table[ord(alphabet) - ord('a')] += 1

max_count = 0
max_count_alphabet = []
for index, value in enumerate(table):
    if value > max_count:
        max_count = value
        max_count_alphabet.clear()
        max_count_alphabet.append(chr(index + ord('A')))
    elif value == max_count:
        max_count_alphabet.append(chr(index + ord('A')))

if len(max_count_alphabet) > 1:
    print('?')
else:
    print(max_count_alphabet[0])
