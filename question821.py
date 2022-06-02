class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans, last = [inf] * len(s), None
        for i, ch in enumerate(s):
            if ch == c:
                if last is not None:
                    for j in range(i, (i - 1 + last) // 2 - 1, -1):
                        ans[j] = min(ans[j], i - j)
                else:
                    for j in range(i, -1, -1):
                        ans[j] = min(ans[j], i - j)
                last = i
            elif last is not None:
                ans[i] = min(ans[i], i - last)
        return ans
