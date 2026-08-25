def solution(phone_number):
    a = phone_number[:-4]
    b = phone_number[-4:]
    answer = a.replace(a,"*"*len(a)) +b 
    
    return answer 