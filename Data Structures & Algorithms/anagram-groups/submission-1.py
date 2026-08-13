class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))  # canonical form shared by all anagrams
            groups[key].append(word)

        return list(groups.values())