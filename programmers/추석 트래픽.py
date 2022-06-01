def solution(lines):
    answer = 0

    time_table = []

    # 순회
    for line in lines:
        # 문자열 전처리
        temp, S, T = line.split()
        finish_hour, finish_min, finish_sec = S.split(':')
        finish_hour, finish_min, finish_sec = int(finish_hour), int(finish_min), int(finish_sec.replace('.', ''))
        finish_time = finish_hour * 60 * 60 * 1000 + finish_min * 60 * 1000 + finish_sec
        process_time = int(float(T[:-1]) * 1000)
        start_time = finish_time - process_time + 1

        time_table.append([start_time, finish_time])

    for i in range(len(time_table)):
        count = 0
        current_start, current_end = time_table[i]
        for j in range(i, len(time_table)):
            next_start, next_end = time_table[j]
            if current_end > next_start - 1000:
                count += 1
        answer = max(answer, count)

    return answer
