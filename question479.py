import math


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        const = 1
        while const < 10 ** n:
            upper = 10 ** n - const
            lower = int(str(upper)[::-1])
            if const ** 2 - lower * 4 >= 0 and (const ** 2 - lower * 4) ** 0.5 == int((const ** 2 - lower * 4) ** 0.5):
                return (upper * 10 ** n + lower) % 1337
            const += 1
s = Solution()
print(Solution.largestPalindrome(n=4))
