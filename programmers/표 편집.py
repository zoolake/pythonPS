class Node:
    def __init__(self):
        self.prev = -1
        self.next = -1
        self.is_delete = False

    def __str__(self):
        return '{},{},{}'.format(self.prev, self.next, self.is_delete)


def solution(n, k, cmd):
    answer = ''

    # n개의 노드를 갖는 양방향 연결리스트 생성
    linked_list = [Node() for _ in range(n)]
    for i in range(n - 1):
        linked_list[i].next = i + 1
        linked_list[i + 1].prev = i

    # CMD를 읽으면서 연산 진행
    store = []
    for command in cmd:
        line = command.split()
        op, num = line[0], 0
        if len(line) > 1:
            num = int(line[1])

        if op == 'D':
            for _ in range(num):
                k = linked_list[k].next
        elif op == 'U':
            for _ in range(num):
                k = linked_list[k].prev
        elif op == 'C':
            # 이전 노드와 다음 노드를 연결
            current_node = linked_list[k]
            if current_node.prev != -1:
                (linked_list[current_node.prev]).next = current_node.next
            if current_node.next != -1:
                (linked_list[current_node.next]).prev = current_node.prev
            # 삭제되는 노드를 store에 저장
            store.append(k)
            current_node.is_delete = True
            # k 위치 변경
            if current_node.next == -1:
                k = current_node.prev
            else:
                k = current_node.next
        elif op == 'Z':
            # store에서 제일 마지막으로 들어온 노드를 꺼낸다.
            index = store.pop()
            # 노드의 정보를 활용하여 다시 연결 해준다.
            node = linked_list[index]
            if node.prev != -1:
                (linked_list[node.prev]).next = index
            if node.next != -1:
                (linked_list[node.next]).prev = index
            node.is_delete = False

    for node in linked_list:
        if node.is_delete:
            answer += 'X'
        else:
            answer += 'O'

    return answer
