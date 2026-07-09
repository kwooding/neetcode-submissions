class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        l,r = 0,window 
        
        while r < len(s2) + 1:
            check = []
            for c in sorted(s2[l:r]):
                if c not in s1:
                    pass
                else:
                    check.append(c)
            
            if check == sorted(s1):
                return True
            l += 1
            r+=1
           
        
        return False