#### pascal triangle
#### leet code daily challenge 16/10/23
#### https://leetcode.com/problems/pascals-triangle-ii/description/?envType=daily-question&envId=2023-10-16

def get_row(n: int) -> list[int]:
    res = [1]
    if n > 0:
        prev = 1
        for k in range(1,n+1):
            next = (prev*(n-k+1))//k
            res.append(next)
            prev = next

    return res

def main():
    testcases = [5,3,0,1,2,6]
    expected = [[1,5,10,10,5,1],[1,3,3,1],[1],[1,1],[1,2,1],[1,6,15,20,15,6,1]]

    for i in range(len(testcases)):
        result = get_row(testcases[i])
        #print(result)
        if result == expected[i]:
            print("Test Case",i+1,"Passed")
        else:
            print("Test Case",i+1,"Failed")

if __name__=="__main__":
    main()