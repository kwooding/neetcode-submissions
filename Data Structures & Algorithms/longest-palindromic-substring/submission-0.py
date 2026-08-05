class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for l in range(len(s)):
            for r in range(l, len(s)):
                check = s[l:r+1]
                if len(check) > len(res) and self.isPalindrome(check):
                    res = check
        return res

        
    def isPalindrome(self,word):
        l,r = 0, len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        
        return True