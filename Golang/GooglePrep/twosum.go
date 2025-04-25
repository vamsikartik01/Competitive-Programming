package google_prep

func twoSum(nums []int, target int) []int {
	n := len(nums)
	for i := range n {
		val := nums[i]
		for j := i + 1; j < n; j++ {
			if val+nums[j] == target {
				return []int{i, j}
			}
		}
	}

	return []int{}

}
