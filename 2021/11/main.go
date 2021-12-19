package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func get_input(path string) [10][10]int {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var res [10][10]int
	scanner := bufio.NewScanner(file)
	cnt := 0
	for scanner.Scan() {
		for i, r := range scanner.Text() {
			res[cnt][i], _ = strconv.Atoi(string(r))
		}
		cnt += 1
	}
	return res
}

func step(res *[10][10]int) int {
	// initial
	cnt := 0
	var proc [10][10]bool
	proc_slice := make([][2]int, 0, 100)
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			res[i][j] += 1
			if res[i][j] > 9 {
				if proc[i][j] == false {
					proc[i][j] = true
					point := [2]int{i, j}
					proc_slice = append(proc_slice, point)
				}
			}
		}
	}

	for len(proc_slice) > 0 {
		new_proc_slice := make([][2]int, 0, 100)

		for _, p := range proc_slice {
			i := p[0]
			j := p[1]

			cnt += 1
			res[i][j] = 0

			for ii := i - 1; ii <= i+1; ii++ {
				for jj := j - 1; jj <= j+1; jj++ {
					if ii >= 0 && ii < 10 && jj >= 0 && jj < 10 {
						if res[ii][jj] > 0 {
							res[ii][jj] += 1
							if res[ii][jj] > 9 {
								if proc[ii][jj] == false {
									proc[ii][jj] = true
									var point = [2]int{ii, jj}
									new_proc_slice = append(new_proc_slice, point)
								}
							}
						}
					}
				}
			}
		}
		proc_slice = new_proc_slice
	}
	return cnt
}

func main() {
	res := get_input("./input.txt")
	fmt.Printf("%v\n", res)
	tot_cnt := 0
	for i := 0; ; i++ {
		fmt.Printf("%v\n", i)
		cnt := step(&res)
		tot_cnt += cnt
		fmt.Printf("step %v loc %v tot %v\n", i+1, cnt, tot_cnt)
		if cnt == 100 {
			break
		}
	}
	fmt.Printf("%v\n", tot_cnt)
}
