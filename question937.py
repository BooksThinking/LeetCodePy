from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=lambda log: (0, log.split(' ')[1:], log.split(' ')[0]) if log[-1].isalpha() else (1,))