from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        begin_number = 0
        end_number = len(s)
        result = []
        for i in s:
            if i == 'I':
                result.append(begin_number)
                begin_number += 1
            else:
                result.append(end_number)
                end_number -= 1
        result.append(begin_number)
        return result
