result = []

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        find(candidates, target)

def find(candidates: List[int], target: int) -> int:
    for data in candidates:
        count = target
        while count > 0:
            temp = candidates.remove(data)
             return find(temp, count)


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    ans = []

    def find(s, use, remain):
        for i in range(s, len(candidates)):
            c = candidates[i]
            if c == remain:
                ans.append(use + [c])
                return
            if c < remain:
                find(i, use + [c], remain - c)
            if c > remain:
                return

    find(0, [], target)
    return ans
