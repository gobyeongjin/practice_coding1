from itertools import permutations

def solution(numbers):
    answer = 0
    lst = []
    kk = len(numbers)
    
    for i in range(1, kk+1):
        number_permutations = set(int("".join(p)) for p in permutations(numbers, i))
        
        for num in number_permutations:
            if num not in lst and is_prime(num):
                lst.append(num)
                answer += 1
    
    return answer

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
