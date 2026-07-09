class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= list(s)
        t= list(t)
        if len(s) != len(t):
            return False
        else:
            for letter in s:
                print(letter)
                if letter in t:
                    t.remove(letter)
                else:
                    return False
            return True
