data_list = []

while True:
    line = list(map(int, input().split()))
    
    
    if sum(line) == 0: 
        break
        
    line.sort()
    a, b, c = line[0], line[1], line[2]

    
    if c >= a + b:
        print("Invalid")
    else:
        
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")

    data_list.append(line)