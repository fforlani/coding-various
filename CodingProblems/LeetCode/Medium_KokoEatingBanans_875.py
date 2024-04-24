class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        start = 1
        end = k = max(piles)
        while start < end:
            half = start + (end - start) // 2
            if self.isKvalid(piles.copy(), h, half):
                k = min(k, half)
                end = half
            else:
                start = half + 1
        return k

    def isKvalid(self, piles: List[int], h: int, k: int) -> int:
        index = 0
        while h > 0 and index < len(piles):
            h -= math.ceil(piles[index] / k)
            index += 1
        return index == len(piles) and h >= 0