def solution(n, lost, reserve):

    lst = [1] * n  
    
    for i in lost:
        lst[i - 1] -= 1
    for i in reserve:
        lst[i - 1] += 1
        
    for i in range(n):
        if lst[i] == 0:
            if i > 0 and lst[i - 1] == 2: 
                lst[i] = 1
                lst[i - 1] = 1
            elif i < n - 1 and lst[i + 1] == 2: 
                lst[i] = 1
                lst[i + 1] = 1
    
    answer = sum(1 for x in lst if x > 0)
    
    return answer
