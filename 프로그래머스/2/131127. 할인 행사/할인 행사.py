from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_zip = dict(zip(want,number))
    
    for i in range(0,len(discount)-9):
        if Counter(discount[i:i+10]) == want_zip:
            answer+=1
        
        
    return answer