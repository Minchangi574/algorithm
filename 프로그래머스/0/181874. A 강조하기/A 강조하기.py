def solution(myString):
    answer = []
    string=list(myString)
    for i in string:
        if i=="a":
            answer.append('A')
        elif i=="A":
            answer.append(i)
        else:
            answer.append(i.lower())
    answer_="".join(answer)
    return answer_