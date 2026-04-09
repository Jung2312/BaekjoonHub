import collections as cs

def solution(participant, completion):
    answer = cs.Counter(participant) - cs.Counter(completion)
    return list(answer)[0]