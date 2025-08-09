import re
def solution(myStr):
    answer=re.split('a|b|c',myStr)
    answer_=[s for s in answer if s!=""]
    if answer_==[]:
        answer_.append("EMPTY")
    return answer_