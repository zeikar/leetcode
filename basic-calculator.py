class Solution:
    def calculate(self, s: str) -> int:
        num_stack = [0]
        op_stack = [1]
        num = 0
        s = '(' + s + ')'

        for i in range(len(s)):

            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '+':
                op = op_stack.pop()
                num_stack[-1] += num * op
                op_stack.append(1)
                num = 0
            elif s[i] == '-':
                op = op_stack.pop()
                num_stack[-1] += num * op
                op_stack.append(-1)
                num = 0
            elif s[i] == '(':
                num_stack.append(0)
                op_stack.append(1)
            elif s[i] == ')':
                op = op_stack.pop()
                num_stack[-1] += num * op
                op = op_stack.pop()
                n = num_stack.pop()
                num_stack[-1] += n * op
                op_stack.append(1)
                num = 0

        return num_stack[0]
