def solution(array, commands):
    answer = []
    for command in commands:
        start,end,num = command[0],command[1],command[2]
        
        lst = array[start-1:end]
        lst = sorted(lst)
        answer.append(lst[num-1])
        
        
    
    return answer