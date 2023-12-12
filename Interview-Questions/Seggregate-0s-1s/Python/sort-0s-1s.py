###   Segregate 0s and 1s from an array 
###   https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s5106/0


def sortArr(arr):
    n = len(arr)
    m = 0
    swap = False

    for i in range(n):
        if arr[i] == 1 and not swap:
            m = i
            swap = True
        if arr[i] == 0  and swap:
            arr[m],arr[i] = arr[i], arr[m]
            m += 1

    return arr

def main():
    arrs = [[0,1,0,0,1,1,0,1,1,0,0,1,0],[1,0,1,1,1,0,0,0,0,0]]
    cnt = 0
    for arr in arrs:
        result = sortArr(arr)
        #print(result)
    
        expected = sorted(arr)
        cnt += 1
        if result == expected:
            print("Test Case",cnt,"- Passed")
        else:
            print("Test Case failed")

if __name__=="__main__":
    main()