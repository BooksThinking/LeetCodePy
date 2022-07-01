class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return 0
        result = 0
        for i, data in num1:
            temp = 10 ** i
            result = result + temp * data * num2
        return  result