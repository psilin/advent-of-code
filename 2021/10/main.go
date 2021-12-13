package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
)

func get_input(path string) []string {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var res []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		res = append(res, scanner.Text())
	}
	return res
}

func main() {
	res := get_input("./input.txt")
	tot_cnt := map[rune]int{'}': 0, '>': 0, ')': 0, ']': 0}
	comp_slice := []int{}
	for _, line := range res {
		stack := []rune{}
		corrupted := false
		for _, c := range line {
			if c == '{' {
				stack = append(stack, c)
			} else if c == '[' {
				stack = append(stack, c)
			} else if c == '<' {
				stack = append(stack, c)
			} else if c == '(' {
				stack = append(stack, c)
			} else if c == '}' {
				if len(stack) == 0 || stack[len(stack)-1] != '{' {
					tot_cnt[c] += 1
					corrupted = true
					break
				}
				stack = stack[:len(stack)-1]
			} else if c == ']' {
				if len(stack) == 0 || stack[len(stack)-1] != '[' {
					tot_cnt[c] += 1
					corrupted = true
					break
				}
				stack = stack[:len(stack)-1]

			} else if c == '>' {
				if len(stack) == 0 || stack[len(stack)-1] != '<' {
					tot_cnt[c] += 1
					corrupted = true
					break
				}
				stack = stack[:len(stack)-1]
			} else if c == ')' {
				if len(stack) == 0 || stack[len(stack)-1] != '(' {
					tot_cnt[c] += 1
					corrupted = true
					break
				}
				stack = stack[:len(stack)-1]
			}
		}
		if corrupted == false {
			cnt := 0
			for i := len(stack) - 1; i >= 0; i-- {
				r := 0
				if stack[i] == '(' {
					r = 1
				} else if stack[i] == '[' {
					r = 2
				} else if stack[i] == '{' {
					r = 3
				} else if stack[i] == '<' {
					r = 4
				}
				cnt = 5*cnt + r
			}
			comp_slice = append(comp_slice, cnt)
		}
	}

	fmt.Printf("%v\n", tot_cnt)
	fmt.Printf("%v\n", 3*tot_cnt[')']+57*tot_cnt[']']+1197*tot_cnt['}']+25137*tot_cnt['>'])

	sort.Ints(comp_slice)
	fmt.Printf("%v\n", comp_slice)
	fmt.Printf("%v %v\n", len(comp_slice), comp_slice[len(comp_slice)/2])
}
