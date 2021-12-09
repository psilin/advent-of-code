package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Lantern struct {
	Timer int
}

func NewLantern() *Lantern {
	return &Lantern{Timer: 8}
}

func NewLanternI(i int) *Lantern {
	return &Lantern{Timer: i}
}

func (l *Lantern) day() bool {
	l.Timer -= 1
	if l.Timer == -1 {
		l.Timer = 6
		return true
	}
	return false
}

func get_input(path string) ([]*Lantern, [9]int) {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
		return nil, [9]int{}
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	strs := strings.Split(scanner.Text(), ",")
	ls := []*Lantern{}
	var ln [9]int
	for _, s := range strs {
		val, _ := strconv.Atoi(s)
		ls = append(ls, &Lantern{Timer: val})
		ln[val] += 1
	}
	return ls, ln
}

func main() {
	ls, ln := get_input("./input.txt")
	for i := 0; i < 80; i++ {
		day_cnt := 0
		for _, l := range ls {
			res := l.day()
			if res == true {
				day_cnt += 1
			}
		}
		for j := 0; j < day_cnt; j++ {
			ls = append(ls, NewLantern())
		}
		fmt.Printf("%v %v\n", i, len(ls))
	}
	fmt.Printf("%v\n", len(ls))

	lln := ln[:]
	for i := 0; i < 256; i++ {
		reset := lln[0]
		lln = lln[1:]
		lln[6] += reset
		lln = append(lln, reset)

		sum := 0
		for j := 0; j <= 8; j++ {
			sum += lln[j]
		}
		fmt.Printf("%v %v\n", i, sum)
	}
}
