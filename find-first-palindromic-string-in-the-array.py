class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def check(word):
            for i in range(len(word) // 2):
                if word[i] != word[len(word)-i-1]:
                    return False
            return True

        for word in words:
            if check(word):
                return word

        return ""
