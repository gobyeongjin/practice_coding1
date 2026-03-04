from collections import deque

def solution(priorities, location):
    
    q = deque([(p, i) for i, p in enumerate(priorities)])
    priorities.sort(reverse = True)
    
    answer = 0
    idx = 0
    
    while q:    
        
        p , i = q.popleft()
        
        if p == priorities[idx]:
            answer += 1
            idx += 1
            
            if i == location :
                return answer 
        
        else:
            q.append((p , i))
    

  