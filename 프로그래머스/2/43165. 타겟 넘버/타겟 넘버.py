# from itertools import product
# def solution(numbers, target):

#     a=[(-i,i) for i in numbers]
    
#     answer=list(map(sum,product(*a)))

#     return answer.count(target)

def solution(numbers, target):
    
    results = [[]]
    
    for i in numbers:
        results = [x + [y] for x in results for y in (-i, i)]
    
    answer = [x for x in results if sum(x) == target]
    
    return len(answer)