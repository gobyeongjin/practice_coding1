from collections import Counter
def solution(participant, completion):
    answer = ''
    
    p = Counter(participant)
    c = Counter(completion)
    
    answer = p-c
    answer= list(set(answer))
    
    return answer[0]