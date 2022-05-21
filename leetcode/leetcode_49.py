import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        for str in strs:
            word = ''.join(sorted(str))
            dict[word].append(str)

        return dict.values()