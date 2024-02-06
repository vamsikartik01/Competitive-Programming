# https://leetcode.com/problems/successful-pairs-of-spells-and-potions

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []
        for spell in spells:
            l,r = 0,n-1
            total = 0
            while l <= r:
                m = (l+r) // 2
                if potions[m]*spell >= success:
                    total += r-m+1
                    r = m - 1
                else:
                    l = m + 1
            
            res.append(total)

        return res