def solution(numLog):
    answer=[]
    for i in range(len(numLog)-1):
        if numLog[i]+1==numLog[i+1]:
            answer.append('w')
        elif numLog[i]-1==numLog[i+1]:
            answer.append('s')
        elif numLog[i]+10==numLog[i+1]:
            answer.append('d')
        elif numLog[i]-10==numLog[i+1]:
            answer.append('a')
        else:
            answer.append('1')
    a_answer="".join(answer)
    return a_answer