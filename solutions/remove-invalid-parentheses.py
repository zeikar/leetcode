from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(st):
            stack = []

            for c in st:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if not stack:
                        return False
                    stack.pop()

            return not stack

        level = {s}

        while True:
            res = []
            for st in level:
                if is_valid(st):
                    res.append(st)

            if res:
                return res

            new_level = set()
            for st in level:
                for i in range(len(st)):
                    if st[i] in '()':
                        new_st = st[:i] + st[i + 1:]
                        new_level.add(new_st)

            level = new_level
