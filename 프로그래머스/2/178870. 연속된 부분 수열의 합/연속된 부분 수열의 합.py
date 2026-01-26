def solution(sequence, k):
    
    answer = []
    
    n = len(sequence)
    
    st = 0
    end = 0
    current_sum = sequence[0]
    
    while st < n and end < n:
        if current_sum == k:
            answer.append([st,end])
            current_sum -= sequence[st]
            st += 1
        
        elif current_sum < k:
            end += 1
            if end < n:
                current_sum += sequence[end]
            
        
        else:
            current_sum -= sequence[st]
            st+=1
            
    
    answer = min(answer, key=lambda x: x[1]-x[0])
    
    return answer