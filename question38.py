class Solution:
    def countAndSay(self, n: int) -> str:
        temp_str = str(n)
        count = 0
        begin = temp_str[0]
        for count, data in enumerate(temp_str):
