class Solution:
    from collections import deque
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for i in operations:
            print(stack)
            if i == '+':
                val1 = stack[-1]
                val2 = stack[-2]
                stack.append(int(val1)+int(val2))
            elif i == 'D':
                operand = stack[-1]
                stack.append(int(operand) * 2)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(i)
        res = 0
        for n in range(len(stack)):
            res += int(stack.pop())
        return res