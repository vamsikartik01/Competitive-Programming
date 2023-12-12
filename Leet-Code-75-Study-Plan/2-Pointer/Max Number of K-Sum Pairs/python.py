class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        l,r = 0,len(nums)-1

        while l<r:
            val = nums[l]+nums[r]
            if val == k:
                res += 1
                l += 1
                r -= 1
            elif val < k:
                l += 1
            else:
                r -= 1

        return res