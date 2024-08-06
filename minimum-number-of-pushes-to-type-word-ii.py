class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        ans = 0
        alphabet = 0
        for a, c in cnt.most_common():
            ans += (alphabet // 8 + 1) * c
            alphabet += 1
        return ans
