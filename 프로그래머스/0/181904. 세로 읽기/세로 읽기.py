def solution(my_string, m, c):
    a=[] # 각 행 추가하는 리스트
    answer=[] # 전체 완성 문자 리스트
    total=[] # 각 행이 모두 모인 리스트
    num=1 # 몇 행인지
    for i in range(len(my_string)):
        if i%m==0:
            a.append(my_string[i])
        else:
            a.append(my_string[i])
            if len(a)==m:
                total.append(a)
                a=[]
                num+=1
    for i in total:
        answer.append(i[c-1])
    if answer==[]: # m 1이면 그냥 전부 출력
        answer_=my_string
    else:
        answer_="".join(answer)
    return answer_