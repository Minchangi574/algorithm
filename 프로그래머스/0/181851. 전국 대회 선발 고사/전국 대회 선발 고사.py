def solution(rank, attendance):
    answer = 0
    attend=[]
    for i in range(len(rank)):
        if attendance[i]==True:
            attend.append((rank[i],i)) # [등수, 학생번호]
    attend.sort() # 오름차순 정렬
    a=attend[0][1] # 튜플 0번째에 1등에 학생번호 인덱스 1로 받음
    b=attend[1][1]
    c=attend[2][1]
    answer=(10000*a)+(100*b)+c
    #print('a',a,'b',b,'c',c)
    #print(attend)
    return answer