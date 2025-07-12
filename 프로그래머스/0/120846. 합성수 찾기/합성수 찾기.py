def solution(n):
    num=[]
    for i in range(n+1):
        a=0
        for j in range(i):
            if i%(j+1)==0:
                a+=1
                if a>=3:
                    num.append(i)
                    break
            
    return len(num)