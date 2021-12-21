package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func get_input(path string) (map[[2]int]bool, []int, []bool) {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	folds := false
	fold_coords := []int{}
	fold_dirs := []bool{}
	dots := make(map[[2]int]bool)
	for scanner.Scan() {
		s := scanner.Text()
		if s == "" {
			folds = true
			continue
		}

		if folds == false {
			res := strings.Split(s, ",")
			x, _ := strconv.Atoi(res[0])
			y, _ := strconv.Atoi(res[1])
			dots[[2]int{x, y}] = false
		} else {
			res := strings.Split(s, "=")
			coord, _ := strconv.Atoi(res[1])
			fold_coords = append(fold_coords, coord)
			dir := res[0][len(res[0])-1] == 'x'
			fold_dirs = append(fold_dirs, dir)
		}
	}
	return dots, fold_coords, fold_dirs
}

func main() {
	dots, fold_coords, fold_dirs := get_input("./input.txt")
	fmt.Printf("%v\n%v\n%v\n%v\n", dots, len(dots), fold_coords, fold_dirs)
	max_x := 0
	max_y := 0
	for k := range dots {
		if max_x < k[0] {
			max_x = k[0]
		}
		if max_y < k[1] {
			max_y = k[1]
		}
	}
	fmt.Printf("%v %v\n", max_x, max_y)

	for i := 0; i < len(fold_dirs); i++ {
		coord := fold_coords[i]
		dir := fold_dirs[i]
		new_dots := make(map[[2]int]bool)
		// x case
		if dir == true {
			for k := range dots {
				if k[0] > coord {
					new_dots[[2]int{2*coord - k[0], k[1]}] = false
				} else if k[0] < coord {
					new_dots[[2]int{k[0], k[1]}] = false
				}
			}
		} else {
			for k := range dots {
				if k[1] > coord {
					new_dots[[2]int{k[0], 2*coord - k[1]}] = false
				} else if k[1] < coord {
					new_dots[[2]int{k[0], k[1]}] = false
				}
			}
		}
		dots = new_dots
		max_x = 0
		max_y = 0
		for k := range dots {
			if max_x < k[0] {
				max_x = k[0]
			}
			if max_y < k[1] {
				max_y = k[1]
			}
		}
		fmt.Printf("%v\n%v\n%v\n%v\n", dots, len(dots), max_x, max_y)
	}

	// pretty print
	res := []string{}
	for y := 0; y <= max_y; y++ {
		s := ""
		for x := 0; x <= max_x; x++ {
			if _, ok := dots[[2]int{x, y}]; ok {
				s += "#"
			} else {
				s += "."
			}
		}
		res = append(res, s)
	}
	for _, r := range res {
		fmt.Println(r)
	}
}
