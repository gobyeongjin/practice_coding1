def solution(people, limit):
    answer = 0
    people.sort()
    
    st = 0
    end = len(people) - 1
    
    while st <= end:
        if people[st] + people[end] <= limit:
            st += 1   # 가벼운 사람도 태움
        end -= 1       # 무거운 사람은 항상 태움
        answer += 1    # 보트 1대 사용
    
    return answer
