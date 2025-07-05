def solution(my_string, overwrite_string, s):
    part_befor=my_string[:s]
    num=len(overwrite_string)
    after_num=s+num
    part_after=my_string[after_num:]
    answer=part_befor+overwrite_string+part_after
    return answer