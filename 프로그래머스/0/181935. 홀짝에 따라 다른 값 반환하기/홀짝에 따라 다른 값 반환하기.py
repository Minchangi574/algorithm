def solution(n):
    total=0
    for i in range(n+1):
        if n%2==0:
            if i%2==0:
                total=total+i**2
        else:
            if i%2!=0:
                total=total+i
    return total