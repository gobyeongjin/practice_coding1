def solution(array, commands):
    answer = []
    for i in commands:
        st = i[0]
        finish = i[1]
        
        array1 = array[st-1:finish]
        array1 = sorted(array1)
        answer.append(array1[i[2]-1])

            
    return answer