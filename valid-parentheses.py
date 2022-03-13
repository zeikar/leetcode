class Solution:
    def isValid(self, s: str) -> bool:
        close = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in close:
                if not stack or stack.pop() != close[char]:
                    return False
            else:
                stack.append(char)
        return not stack
