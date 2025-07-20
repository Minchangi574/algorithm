def solution(my_string, queries):
    my_list=list(my_string)
    for s,e in queries:
        print("시작")
        if (e-s)%2!=0:
            num=((e-s)/2)+0.5
        else:
            num=(e-s)/2
        for i in range(int(num)):
            a=my_list[s+i]
            b=my_list[e-i]
            my_list[e-i]=a
            my_list[s+i]=b
    my_list_answer="".join(my_list)
    return my_list_answer