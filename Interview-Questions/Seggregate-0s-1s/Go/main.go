//###   Segregate 0s and 1s from an array
//###   https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s5106/0

package main

import (
	"fmt"
	"reflect"
	"sort"
)

func sortArr(arr []int) []int {
	n := len(arr)
	m := 0
	swap := false

	for i := 0; i < n; i++ {
		if arr[i] == 1 && !swap {
			m = i
			swap = true
		}
		if arr[i] == 0 && swap {
			arr[m], arr[i] = arr[i], arr[m]
			m += 1
		}
	}
	return arr
}

func main() {
	fmt.Println("Hello world!")
	arr1 := []int{0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0}
	arr2 := []int{1, 0, 1, 1, 1, 0, 0, 0, 0, 0}
	arrs := [][]int{arr1, arr2}

	for i, arr := range arrs {
		result := sortArr(arr)
		sort.Ints(arr)
		//fmt.Println(result)
		if reflect.DeepEqual(result, arr) {
			fmt.Println("Test Case", i, "passed")
		} else {
			fmt.Println("Test Case", i, "failed")
		}
	}
}
