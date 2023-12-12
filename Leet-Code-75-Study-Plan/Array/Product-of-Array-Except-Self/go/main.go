func productExceptSelf(nums []int) []int {
    product, prodZero := 1,1
    zeroes := false
    for _,num := range(nums) {
        product = product * num
        if (num != 0) || (zeroes) {
            prodZero = prodZero * num
        } 

        if (num==0) && !zeroes {
            zeroes = true
        }
    }

    res := []int{}
    for _.num := range(nums) {
        if num == 0{
            res = append(res, prodZero)
        } else {
            res = append(res, product/num)
        }
    }
    return res
}