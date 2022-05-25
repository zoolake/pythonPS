import math
import collections


def solution(fees, records):
    answer = []
    # records 순회하면서 주차 시간 처리
    car_in_time = collections.defaultdict(str)
    car_time = collections.defaultdict(int)
    car_fee = collections.defaultdict(int)
    for record in records:
        time, car, flag = record.split()

        if flag == 'IN':  # 입차
            car_in_time[car] = time
        else:  # 출차
            in_time = car_in_time[car]
            car_time[car] += calculate_time(in_time, time)
            del car_in_time[car]

    # 출차 기록이 없는 경우 일괄 출차 처리
    for car, in_time in car_in_time.items():
        car_time[car] += calculate_time(in_time, '23:59')

    # 일괄 요금 처리
    for car, time in car_time.items():
        car_fee[car] += calculate_fee(time, fees)

    sorted_car_fee = dict(sorted(car_fee.items()))
    for car, fee in sorted_car_fee.items():
        answer.append(fee)

    return answer


def calculate_time(in_time, out_time):
    in_hour, in_minute = list(map(int, in_time.split(':')))
    out_hour, out_minute = list(map(int, out_time.split(':')))
    return (out_hour - in_hour) * 60 + (out_minute - in_minute)


def calculate_fee(time, fees):
    fee = fees[1]
    if time > fees[0]:
        time -= fees[0]
        fee += math.ceil(time / fees[2]) * fees[3]
    return fee
