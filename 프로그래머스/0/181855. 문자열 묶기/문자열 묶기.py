def solution(strArr):
    answer = {}
    num=[]
    for i in strArr:
        num.append(len(i))
    for item in num:
        if item in answer:
            answer[item]+=1
        else:
            answer[item]=1
    return max(answer.values())