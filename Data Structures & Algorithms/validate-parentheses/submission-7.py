class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False
        for c in s[:]:
            print(c)
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            if stack:
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
            else:
                return False
        if stack:
            return False
        return True
