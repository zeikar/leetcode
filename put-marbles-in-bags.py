class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_weights = []
        for i in range(1, len(weights)):
            pair_weights.append(weights[i - 1] + weights[i])

        pair_weights.sort()

        minans = 0
        for i in range(k - 1):
            minans += pair_weights[i]
        minans += weights[0] + weights[-1]

        maxans = 0
        for i in range(k - 1):
            maxans += pair_weights[len(pair_weights) - i - 1]
        maxans += weights[0] + weights[-1]

        return maxans - minans
