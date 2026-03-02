import math
from collections import deque

def solution(progresses, speeds):
    days = []

    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)
    
    days = deque(days)
    
    answer = []
    point = days.popleft()
    count = 1
    
    while days:
        if days[0] <= point:
            days.popleft()
            count += 1
        else:
            answer.append(count)
            point = days.popleft()
            count = 1
    
    answer.append(count)  
    
    return answer