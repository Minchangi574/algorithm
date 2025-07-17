def solution(arr):
    stk=[]
    a=0 # stk의 인덱스 번호를 의미
    while a<len(arr):
        if stk==[]:
            stk.append(arr[a])
            a+=1
        elif stk[-1]<arr[a]:
            stk.append(arr[a])
            a+=1
        elif stk[-1]>=arr[a]:
            stk.pop()
        
    return stk