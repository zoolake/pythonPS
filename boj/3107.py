address = input()
groups = address.split(':')

group_count = 0
for group in groups:
    if group != '':
        group_count += 1

zero_group = 8 - group_count
seperator_count = 7

answer = []
flag = True
for group in groups:
    if group == '' and flag:
        while zero_group > 0:
            answer.append('0000')
            zero_group -= 1
            if seperator_count >= 1:
                answer.append(':')
                seperator_count -= 1
        flag = False

    elif group != '':
        new_group = '0' * (4 - len(group)) + group
        answer.append(new_group)
        if seperator_count >= 1:
            answer.append(':')
            seperator_count -= 1
print(''.join(answer))
