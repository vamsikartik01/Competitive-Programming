func increasingTriplet(nums []int) bool {
	f := math.MaxInt64
	s := math.MaxInt64
	for _, num := range nums {
		if num <= f {
			f = num
		} else if num <= s {
			s = num
		} else {
			return true
		}
	}
	return false
}