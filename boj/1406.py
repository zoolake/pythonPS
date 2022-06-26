import sys


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return '{}'.format(self.value)


word = input()
M = int(input())

# 양방향 연결리스트 생성
dummy_node = Node('DUMMY')
current_node = dummy_node
for i in range(len(word)):
    next_node = Node(word[i])
    # 두 노드를 연결
    current_node.right = next_node
    next_node.left = current_node
    # 커서 위치 이동
    current_node = next_node

for _ in range(M):
    line = sys.stdin.readline().split()
    op, c = line[0], ''
    if op == 'P':
        c = line[1]
        # 새로운 노드 생성
        new_node = Node(c)
        # 연결
        next_node = current_node.right
        new_node.right = next_node
        new_node.left = current_node
        current_node.right = new_node
        if next_node is not None:
            next_node.left = new_node
        # 커서 이동
        current_node = new_node
    if op == 'L':
        # 맨 앞이 아닌 경우
        if current_node.left is not None:
            current_node = current_node.left
    if op == 'D':
        # 맨 뒤가 아닌 경우
        if current_node.right is not None:
            current_node = current_node.right
    if op == 'B':
        if current_node.value != 'DUMMY':
            left_node = current_node.left
            right_node = current_node.right
            # 현재 커서가 위치한 이전 노드와 다음 노드를 연결
            left_node.right = right_node
            if right_node is not None:
                right_node.left = left_node
            # 커서 이동
            current_node = left_node

node = dummy_node.right
while True:
    if node is None:
        break
    print(node.value, end='')
    node = node.right
