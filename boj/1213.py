import collections
import string

alphabets = list(string.ascii_uppercase)
counter = collections.Counter(input())

answer = ''
for alphabet in alphabets:
    while True:
        if counter[alphabet] >= 2:
            counter[alphabet] -= 2
            answer += alphabet
        else:
            break

remain = ''
for key, value in counter.items():
    if value > 0:
        remain += key

if remain != remain[::-1]:
    print('I\'m Sorry Hansoo')
else:
    reverse = answer[::-1]
    print(answer + remain + reverse)
