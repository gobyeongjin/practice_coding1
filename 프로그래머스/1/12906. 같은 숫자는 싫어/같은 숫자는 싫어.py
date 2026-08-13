def solution(arr):
    
    last = arr[0]
    answer = [arr[0]]
    
    for i in range(1,len(arr)):
        if last == arr[i]:
            continue
        else:
            last = arr[i]
            answer.append(arr[i])
    
    return answer