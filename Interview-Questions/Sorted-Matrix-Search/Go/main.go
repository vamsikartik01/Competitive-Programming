// Sorted Matrix Search - Interview Question
// Given a sorted matrix of mxn find the index of the given element.

package main

import (
	"fmt"
	"reflect"
)

func binarySearch(arr []int, val int) int {
	var n = len(arr)
	var l, r = 0, n - 1
	for l <= r {
		m := l + (r-l)/2
		if val == arr[m] {
			return m
		} else if val < arr[m] {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return -1
}

func matrixSearch(matrix [][]int, val int) []int {
	var n = len(matrix)
	var p = len(matrix[0])
	var t, b = 0, n - 1
	for t <= b {
		m := t + (b-t)/2
		if val >= matrix[m][0] && val <= matrix[m][p-1] {
			resm := binarySearch(matrix[m], val)
			if resm == -1 {
				return []int{-1, -1}
			}
			return []int{m, resm}
		} else if val < matrix[m][0] {
			b = m - 1
		} else {
			t = m + 1
		}
	}

	return []int{-1, -1}
}

func main() {

	matrix := [][]int{
		{12, 14, 16, 18, 20, 23},
		{25, 27, 28, 31, 32, 33},
		{35, 37, 38, 40, 42, 43},
		{54, 55, 56, 59, 60, 65},
	}

	vals := []int{14, 34, 42, 65, 55}
	expected := [][]int{{0, 1}, {-1, -1}, {2, 4}, {3, 5}, {3, 1}}

	for i, val := range vals {
		result := matrixSearch(matrix, val)
		//fmt.Println(result)
		if reflect.DeepEqual(result, expected[i]) {
			fmt.Println("Test Case", i+1, "Passed")
		} else {
			fmt.Println("Test Case", i+1, "Failed")
		}
	}

}
