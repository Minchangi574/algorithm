def solution(myString):
    answer=[]
    string=list(myString)
    count=0
    for i in string:
        if i!='x':
            count+=1
        else:
            answer.append(count)
            count=0
    answer.append(count) # 마지막 X
    
    return answer