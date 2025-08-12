def solution(arr):
    answer = []
    num=len(arr)
    while True:
        if (num&(num-1)==0):
            break
        else:
            arr.append(0)
            num=len(arr)
    
    return arr