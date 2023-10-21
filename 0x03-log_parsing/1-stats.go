package main

import (
	"bufio"
	"fmt"
	"os"
	"os/signal"
	"regexp"
	"sort"
	"strconv"
	"syscall"
)

var (
	totalSize int
	statusMap = make(map[int]int)
)

// printStats prints the total file size and the count of each status code.
func printStats() {
	fmt.Printf("Total file size: %d\n", totalSize)
	var keys []int
	for k := range statusMap {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	for _, k := range keys {
		fmt.Printf("%d: %d\n", k, statusMap[k])
	}
}


// main reads from stdin, parses each line using a regular expression, and updates the total file size and the status code count.
// After every 10 lines or when a keyboard interruption (CTRL + C) is detected, it invokes printStats to print the statistics.
// If there's an error reading from stdin, it prints that error to stderr.
func main() {
	scanner := bufio.NewScanner(os.Stdin)
	lines := 0

	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		printStats()
		os.Exit(1)
	}()

	for scanner.Scan() {
		lines++
		line := scanner.Text()

        re := regexp.MustCompile(`\s*(?P<ip>\S+)\s*- \[(?P<date>[^\]]+)\] "(?P<method>GET) (?P<res>/projects/260) (?P<proto>HTTP/1\.1)" (?P<status_code>\d+) (?P<file_size>\d+)\s*`)
        match := re.FindStringSubmatch(line)

        if len(match) == 0 {
            continue
        }

        size, err := strconv.Atoi(match[7])
        if err != nil {
            continue
        }
        totalSize += size

        status, err := strconv.Atoi(match[6])
        if err != nil {
            continue
        }

        if status == 200 || status == 301 || status == 400 || status == 401 || status == 403 || status == 404 || status == 405 || status == 500 {
            statusMap[status]++
        }

        if lines%10 == 0 {
            printStats()
        }
    }

    if err := scanner.Err(); err != nil {
        fmt.Fprintln(os.Stderr, "reading standard input:", err)
    }
}
