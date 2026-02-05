from collections import Counter

N = input().upper()  
S = Counter(N)
word_count = S.most_common()

if len(word_count) > 1:

    if word_count[0][1] == word_count[1][1]:
        print('?')
    else:
        print(word_count[0][0])

else:
    print(word_count[0][0])
