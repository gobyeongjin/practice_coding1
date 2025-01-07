def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    if numbers[0]*numbers[1] > numbers[-1]*numbers[-2]:
        return numbers[0]*numbers[1]
    else:
        return numbers[-1]*numbers[-2]
