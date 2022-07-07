# input
word = input()
table = set()
for length in range(1, len(word) + 1):
    for i in range(len(word) - (length - 1)):
        sub_word = word[i:i + length]
        table.add(sub_word)

print(len(table))
