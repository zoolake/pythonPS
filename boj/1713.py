import sys


class Student:
    def __init__(self, no, count):
        self.no = no
        self.count = count


N = int(input())
M = int(input())
students = list(map(int, input().split()))

answer = []
for student in students:
    # (이미 사진이 올라간 경우) 추천받은 학생의 사진의 추천 횟수를 올린다.
    for i in range(len(answer)):
        if student == answer[i].no:
            answer[i].count += 1
            break
    else:
        # 다 찼다면 가장 추천이 적은 학생의 사진을 내린다.
        if len(answer) == N:
            min_index = -1
            min_count = sys.maxsize
            for i in range(len(answer)):
                if min_count > answer[i].count:
                    min_index = i
                    min_count = answer[i].count
            if min_index != -1:
                del answer[min_index]
        # 새로 추천받은 학생의 사진을 올린다.
        answer.append(Student(student, 1))

answer.sort(key=lambda s: s.no)
for i in range(len(answer)):
    print(answer[i].no, end=' ')
