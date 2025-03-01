package lc75

// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

func KidsWithCandies(candies []int, extraCandies int) []bool {
	maxCandies := 0
	for _, candy := range candies {
		if maxCandies < candy {
			maxCandies = candy
		}
	}
	var res []bool

	for _, candy := range candies {
		if candy+extraCandies >= maxCandies {
			res = append(res, true)
		} else {
			res = append(res, false)
		}
	}
	return res
}
