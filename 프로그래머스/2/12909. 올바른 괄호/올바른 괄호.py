from collections import deque
def solution(s):
    answer = True
    
    ss = []
    
    s = deque(s)
    for i in s:
        if len(ss) == 0:
            ss.append(i)
        elif ss[-1] == '(' and i == ')':
            ss.pop()
        elif ss[-1] == '(' :
            ss.append(i)
        else:
            break
    
    if len(ss) != 0:
        return False
    else:
        return True
    
 