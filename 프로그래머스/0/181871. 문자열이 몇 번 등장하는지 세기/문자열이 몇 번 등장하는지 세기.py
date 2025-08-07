def solution(myString, pat):
    answer = 0
    index=0
    while True:
        num=myString.find(pat,index) # 처음에 index=0임
        if num==-1:
            break
        else:
            answer+=1
            index=num+1
                # pat이 끝나는 지점부터 다시 확인하기 위함 
    return answer