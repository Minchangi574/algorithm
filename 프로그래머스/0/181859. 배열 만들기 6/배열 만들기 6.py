def solution(arr):
    answer = []
    for i in arr:
        if answer==[]:
            answer.append(i)
        elif answer[-1]==i:
            answer.pop() # 맨 끝 삭제
        else:
            answer.append(i)
    if answer==[]:
        answer.append(-1)
    return answer