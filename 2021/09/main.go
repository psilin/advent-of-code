package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func get_input(path string) [100][100]int {
	var res [100][100]int
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	i := 0
	for scanner.Scan() {
		for j, c := range scanner.Text() {
			res[i][j], _ = strconv.Atoi(string(c))
		}
		i++
	}
	return res
}

func size_of_basin(i, j int, visited *[100][100]int, res *[100][100]int, size *int) {
	*size += 1
	visited[i][j] = 1

	if i != 0 && visited[i-1][j] == 0 && res[i][j] < res[i-1][j] && res[i-1][j] < 9 {
		size_of_basin(i-1, j, visited, res, size)
	}
	if i != 99 && visited[i+1][j] == 0 && res[i][j] < res[i+1][j] && res[i+1][j] < 9 {
		size_of_basin(i+1, j, visited, res, size)
	}
	if j != 0 && visited[i][j-1] == 0 && res[i][j] < res[i][j-1] && res[i][j-1] < 9 {
		size_of_basin(i, j-1, visited, res, size)
	}
	if j != 99 && visited[i][j+1] == 0 && res[i][j] < res[i][j+1] && res[i][j+1] < 9 {
		size_of_basin(i, j+1, visited, res, size)
	}
}

func main() {
	res := get_input("./input.txt")
	var visited [100][100]int
	var basins []int

	cnt := 0
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			valid := true
			r := res[i][j]
			if i != 0 {
				valid = valid && (r < res[i-1][j])
			}
			if i != 99 {
				valid = valid && (r < res[i+1][j])
			}
			if j != 0 {
				valid = valid && (r < res[i][j-1])
			}
			if j != 99 {
				valid = valid && (r < res[i][j+1])
			}
			if valid == true {
				cnt += (r + 1)
				b_size := 0
				size_of_basin(i, j, &visited, &res, &b_size)
				basins = append(basins, b_size)
			}
		}
	}
	fmt.Printf("%v\n\n", cnt)
	fmt.Printf("%v %v\n", len(basins), basins)
	sort.Ints(basins)
	fmt.Printf("%v %v %v\n", basins[len(basins)-3], basins[len(basins)-2], basins[len(basins)-1])
	fmt.Printf("%v\n", basins[len(basins)-3]*basins[len(basins)-2]*basins[len(basins)-1])
}
