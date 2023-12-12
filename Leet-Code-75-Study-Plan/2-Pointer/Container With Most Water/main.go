func maxArea(height []int) int {
	maxArea := 0
	n := len(height)
	l, r := 0, n-1

	for l < r {
		h := min(height[l], height[r])
		area := h * (r - l)
		maxArea = max(maxArea, area)
		if height[l] < height[r] {
			l += 1
		} else {
			r -= 1
		}
	}

	return maxArea
}