package main

import (
	"fmt"
)

/*
minOperationsToReach calculates the minimum number of operations needed to reach a target character count.
*/
func minOperations(n int) int {
	totalOperations := 0

	for factor := 2; factor <= n; factor++ {
		for n%factor == 0 {
			totalOperations += factor
			n /= factor
		}
	}

	return totalOperations
}

func main() {
	n := 9
	minOperations := minOperations(n)

	fmt.Printf("Minimum number of operations to reach %d characters: %d\n", n, minOperations)
}
