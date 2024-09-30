from collections import Counter
import re

def common(paragraph):
    paragraph = re.sub(r'[^\w\s]', '', paragraph.lower())
    words = paragraph.split(" ")
    
    answer = Counter(words)
    
    answer = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    
    return answer[0][0]

paragraph = "BOb hit a ball, the hit BALL flew far after it was hit."
print(common(paragraph))
