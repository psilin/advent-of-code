package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func getInput(path string) (map[string]string, map[string]int, string) {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	rules := false

	str := make(map[string]int)
	dict := make(map[string]string)
	bound := ""

	for scanner.Scan() {
		s := scanner.Text()
		if s == "" {
			rules = true
			continue
		}

		if rules == false {
			bound = string(s[0]) + string(s[len(s)-1])
			for i := 0; i < len(s)-1; i++ {
				ss := string(s[i]) + string(s[i+1])
				val, ok := str[ss]
				if ok == true {
					str[ss] = val + 1
				} else {
					str[ss] = 1
				}
			}
		} else {
			words := strings.Fields(s)
			dict[words[0]] = words[2]
		}
	}
	return dict, str, bound
}

func Step(dict map[string]string, str map[string]int, bound string, steps int) {
	// steps
	for i := 0; i < steps; i++ {
		new_str := make(map[string]int)

		for key, val := range str {
			dict_val, ok := dict[key]
			if ok == true {
				first := string(key[0]) + string(dict_val)
				fval, ok := new_str[first]
				if ok == true {
					new_str[first] = fval + val
				} else {
					new_str[first] = val
				}

				second := string(dict_val) + string(key[1])
				sval, ok := new_str[second]
				if ok == true {
					new_str[second] = sval + val
				} else {
					new_str[second] = val
				}
			} else {
				oldval, ok := new_str[key]
				if ok == true {
					new_str[key] = oldval + val
				} else {
					new_str[key] = val
				}
			}
		}
		str = new_str
	}

	// count
	cnt := make(map[string]int)
	for key, val := range str {
		first := string(key[0])
		fval, ok := cnt[first]
		if ok == true {
			cnt[first] = fval + val
		} else {
			cnt[first] = val
		}

		second := string(key[1])
		sval, ok := cnt[second]
		if ok == true {
			cnt[second] = sval + val
		} else {
			cnt[second] = val
		}
	}

	cnt[string(bound[0])] += 1
	cnt[string(bound[1])] += 1
	max := cnt[string(bound[1])]
	min := cnt[string(bound[0])]
	for _, val := range cnt {
		if val > max {
			max = val
		}

		if val < min {
			min = val
		}
	}
	fmt.Printf("%v %v %v\n", max, min, (max-min)/2)
}

func main() {
	dict, str, bound := getInput("./input.txt")
	fmt.Printf("%v\n%v\n%v\n", dict, str, bound)
	Step(dict, str, bound, 10)
	Step(dict, str, bound, 40)
}
