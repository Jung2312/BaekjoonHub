from collections import Counter

def solution(clothes):
    
    answerdict = Counter(row[1] for row in clothes)
    
    i = 1
    for cnt in answerdict.values():
        i *= (cnt + 1)

    return i - 1