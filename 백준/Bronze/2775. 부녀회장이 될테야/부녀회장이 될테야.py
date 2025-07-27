test_case = int(input())

for _ in range(test_case):
    floor = int(input())
    room = int(input())

    f0 = [i for i in range(1, room + 1)]

    for k in range(floor):
        for i in range(1, room):
            f0[i] += f0[i - 1]
        # print(' '.join(map(str, f0))) 
    print(f0[-1]) 
