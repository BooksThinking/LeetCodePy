class Solution:
    def countAndSay(self, n: int) -> str:
        begin = 0
        temp = 1
        while begin < n-1:
            temp = read_number(temp)
            begin += 1
        return str(temp)

def read_number(n: int):
    temp_str = str(n)
    count = 0
    begin = temp_str[0]
    result = ""
    for data in temp_str:
        if data == begin:
            count += 1
        else:
            result = result + str(count) + str(begin)
            count = 1
            begin = data
    result = result + str(count) + str(begin)
    return result

s = Solution()
print(s.countAndSay(4))