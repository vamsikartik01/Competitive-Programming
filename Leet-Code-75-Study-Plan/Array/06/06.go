// https://leetcode.com/problems/reverse-words-in-a-string/

package main

import "strings"

func reverse(chars []string) []string {
	n := len(chars)
	i := 0
	for i < n/2 {
		chars[i], chars[n-i-1] = chars[n-i-1], chars[i]
		i += 1
	}
	return chars
}

func reverseWords(s string) string {
	trimmed := strings.TrimSpace(s)
	words := strings.Fields(trimmed)
	revWords := reverse(words)
	return strings.Join(revWords, " ")
}
