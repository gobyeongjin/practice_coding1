def solution(arr):
    answer = []
    lst_num = -1
    
    for i in arr:
        if i!= lst_num:
            answer.append(i)
            lst_num = i
    
    return answer