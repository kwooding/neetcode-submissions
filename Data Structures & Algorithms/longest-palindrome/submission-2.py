class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        length = 0

        has_odd = False

        for c in count.values():
            length += c // 2 * 2
            if c % 2 == 1:
                has_odd = True

        return length + 1 if has_odd else length