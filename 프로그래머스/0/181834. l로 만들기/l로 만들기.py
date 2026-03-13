def solution(myString):
    myList = list(myString)

    for i in range(len(myList)):
        if ord('l') > ord(myList[i]):
            myList[i] = 'l'
            
    return "".join(myList)