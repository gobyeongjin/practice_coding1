from collections import Counter
def solution(participant, completion):
    answer = ''
    
    participant = Counter(participant)
    completion = Counter(completion)
    
    answer = participant - completion
    
    name = list(answer.keys())[0]
    
    return name