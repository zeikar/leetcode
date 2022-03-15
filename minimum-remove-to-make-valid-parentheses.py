class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = ""
        cnt = 0

        for ch in s:
            if ch == '(':
                cnt += 1
                temp += ch
            elif ch == ')':
                if cnt != 0:
                    temp += ch
                    cnt -= 1
            else:
                temp += ch

        ans = ""
        for ch in temp[::-1]:
            if ch == '(' and cnt > 0:
                cnt -= 1
            else:
                ans += ch

        return ans[::-1]
