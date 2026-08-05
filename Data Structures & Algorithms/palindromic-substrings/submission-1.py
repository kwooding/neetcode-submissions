class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for center in range(len(s)):
        # odd length
            l, r = center, center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        # even length
            l, r = center, center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res


    def isPalindrome(self,word):
        l,r = 0, len(word) -1
        while l < r:
            if word[l] != word[r]:
                return False

            l += 1
            r -= 1
        
        return True