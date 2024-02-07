# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1168980774/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        res = []
        for candy in candies:
            if candy+extraCandies >= maxCandies:
                res.append(True)
            else:
                res.append(False)

        return res