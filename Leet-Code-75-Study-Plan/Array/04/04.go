package main

func canPlaceFlowers(flowerbed []int, n int) bool {
	var res int = 0
	k := len(flowerbed)
	if k == 1 {
		if flowerbed[0] == 0 {
			res += 1
			flowerbed[0] = 1
		}
	} else {
		for i := 0; i < k; i++ {
			if i == 0 {
				if (flowerbed[i] == 0) && (flowerbed[i+1] == 0) {
					res += 1
					flowerbed[i] = 1
				}
			} else if i == k-1 {
				if (flowerbed[i] == 0) && (flowerbed[i-1] == 0) {
					res += 1
					flowerbed[i] = 1
				}
			} else {
				if (flowerbed[i] == 0) && (flowerbed[i-1] == 0) && (flowerbed[i+1] == 0) {
					res += 1
					flowerbed[i] = 1
				}
			}
		}
	}
	if n <= res {
		return true
	} else {
		return false
	}
}
