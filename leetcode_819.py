import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 전처리 진행
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^a-z]', ' ', paragraph)

        words = paragraph.split()
        counter = collections.defaultdict(int)
        for word in words:
            if word not in banned:
                counter[word] += 1

        max_keys = [key for key, value in counter.items() if max(counter.values()) == value]
        return max_keys[0]
