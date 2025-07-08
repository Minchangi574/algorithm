def solution(a, b):
    a_num=str(a)+str(b)
    b_num=2*a*b
    if int(a_num)>int(b_num):
        answer=int(a_num)
    elif int(b_num)>int(a_num):
        answer=b_num
    else:
        answer=int(a_num)
    return answer