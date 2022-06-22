target = input()

num = 1
index = 0
while True:
    if index >= len(target):
        num -= 1
        break

    # 포함
    string_num = str(num)
    for i in range(len(string_num)):
        if target[index] == string_num[i]:
            index += 1
            if index >= len(target):
                break
    num += 1

print(num)
