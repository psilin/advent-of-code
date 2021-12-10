package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func get_input(path string) [][]string {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
		return nil
	}
	defer file.Close()

	var res [][]string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		res = append(res, strings.Fields(scanner.Text()))
	}
	return res
}

func extract_numbers(words []string) int {
	cnt := 0
	collect := false
	for _, w := range words {
		if w == "|" {
			collect = true
			continue
		}

		if collect == true {
			l := len(w)
			if l == 2 || l == 3 || l == 4 || l == 7 {
				cnt++
			}
		}
	}
	return cnt
}

// check if string a contains string b (substitutions does not matter)
func contains(a, b string) bool {
	for _, bchr := range b {
		if strings.Contains(a, string(bchr)) == false {
			return false
		}
	}
	return true
}

func extract_complicated(words []string) int {
	dict := [10]string{}
	d235 := []string{}
	d069 := []string{}
	// initial scan
	for _, w := range words {
		if w == "|" {
			break
		}

		l := len(w)

		if l == 2 {
			dict[1] = w
		} else if l == 3 {
			dict[7] = w
		} else if l == 4 {
			dict[4] = w
		} else if l == 7 {
			dict[8] = w
		} else if l == 5 {
			d235 = append(d235, w)
		} else if l == 6 {
			d069 = append(d069, w)
		}
	}

	// 069 case
	for _, w := range d069 {
		if contains(w, dict[4]) == true && contains(w, dict[7]) == true {
			dict[9] = w
		} else if contains(w, dict[7]) == true {
			dict[0] = w
		} else {
			dict[6] = w
		}
	}

	// 235 case
	for _, w := range d235 {
		if contains(w, dict[7]) == true {
			dict[3] = w
		} else if contains(dict[6], w) == true {
			dict[5] = w
		} else {
			dict[2] = w
		}
	}

	val := 0
	collect := false
	for _, w := range words {
		if w == "|" {
			collect = true
			continue
		}

		if collect == true {
			subval := 0
			l := len(w)
			if l == 2 {
				subval = 1
			} else if l == 3 {
				subval = 7
			} else if l == 4 {
				subval = 4
			} else if l == 5 {
				if contains(w, dict[2]) == true {
					subval = 2
				} else if contains(w, dict[3]) == true {
					subval = 3
				} else {
					subval = 5
				}
			} else if l == 6 {
				if contains(w, dict[0]) == true {
					subval = 0
				} else if contains(w, dict[6]) == true {
					subval = 6
				} else {
					subval = 9
				}
			} else if l == 7 {
				subval = 8
			}
			val = 10*val + subval
		}
	}
	return val
}

func main() {
	res := get_input("./input.txt")
	total_cnt := 0
	total_cnt_comp := 0
	for _, words := range res {
		total_cnt += extract_numbers(words)
		total_cnt_comp += extract_complicated(words)
	}
	fmt.Printf("%v %v\n", total_cnt, total_cnt_comp)
}
