package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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
	for _, line := range res {
		stack := []rune{}
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
					break
				}
				stack = stack[:len(stack)-1]
			} else if c == ']' {
				if len(stack) == 0 || stack[len(stack)-1] != '[' {
					tot_cnt[c] += 1
					break
				}
				stack = stack[:len(stack)-1]

			} else if c == '>' {
				if len(stack) == 0 || stack[len(stack)-1] != '<' {
					tot_cnt[c] += 1
					break
				}
				stack = stack[:len(stack)-1]
			} else if c == ')' {
				if len(stack) == 0 || stack[len(stack)-1] != '(' {
					tot_cnt[c] += 1
					break
				}
				stack = stack[:len(stack)-1]
			}
		}
	}

	fmt.Printf("%v\n", tot_cnt)
	fmt.Printf("%v\n", 3*tot_cnt[')']+57*tot_cnt[']']+1197*tot_cnt['}']+25137*tot_cnt['>'])
}
