class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pd = 1
        pd0 = 1
        zeroes = False
        for num in nums:
            pd *= num
            if num != 0 or zeroes:
                pd0 = pd0*num

            if num==0 and not zeroes:
                zeroes = True

        res = []
        for num in nums:
            if num == 0:
                res.append(pd0)
            else:
                res.append(int(pd/num))

        return res