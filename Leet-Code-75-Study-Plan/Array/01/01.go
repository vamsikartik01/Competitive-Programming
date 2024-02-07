// https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
package main

import "strings"

func mergeAlternately(word1 string, word2 string) string {
	var res []string
	words1 := strings.Split(word1, "")
	words2 := strings.Split(word2, "")
	i := 0
	for (i < len(words1)) && (i < len(words2)) {
		res = append(res, words1[i]+words2[i])
		i += 1
	}
	res = append(res, words1[i:]...)
	res = append(res, words2[i:]...)

	return strings.Join(res, "")
}
