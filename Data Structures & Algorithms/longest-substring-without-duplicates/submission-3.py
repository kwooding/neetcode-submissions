class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = list()
        longest = list()
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for l in s:
            if l not in sub_str:
                sub_str.append(l)
            else:
                if len(longest) < len(sub_str):
                    longest = sub_str[:]
                index = sub_str.index(l)
                sub_str = sub_str[index + 1:]
                sub_str.append(l)
        if len(sub_str) > len(longest):
            longest = sub_str[:]
        return len(longest)