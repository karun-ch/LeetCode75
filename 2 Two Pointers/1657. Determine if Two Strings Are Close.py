# # s = "hello"
# # print()
# # e=enumerate(s)

# # print(list(e))

# from collections import Counter

# # Example
# s1 = "listen"
# s2 = "silent"
# print(Counter(s1))
# print(Counter(s2)) 


from collections import defaultdict

# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)

# print(anagrams)

# print(''.join(sorted("bgtya")))

for word in words:
    sorted_word = ''.join(sorted(word))
    print("ifr",word, "  ", sorted_word)
    anagrams[sorted_word].append(word)
    print(list(anagrams))

print(list(anagrams.items()))