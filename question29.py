class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if dividend == -2147483648 and divisor == -1:
            return 0x7fffffff;
        a, b = abs(dividend), abs(divisor)
        if a < b:
            return 0
        c = b
        while (c << 1) <= a:
            c <<= 1
        ans = 0
        while c >= b:
            ans <<= 1
            if a >= c:
                ans |= 1
                a -= c
            c >>= 1
        if (dividend > 0) ^ (divisor > 0):
            ans = -ans
        return ans