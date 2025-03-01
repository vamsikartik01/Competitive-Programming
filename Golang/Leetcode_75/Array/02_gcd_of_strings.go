package lc75

// https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

import "strings"

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func GcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}

	l1 := len(strings.Split(str1, ""))
	l2 := len(strings.Split(str2, ""))
	gcdVal := gcd(l1, l2)

	return strings.Join(strings.Split(str1, "")[:gcdVal], "")
}
