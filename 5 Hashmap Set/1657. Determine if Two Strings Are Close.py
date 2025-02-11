import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        
        count1=collections.Counter(word1)
        count2=collections.Counter(word2)

        if count1.keys() != count2.keys():
            return False
        
        return sorted(count1.values())==sorted(count2.values())
            






# from collections import Counter
# word = "aaabcde"
# c1=Counter(word)
# print(c1)


# # word = "aaabcde"
# # w1="abcde"
# # w2="aecdb"
# # z="qwertyuioplkjhgfdsazxcvbnm"

# # # Count the occurrences using a dictionary
# # cd1 = {char: w1.count(char) for char in sorted(set(z))}
# # # cd=count_dict
# # # print(count_dict)

# # # print(word.count('a'))

# # # print(cd)
# # cd2 = {char: w2.count(char) for char in sorted(set(z))}


# # # print(cd1)
# # # print(cd2)

# # # Get all values as lists
# # values_cd1 = list(cd1.values())
# # values_cd2 = list(cd2.values())

# # # print("Values from cd1:", values_cd1)
# # # print("Values from cd2:", values_cd2)

# # # s1=sum(values_cd1)
# # # s2=sum(values_cd2)

# # fl1 = [num for num in values_cd1 if num not in (0, 1)]


