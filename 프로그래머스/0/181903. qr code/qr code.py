def solution(q, r, code):
    num=[]
    for i in range(len(code)):
        if i%q==r:
            num.append(code[i])
    answer="".join(num)
    return answer