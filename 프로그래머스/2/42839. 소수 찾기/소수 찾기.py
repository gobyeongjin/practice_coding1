from itertools import permutations

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    all_numbers = set()
    
    for i in range(1, len(num_list) + 1):
        for perm in permutations(num_list, i):
            num = int(''.join(perm))
            all_numbers.add(num)
    

    for number in all_numbers:
        if prime(number): 
            answer += 1
    
    return answer


def prime(numbers1):
    if numbers1 < 2:
        return False 
    
    for i in range(2, int(numbers1**0.5) + 1):
        if numbers1 % i == 0:
            return False
    
    return True

            
            
            