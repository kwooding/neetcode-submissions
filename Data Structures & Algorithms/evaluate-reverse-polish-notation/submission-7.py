class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        ops = "+-*/"
        stack = []

        for t in tokens:
            print(t)
            if t not in ops:
                t = int(t)
                stack.append(t)
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    res = (a+b)
                    stack.append(res)
                elif t == "-":
                    res = (a-b)
                    stack.append(res)

                elif t == "*":
                    res = (a * b)
                    stack.append(res)

                elif t == "/":
                    res = int(a/b)
                    stack.append(res)

                

            print(stack)

        return stack[-1]