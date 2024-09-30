from collections import deque

def palindrom(palin):
    pal = deque(palin)
    while len(pal) > 1:
        if pal.popleft() != pal.pop():
            return False
    return True

def find(words):
    answer = []
    for i in range(len(words)):
        for k in range(i + 1, len(words) + 1):
            palin = words[i:k]
            if palindrom(palin):
                answer.append(palin)
    return answer

def longest(answer):
    long_len = 0
    long_answer = answer[0]
    
    for i in range(len(answer)):
        if len(answer[i]) > long_len:
            long_len = len(answer[i])
            long_answer = answer[i]
    
    return long_answer

words = "babad"
answer = find(words)  
print(longest(answer))
