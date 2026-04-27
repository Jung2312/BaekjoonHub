import collections as col

def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    answer = col.Counter(participant) - col.Counter(completion)

    return list(answer.keys())[0]