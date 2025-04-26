package google_prep

import (
	"slices"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	hashMap := make(map[string][]int)
	var result [][]string

	for i, str := range strs {
		strChars := strings.Split(str, "")
		slices.Sort(strChars)
		sortedStr := strings.Join(strChars, "")
		_, ok := hashMap[sortedStr]
		if !ok {
			hashMap[sortedStr] = []int{i}
		} else {
			hashMap[sortedStr] = append(hashMap[sortedStr], i)
		}
	}

	for _, v := range hashMap {
		var subVal []string
		for _, index := range v {
			subVal = append(subVal, strs[index])
		}
		result = append(result, subVal)
	}
	return result

}
