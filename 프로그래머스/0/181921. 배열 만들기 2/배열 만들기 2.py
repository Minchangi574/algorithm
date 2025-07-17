def solution(l, r):
    num=[]
    a=0
    for i in range(l,r+1):
        if '1' in str(i) or '2' in str(i) or '3' in str(i) or '4' in str(i) or '6' in str(i) or '7' in str(i) or '8' in str(i) or '9' in str(i):
            a=1
        else:
            num.append(i)
    if num==[]:
        return [-1]

            

            
    return num