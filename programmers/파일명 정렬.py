class File:
    def __init__(self, head, number, tail, index):
        self.head = head
        self.number = number
        self.tail = tail
        self.index = index

    def __lt__(self, other):
        if self.head.lower() < other.head.lower():
            return True
        elif self.head.lower() == other.head.lower():
            return int(self.number) < int(other.number)
        else:
            return self.index < other.index


def solution(files):
    answer = []

    temp = []
    for index in range(len(files)):
        # 문자열 전처리
        head, number, tail = process(files[index])
        temp.append(File(head, number, tail, index))

    temp.sort()

    for data in temp:
        head, number, tail = data.head, data.number, data.tail
        answer.append(head + number + tail)

    return answer


def process(file):
    head, number, tail = [], [], []
    head_flag, number_flag = False, False
    for i in range(len(file)):
        current = file[i]
        # head를 채우는 중
        if not head_flag:
            if not current.isdigit():
                head.append(current)
            else:
                head_flag = True

        if head_flag and not number_flag:
            if current.isdigit():
                number.append(current)
            else:
                number_flag = True

        if head_flag and number_flag:
            tail.append(current)

    return [''.join(head), ''.join(number), ''.join(tail)]


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
