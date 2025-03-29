def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def solution(numer1, denom1, numer2, denom2):
    denom3=denom1*denom2 #통분한 분모 값
    numer3=numer1*denom2+numer2*denom1
    
    gcd_value=gcd(numer3,denom3)
    simpil_numer3=numer3/gcd_value
    simpil_denom3=denom3/gcd_value
        
    answer = [simpil_numer3,simpil_denom3]
    return answer
