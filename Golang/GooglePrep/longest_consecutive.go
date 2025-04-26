package google_prep

func longestConsecutive(nums []int) int {
	HashMap := make(map[int]int)
	maxLength := 0
	for i, num := range nums {
		HashMap[num] = i
	}

	for _, num := range HashMap {
		currentLength := 1
		temp := num

		if _, ok := HashMap[num-1]; !ok {
			for {
				temp = temp + 1

				_, ok = HashMap[temp]
				if !ok {
					break
				}
				currentLength += 1
			}
		}

		if currentLength > maxLength {
			maxLength = currentLength
		}
	}

	return maxLength
}
