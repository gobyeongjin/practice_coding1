N = int(input())
count = 0 

def find(word):
    lst = []
    is_group_word = True

    for i in range(len(word)):
        if i == 0:
            lst.append(word[i])
            continue

        if word[i] != word[i-1]:
            if word[i] in lst:
                is_group_word = False
                break
            lst.append(word[i])

    if is_group_word:
        return 1
    else:
        return 0

for _ in range(N):
    word = input()
    if find(word) == 1:
        count += 1

print(count)
