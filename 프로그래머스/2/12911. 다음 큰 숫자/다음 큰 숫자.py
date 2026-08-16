def solution(n):
    answer = 0
    
    a = bin(n)
    a_count = a.count("1")
    k = n+1
    
    while k:
        if bin(k).count("1") == a_count:
            return k
        else:
            k+=1