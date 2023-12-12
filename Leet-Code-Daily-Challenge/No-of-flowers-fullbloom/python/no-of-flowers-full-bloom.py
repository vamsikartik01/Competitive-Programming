#####  Number of flowers in full bloom
#####  https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/



class Solution:
    def binSearch(self, arr: list[int], val: int) -> int:
        l,r = 0,len(arr)-1
        while l<=r:
            m = (l+r)//2
            if val >= arr[m]:
                l = m+1
            else:
                r = m-1
        return r+1

    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        
        bloomed = []
        bloomedOut = []
        for flower in flowers:
            bloomed.append(flower[0])
            bloomedOut.append(flower[1])

        bloomed.sort()
        bloomedOut.sort()

        res = []
        for person in people:
            tbf = self.binSearch(bloomed, person)
            tbof = self.binSearch(bloomedOut, person-1)
            res.append(tbf-tbof)

        return res
        
    # Traditional Search - Got Time limit exceded
    def search(self, array: list[int], val: int) -> int:
        cnt = 0
        for i in array:
            if i <= val:
                cnt += 1
        return cnt

    ############  Memory limit exceded
    def fullBloomFlowersMemoryLimitExceded(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        data = dict()
        for flower in flowers:
            for i in range(flower[0], flower[-1]+1):
                if i in data:
                    data[i] += 1
                else:
                    data[i] = 1
        
        result = []
        for person in people:
            if person in data:
                result.append(data[person])
            else:
                result.append(0)

        return result 
        

    ######## Traditional Approach - Time limit exceded
    def fullBloomFlowersTimeLimitExceded(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        result = []
        for person in people:
            cnt = 0
            for flower in flowers:
                if person >= flower[0] and person <= flower[-1]:
                    cnt += 1
                
            result.append(cnt) 
        return result

def main():
    n = 2
    testcases = [[[1,10],[3,3]],[[1,6],[3,7],[9,12],[4,13]]]
    testcasesPeople = [[3,3,2],[2,3,7,11]]
    expected = [[2,2,1],[1,2,2,2]]

    solution = Solution()
    for i in range(n):
        result = solution.fullBloomFlowers(testcases[i],testcasesPeople[i])
        #print(result)
        if result == expected[i]:
            print("Test Case",i+1,"Passed")
        else:
            print("Test case",i+1,"Failed")

if __name__=="__main__":
    main()