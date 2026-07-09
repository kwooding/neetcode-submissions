class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalpha() or c.isnumeric()).lower()
        print(s)
        length = len(s)
        l = 0
        r = length - 1
    
        while l <= r:
            if l == r:
                return True
            else:
                if s[l] == s[r]:
                    l +=1
                    r -=1
                else:
                    return False
        
        return True
            
            