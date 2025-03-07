// https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
package main

import "strings"

func mergeAlternately(word1 string, word2 string) string {
	words1 := strings.Split(word1, "")
	words2 := strings.Split(word2, "")
	i := 0
	op := []string{}
	for i < len(words1) && i < len(words2) {
		op = append(op, words1[i])
		op = append(op, words2[i])
		i += 1
	}
	op = append(op, words1[i:]...)
	op = append(op, words2[i:]...)
	return strings.Join(op, "")
}
