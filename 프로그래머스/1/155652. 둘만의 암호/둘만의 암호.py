def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    s = list(s)
    alpha = [chr(i) for i in range(97,123) if chr(i) not in skip]
    
    for i in s:
        answer += alpha[((alpha.index(i))+index) % len(alpha)]
    return answer