class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = "".join(char for char in s if char.isalnum()).lower()
        n = len(c)
        l,r = 0, n - 1
        while l<r:
            if c[l] != c[r]:
                return False
            l +=1
            r-=1

        return True
