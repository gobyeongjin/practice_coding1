def solution(sequence, k):
    
    st = 0
    end = 0
    
    current_sum = 0
    result = [] 
    
    len_sequence = len(sequence)
    
    while True:
        if current_sum >= k :
            if current_sum == k:
                result.append((st,end-1))
            
            current_sum -= sequence[st]
            st += 1
                

        
        else:
            if end == len_sequence:
                break
            
            current_sum += sequence[end]
            end += 1
            
    answer = min(result, key=lambda x: (x[1] - x[0], x[0]))
            
    return answer
        
        