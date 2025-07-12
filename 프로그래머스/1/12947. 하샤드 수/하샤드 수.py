def solution(x):
    a=str(x)
    b=len(a)
    num=0
    for i in range(b):
        num+=int(a[i])
    if x%num==0:
        answer=True
    else:
        answer=False


    return answer