import collections

def solution(survey, choices):
    answer = ''
    
    table = collections.defaultdict(int)
    for types, choice in zip(survey, choices):
        if choice < 4:
            table[types[0]] += (4-choice)
        elif choice > 4:
            table[types[1]] += (choice-4)
    
    type_pair = ['RT','CF','JM','AN']
    for pair in type_pair:
        if table[pair[0]] >= table[pair[1]]:
            answer += pair[0]
        else:
            answer += pair[1]
    
    return answer
