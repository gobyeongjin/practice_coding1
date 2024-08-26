def solution(answers):
    answer = [0, 0, 0]
    students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    for i, student in enumerate(students):
        for j in range(len(answers)):
            if student[j % len(student)] == answers[j]:
                answer[i] += 1
    
    max_score = max(answer)
    result = [i + 1 for i, score in enumerate(answer) if score == max_score]
    
    return result
