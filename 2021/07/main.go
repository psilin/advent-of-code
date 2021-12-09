package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func get_input(path string) []int {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
		return nil
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	strs := strings.Split(scanner.Text(), ",")
	ln := []int{}
	for _, s := range strs {
		val, _ := strconv.Atoi(s)
		ln = append(ln, val)
	}
	sort.Ints(ln)
	return ln
}

func main() {
	ln := get_input("./input.txt")

	sums := make([]int, 1947)
	for i := 0; i < 1947; i++ {
		for _, el := range ln {
			if el < i {
				sums[i] += (i - el)
			} else {
				sums[i] += (el - i)
			}
		}
	}
	sort.Ints(sums)
	fmt.Printf("%v %v %v\n", len(sums), sums[0], sums[len(sums)-1])

	sums2 := make([]int, 1947)
	for i := 0; i < 1947; i++ {
		for _, el := range ln {
			if el < i {
				sums2[i] += (i - el) * (i - el + 1) / 2
			} else {
				sums2[i] += (el - i) * (el - i + 1) / 2
			}
		}
	}
	sort.Ints(sums2)
	fmt.Printf("%v %v %v\n", len(sums2), sums2[0], sums2[len(sums2)-1])
}
