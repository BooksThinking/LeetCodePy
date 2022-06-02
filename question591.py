# class Solution:
#     def isValid(self, code: str) -> bool:
#         stack = []
#         length = len(code)
#         for i in range(0, length):
#             if code[i] == '<':
#                 check, end_number = check_CDATA(code, i)
#                 if check:
#                     i = end_number
#                 else:
#
#
# def check_CDATA(code: str, begin: int):
#     if check_str_equal(code, begin, "<![CDATA["):
#         begin = begin + 9
#         while begin < len(code)-1:
#             if code[begin] == ']' and code[begin+1] == ']':
#                 return True, begin+1
#     return False, -1
#
#
# def check_str_equal(code: str, begin: int, input: str) -> bool:
#     for i,data in enumerate(input):
#         if data != code[begin + i]:
#             return False
#     return True
#

class Solution:
    def isValid(self, code: str) -> bool:
        tags = []
        i, n = 0, len(code)
        while i < n:
            if code[i] != "<":
                if not tags:
                    return False
                i += 1
                continue
            if i == n - 1:
                return False
            if code[i + 1] == "/":
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i + 2: j]
                if not tags or tags[-1] != tagname:
                    return False
                tags.pop()
                i = j + 1
                if not tags and i != n:
                    return False
            elif code[i + 1] == "!":
                if not tags:
                    return False
                cdata = code[i + 2: i + 9]
                if cdata != "[CDATA[":
                    return False
                j = code.find("]]>", i)
                if j == -1:
                    return False
                i = j + 1
            else:
                j = code.find(">", i)
                if j == -1:
                    return False
                tagname = code[i + 1: j]
                if not 1 <= len(tagname) <= 9 or not all(ch.isupper() for ch in tagname):
                    return False
                tags.append(tagname)
                i = j + 1

        return not tags