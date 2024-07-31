class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def putBook(bookIdx):
            if bookIdx == n:
                return 0

            width = 0
            maxHeight = 0
            ret = 987654321
            for i in range(bookIdx, n):
                [t, h] = books[i]
                width += t

                if width > shelfWidth:
                    break

                maxHeight = max(maxHeight, h)
                ret = min(ret, putBook(i + 1) + maxHeight)

            return ret

        return putBook(0)
