class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
    
        res = ""
        mult = 0
        for c in s:
            if c.isdigit():
                mult = mult * 10 + int(c)
            elif c == "[":
                stack.append((res,mult))
                res = ""
                mult = 0
            elif c == "]":
                prev, num = stack.pop()
                res = prev + res * num
            else:
                res += c

        return res