def solution(my_string, target):
    answer = 0
    string=[]
    for i in range(len(my_string)):
        for k in range(i+1,len(my_string)+1): # 그냥 i이면 빈 문자열 추가
            string.append(my_string[i:k])
    if target in string:
        answer=1
    else:
        answer=0
            
    return answer