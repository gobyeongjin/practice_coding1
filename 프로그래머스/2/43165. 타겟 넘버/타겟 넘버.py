def dfs(index, current_sum, numbers, target):
    if index == len(numbers):
        return 1 if current_sum == target else 0
    
    count = 0
    count += dfs(index + 1, current_sum + numbers[index], numbers, target)  
    count += dfs(index + 1, current_sum - numbers[index], numbers, target)  
    
    return count

def solution(numbers, target):
    return dfs(0, 0, numbers, target)

