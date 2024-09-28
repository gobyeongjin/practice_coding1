from collections import deque

def solution(number, k):
    answer = deque()
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    
    return ''.join(list(answer)[:len(number) - k])
