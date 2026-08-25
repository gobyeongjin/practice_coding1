def solution(arr, k):
    answer = []
    arr  = list(map(lambda x: x*k if k%2 == 1 else x+k, arr))
    return arr