package main

import (
	"fmt"
)

/*
minOperationsToReach calculates the minimum number of operations needed to reach a target character count.
*/
func minOperations(n int) int {
	if n <= 0 || n == 1 {
		return 0
	}

	ops := 0
	i := 2

	for i <= n {
		for n % i == 0 {
			ops += i
			n = n / i
		}
		i++
	}
	return ops
}

func main() {
	n := 9
	minOperations := minOperations(n)

	fmt.Printf("Minimum number of operations to reach %d characters: %d\n", n, minOperations)
}
