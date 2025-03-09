package lc75

// https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

func CanPlaceFlowers(flowerbed []int, n int) bool {
	len := len(flowerbed)
	for i, val := range flowerbed {
		if val == 0 {
			if i == 0 {
				if len > 1 {
					if flowerbed[i+1] == 0 {
						n -= 1
						flowerbed[i] = 1
					}
				} else {
					n -= 1
					flowerbed[i] = 1
				}
			} else if i == len-1 {
				if flowerbed[i-1] == 0 {
					n -= 1
					flowerbed[i] = 1
				}
			} else {
				if flowerbed[i-1] == 0 && flowerbed[i+1] == 0 {
					n -= 1
					flowerbed[i] = 1
				}
			}
		}
	}
	if n <= 0 {
		return true
	}
	return false
}
