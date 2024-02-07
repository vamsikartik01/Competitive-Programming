// https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

package main

import "strings"

func ifExists(s []string, a string) bool {
	for _, char := range s {
		if char == a {
			return true
		}
	}
	return false
}

func reverseVowels(s string) string {
	vowels := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
	var v []string
	chars := strings.Split(s, "")
	vc := 0
	for _, char := range chars {
		if ifExists(vowels, char) {
			vc += 1
			v = append(v, char)
		}
	}

	for i, char := range chars {
		if ifExists(vowels, char) {
			chars[i] = v[vc-1]
			vc -= 1
		}
	}

	return strings.Join(chars, "")
}
