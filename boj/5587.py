N = int(input())

cards = [0] * (2 * N + 1)
cards[0] = -1
for _ in range(1, N + 1):
    card = int(input())
    cards[card] = 1

A, B = [], []
for card, owner in enumerate(cards):
    # 근상
    if owner == 0:
        B.append(card)
    # 상근
    elif owner == 1:
        A.append(card)
table_card = 0
while True:
    # 상근 차례
    for index, card in enumerate(A):
        if table_card < card:
            table_card = card
            del A[index]
            break
    # 아무것도 내지 못했다면
    else:
        table_card = 0
    if not A:
        break

    # 근상 차례
    for index, card in enumerate(B):
        if table_card < card:
            table_card = card
            del B[index]
            break
    # 아무것도 내지 못했다면
    else:
        table_card = 0
    if not B:
        break

print(len(B))
print(len(A))
