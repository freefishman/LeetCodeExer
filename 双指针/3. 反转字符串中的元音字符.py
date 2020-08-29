# 345. Reverse Vowels of a String (Easy)
class Solution:
    def reverseVowels(s: str) -> str:
        lists = [i for i in s]
        tools = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        i = 0
        j = len(lists)-1
        while i < j:
            if lists[i] not in tools:
                i += 1
            if lists[j] not in tools:
                j -= 1
            if lists[i] in tools and lists[j] in tools:
                lists[i], lists[j] = lists[j], lists[i]
                i += 1
                j -= 1
        return "".join(i for i in lists)
print(Solution.reverseVowels("hello"))