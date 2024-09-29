
from collections import deque

def palindrom(words):
    pal = deque()
    
    # 입력 받은 문자열에서 알파벳만 소문자로 변환하여 덱에 추가
    for word in words:
        if word.isalpha():
            pal.append(word.lower())
    
    # 덱의 앞뒤에서 비교
    while len(pal) > 1:
        if pal.popleft() != pal.pop():
            print("false")
            return
    
    print("true")

# 사용자 입력
words = input("문자열을 입력하세요: ")
palindrom(words)


