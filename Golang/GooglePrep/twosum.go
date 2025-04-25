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

func twoSumOptimised(nums []int, target int) []int {
	hashMap := make(map[int]int)

	for i, num := range nums {
		comp := target - num
		li, ok := hashMap[comp]
		if ok {
			return []int{li, i}
		}
		hashMap[num] = i
	}
	return []int{}
}
