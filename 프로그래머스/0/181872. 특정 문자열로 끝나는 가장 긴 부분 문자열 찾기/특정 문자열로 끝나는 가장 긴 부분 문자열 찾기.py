def solution(myString, pat):
    index=myString.rfind(pat) # rfind는 맨뒤에서부터 원하는 값 인덱스 찾음
    answer=myString[:index+len(pat)]
    return answer