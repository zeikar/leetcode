class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = min(max(x1, xCenter), x2)
        y = min(max(y1, yCenter), y2)

        return (x - xCenter)**2 + (y - yCenter)**2 <= radius**2
