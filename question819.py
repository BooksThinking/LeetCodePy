import collections
from typing import List

class Solution:
    def mostCommonWord(self ,paragraph: str, banned: List[str]) -> str:
        signs = ["!", "?", "'", ",", ";", "."]
        dict = collections.defaultdict(int)
        for sign in signs:
            paragraph = paragraph.replace(sign, " ")
        temp = paragraph.split(" ")

        for par in temp:
            if par.lower() not in banned:
                if par.lower() in dict.keys():
                    dict[par.lower()] = dict.get(par.lower()) + 1
                else:
                    dict[par.lower()] = 1
        max = 0
        MyTemp = ''
        for temp in dict.keys():
            if dict[temp] > max and temp != '':
                max = dict[temp]
                MyTemp = temp
        return MyTemp
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
s = Solution()
print(s.mostCommonWord(paragraph, banned))


