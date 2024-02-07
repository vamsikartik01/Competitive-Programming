package main

import "strings"

func gcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func gcdOfStrings(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}

	l1, l2 := len(str1), len(str2)
	chars := strings.Split(str1, "")
	return strings.Join(chars[:gcd(l1, l2)], "")
}
