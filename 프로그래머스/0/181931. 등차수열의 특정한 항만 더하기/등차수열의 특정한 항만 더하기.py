def solution(a, d, included):
    total=0
    included_len=len(included)
    for i in range(included_len):
        num=a+(i*d)
        if included[i]==True:
            total+=num
        
        
        
    return total
