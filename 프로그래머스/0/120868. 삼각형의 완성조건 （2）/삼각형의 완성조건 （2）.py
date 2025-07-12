def solution(sides):
    a=max(sides)
    b=min(sides)
    count=0
    h=a+b
    for i in range(a+1): # a가 긴거 -> b+i > a
        if a<b+i:
            count+=1
            print("a가 긴거: ",i)
            
    for c in range(h): # 받는값이 긴거 -> a+b > c
        if c>a: # c는 a보다 긴 값이므로
            count+=1
            print("받는값이 긴거: ",c)
            
    return count