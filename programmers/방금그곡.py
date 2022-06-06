def solution(m, musicinfos):
    answer = ''

    m = process(m)
    for musicinfo in musicinfos:
        start, end, name, codes = musicinfo.split(',')
        time_diff = get_time_diff(start, end)

        codes = process(codes)
        total_codes = codes * (time_diff // len(codes)) + codes[:(time_diff % len(codes))]

        if m in total_codes:
            if answer == '':
                answer = [name, time_diff, start]
            else:
                # 재생시간이 더 긴 경우
                if answer[1] < time_diff:
                    answer = [name, time_diff, start]
                # 재생시간도 같다면
                elif answer[1] == time_diff:
                    # 더 빨리 입력된 경우
                    if get_time_diff(answer[2], start) < 0:
                        answer = [name, time_diff, start]

    if answer == '':
        return "(None)"

    return answer[0]


def process(codes):
    codes = codes.replace('C#', 'c')
    codes = codes.replace('D#', 'd')
    codes = codes.replace('F#', 'f')
    codes = codes.replace('G#', 'g')
    codes = codes.replace('A#', 'a')
    return codes


def get_time_diff(start, end):
    start_hour, start_minute = list(map(int, start.split(':')))
    end_hour, end_minute = list(map(int, end.split(':')))

    start_total = start_hour * 60 + start_minute
    end_total = end_hour * 60 + end_minute
    return end_total - start_total
