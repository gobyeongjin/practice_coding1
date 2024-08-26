def solution(sizes):
    answer = 0
    length = []
    tall = []
    
    for size in sizes:
        size.sort()
    
    for i in sizes:
        length.append(i[0])
        tall.append(i[1])
    
        
    
    
    return max(length) * max(tall)