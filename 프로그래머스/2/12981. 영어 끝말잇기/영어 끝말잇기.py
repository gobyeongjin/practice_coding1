def solution(n, words):
    
    used = []
    
    for i, word in enumerate(words):
        
        if i == 0 :
            used.append(word)
            continue
        
        if word[0] != used[-1][-1] or len(word) <=1 or word in used:
            people = i % n + 1
            turn = i // n + 1
            
            return (people,turn)
        
        used.append(word)
    
    return [0,0]
    
        


    
        
