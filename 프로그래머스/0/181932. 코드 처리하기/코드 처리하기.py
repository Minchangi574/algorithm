def solution(code):
    mod=0
    ret=[]
    code_len=len(code)
    for i in range(code_len):
        if code[i]!='1':
            if mod==0:
                if i%2==0:
                    num=code[i]
                    ret.append(num)
            else:
                if i%2!=0:
                    num=code[i]
                    ret.append(num)       
        else:
            if mod==0:
                mod=1
            else:
                mod=0
    result_ret="".join(ret)
    if not result_ret: # result_ret이 빈 문자열인 경우
        return "EMPTY"
    else:
        return result_ret
#    return result_ret