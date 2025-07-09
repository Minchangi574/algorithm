def solution(arr, queries):
    answer=[]
    for s,e,k in queries:
        min_=[]
        for i in range(s,e+1):
            if arr[i]>k:
                min_.append(arr[i])
        if len(min_)==0:
            answer.append(-1)
        else:
            answer.append(min(min_))
        
    return answer