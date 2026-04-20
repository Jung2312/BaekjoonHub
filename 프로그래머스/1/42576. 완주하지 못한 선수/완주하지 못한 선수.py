import collections as col

def solution(participant, completion):
    answer = col.Counter(participant) - col.Counter(completion)
    return list(answer.keys())[0]