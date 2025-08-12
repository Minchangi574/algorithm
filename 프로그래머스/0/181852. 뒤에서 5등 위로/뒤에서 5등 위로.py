def solution(num_list):
    answer = []
    num_list.sort()
    num=num_list
    for i in range(len(num)):
        if i>4:
            answer.append(num[i])
    return answer