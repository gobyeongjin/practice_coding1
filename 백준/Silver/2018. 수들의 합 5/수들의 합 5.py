N = int(input())

st = 1
end = 1
current_add = 0
answer = 0

while st <= N:
    if current_add < N:
        current_add += end
        end += 1
    elif current_add > N:
        current_add -= st
        st += 1
    else:
        answer += 1
        current_add -= st
        st += 1

print(answer)
