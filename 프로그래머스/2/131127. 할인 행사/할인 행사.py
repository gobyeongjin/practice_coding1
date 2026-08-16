from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    lst = []
    want_counter = dict(zip(want,number))
    
    for i in range(len(discount)-9):
        if want_counter == Counter(discount[i:i+10]):
            answer+=1
        else:
            continue
    
    return answer