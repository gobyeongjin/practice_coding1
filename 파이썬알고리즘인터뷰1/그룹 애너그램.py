from collections import defaultdict

def anag(anagram):
    anagram_dict = defaultdict(list)
    
    for word in anagram:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)
    
    return list(anagram_dict.values())

anagram = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anag(anagram))


