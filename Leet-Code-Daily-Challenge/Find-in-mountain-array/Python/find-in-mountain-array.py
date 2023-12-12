###   https://leetcode.com/problems/find-in-mountain-array/?source=submission-noac

## Approach 2 - Find the peak, search in the increasing and decreasing part separately.
class Solution1:
    def peak_finder(self, arr: list[int], n: int) -> int:
        l,r = 0,n-1
        while l < r :
            m = (l+r)//2
            if arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m
        return l

    def bin_search(self, arr: list[int], l: int, r: int, val: int, desc: bool = False) -> int:
        while l <= r:
            m = (l+r)//2
            mid_val = arr[m]
            if val == mid_val:
                return m
            elif val > mid_val:
                if desc:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if desc:
                    l = m + 1
                else:
                    r = m - 1

        return -1

    def findInMountainArray(self, target: int, mountain_arr: list[int]) -> int:
        n = len(mountain_arr)
        peak = self.peak_finder(mountain_arr, n)
        # print("peak",peak)
        if peak > 0:
            res = self.bin_search(mountain_arr,0,peak+1,target)
            if res != -1:
                return res
            else:
                res = self.bin_search(mountain_arr,n-peak-1,n-1,target, True)
                return res

        return -1     

### Approach1 using recursive search, time complexity satisfied but the condition is we shouldn't make to many fetches from the array. So this is not ideal. 
class Solution:
    def target_search(self, arr: list[int], l: int, r: int, val: int) -> int:
        if l > r:
            return []
        m = (l+r)//2
        # print("l,r,m",l,r,m)
        res = []
        if arr[m] == val:
            res.append(m)
        elif l==r:
            return res
        
        res += self.target_search(arr,l,m-1,val)
        res += self.target_search(arr,m+1,r,val)
        

        # print("res",res)
        return res

    def findInMountainArray(self, target: int, mountain_arr: list[int]) -> int:
        l,r = 0,len(mountain_arr)-1
        # print("target,l,r",target,l,r)
        res = self.target_search(mountain_arr, l, r, target)
        if len(res)>0:
            return min(res)
        else:
            return -1
   


def main():
    n = 3
    testcases = [[1,2,3,4,5,3,1],[0,1,2,4,2,1],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82]]
    testcasesTarget = [3,3,1]
    expected = [2,-1,0]

    solution = Solution1()
    for i in range(n):
        result = solution.findInMountainArray(testcasesTarget[i],testcases[i])
        print(result)
        if result == expected[i]:
            print("Test Case",i+1,"Passed")
        else:
            print("Test case",i+1,"Failed")


if __name__=="__main__":
    main()