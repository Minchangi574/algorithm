def solution(myString):
    answer = myString.split("x")
    string=[s for s in answer if s!=""]
    answer_=string.sort()
    return string