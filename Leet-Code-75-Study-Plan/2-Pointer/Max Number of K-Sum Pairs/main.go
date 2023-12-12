func maxOperations(nums []int, k int) int {
	sort.Ints(nums)
	n := len(nums)
	res, l, r := 0, 0, n-1

	for l < r {
		if nums[l]+nums[r] == k {
			res += 1
			l += 1
			r -= 1
		} else if nums[l]+nums[r] < k {
			l += 1
		} else {
			r -= 1
		}
	}
	return res
}