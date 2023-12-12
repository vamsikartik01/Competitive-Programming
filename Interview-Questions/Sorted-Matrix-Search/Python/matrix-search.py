####  Sorted Matrix Search - Interview Question
###   Given a sorted matrix of mxn find the index of the given element.

def binarySearch(arr, val):
    n = len(arr)
    l,r = 0,n-1
    while l <= r :
        m = l + (r-l)//2
        # print("l,r,m",l,r,m)
        if arr[m] == val:
            return m
        elif val < arr[m]:
            r = m-1
        else:
            l = m+1
    return -1

def searchMatrix(matrix, val):
    n = len(matrix)
    t,b = 0,n-1
    while t <= b:
        m = t + (b-t)//2
        # print("t,b,m",t,b,m)
        if val >= matrix[m][0] and val <= matrix[m][-1]:
            resn = binarySearch(matrix[m],val)
            if resn == -1:
                break
            return m,resn
        elif val < matrix[m][0]:
            b = m-1
        else:
            t = m+1
    return -1,-1

def main():
    matrix = [
        [12, 14, 16, 18, 20, 23],
        [25, 27, 28, 31, 32, 33],
        [35, 37, 38, 40, 42, 43],
        [54, 55, 56, 59, 60, 65]
    ]
    vals = [14, 34, 42, 65, 55]
    expected = [(0,1),(-1,-1),(2,4),(3,5),(3,1)]

    for i in range(len(vals)):
        result = searchMatrix(matrix,vals[i])
        #print(result)
        if result == expected[i] :
            print("Test Case",i+1,"Passed")
        else:
            print("Test Case",i+1,"Failed")
    

if __name__=="__main__":
    main()