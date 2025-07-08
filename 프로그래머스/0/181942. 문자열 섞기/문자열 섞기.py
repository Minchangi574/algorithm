def solution(str1, str2):
    total=[]
    for i,n in zip(str1,str2):
        total.append(i)
        total.append(n)
    total_list="".join(total)
    
    answer = ''
    return total_list