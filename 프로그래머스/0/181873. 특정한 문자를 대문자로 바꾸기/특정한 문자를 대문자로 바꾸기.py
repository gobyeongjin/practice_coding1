def solution(my_string, alp):
    
    my_string = list(my_string)
    answer = list(map(lambda x:x.upper() if x==alp else x, my_string))
    return "".join(answer)