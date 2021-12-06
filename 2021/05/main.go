package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Line struct {
	x1, y1, x2, y2 int
}

func (l Line) is_hor_vert() bool {
	return l.x1 == l.x2 || l.y1 == l.y2
}

func abs(i int) int {
	if i >= 0 {
		return i
	}
	return -i
}

func (l Line) point_in_line(x, y int) bool {
	if l.x1 == l.x2 && l.x1 == x {
		if (l.y1 <= y && y <= l.y2) || (l.y2 <= y && y <= l.y1) {
			return true
		}
	} else if l.y1 == l.y2 && l.y1 == y {
		if (l.x1 <= x && x <= l.x2) || (l.x2 <= x && x <= l.x1) {
			return true
		}
	} else {
		if (abs(l.x1-x)+abs(x-l.x2) == abs(l.x1-l.x2)) && (abs(l.y1-y)+abs(y-l.y2) == abs(l.y1-l.y2)) && abs(l.x1-x) == abs(l.y1-y) {
			return true
		}
	}
	return false
}

func get_line(s string) Line {
	var ln Line
	words := strings.Fields(s)
	w1 := strings.Split(words[0], ",")
	ln.x1, _ = strconv.Atoi(w1[0])
	ln.y1, _ = strconv.Atoi(w1[1])
	w2 := strings.Split(words[2], ",")
	ln.x2, _ = strconv.Atoi(w2[0])
	ln.y2, _ = strconv.Atoi(w2[1])
	return ln
}

func get_input(path string) ([]Line, []Line) {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
		return nil, nil
	}
	defer file.Close()

	var lines []Line
	var all_lines []Line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		l := scanner.Text()
		ln := get_line(l)
		if ln.is_hor_vert() {
			lines = append(lines, ln)
		}
		all_lines = append(all_lines, ln)
	}
	return lines, all_lines
}

func main() {
	tot_cnt := 0
	lines, all_lines := get_input("./input.txt")

	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			loc_cnt := 0
			for _, l := range lines {
				if l.point_in_line(x, y) {
					loc_cnt++
					if loc_cnt == 2 {
						tot_cnt++
						break
					}
				}
			}
		}
	}

	all_tot_cnt := 0
	for x := 0; x < 1000; x++ {
		for y := 0; y < 1000; y++ {
			loc_cnt := 0
			for _, l := range all_lines {
				if l.point_in_line(x, y) {
					loc_cnt++
					if loc_cnt == 2 {
						all_tot_cnt++
						break
					}
				}
			}
		}
	}

	fmt.Printf("%v %v\n", tot_cnt, all_tot_cnt)
}
