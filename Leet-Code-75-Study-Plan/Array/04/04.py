# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        k = len(flowerbed)
        if k == 1:
            if flowerbed[0] == 0:
                res += 1
        else:        
            for i in range(k):
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        res += 1
                        flowerbed[i] = 1

                elif i == k-1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        res += 1
                        flowerbed[i] = 1

                else:
                    if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        res += 1
                        flowerbed[i] = 1

        if n <= res:
            return True
        else:
            return False
             
            