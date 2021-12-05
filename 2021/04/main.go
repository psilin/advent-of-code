package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Board struct {
	Lines [5][5]int
}

func (b Board) sum_line(line int, row bool) int {
	sum := 0
	if row == true {
		for i := 0; i < 5; i++ {
			sum += b.Lines[line][i]
		}
	} else {
		for i := 0; i < 5; i++ {
			sum += b.Lines[i][line]
		}
	}
	return sum
}

func (b Board) sum_unmarked(numbers []int) int {
	sum := 0
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			elem_found := false
			for _, k := range numbers {
				if k == b.Lines[i][j] {
					elem_found = true
					break
				}
			}

			if elem_found == false {
				sum += b.Lines[i][j]
			}
		}
	}
	return sum
}

func (b Board) check_bingo(numbers []int) int {
	for i := 0; i < 5; i++ {
		found_line := true
		for j := 0; j < 5; j++ {
			elem_found := false
			for _, k := range numbers {
				if k == b.Lines[i][j] {
					elem_found = true
					break
				}
			}

			if elem_found == false {
				found_line = false
				break
			}
		}

		if found_line == true {
			return b.sum_line(i, true)
		}
	}

	for i := 0; i < 5; i++ {
		found_line := true
		for j := 0; j < 5; j++ {
			elem_found := false
			for _, k := range numbers {
				if k == b.Lines[j][i] {
					elem_found = true
					break
				}
			}

			if elem_found == false {
				found_line = false
				break
			}
		}

		if found_line == true {
			return b.sum_line(i, false)
		}
	}

	return -1
}

func get_input(path string) ([]int, []Board, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, nil, err
	}
	defer file.Close()

	var numbers []int
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	split := strings.Split(scanner.Text(), ",")
	for _, i := range split {
		val, err := strconv.Atoi(i)
		if err != nil {
			log.Fatal(err)
		}
		numbers = append(numbers, val)
	}

	fmt.Println(numbers)

	var boards []Board
	scanner.Scan()
	tmp_board := Board{}
	cnt := 0
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			boards = append(boards, tmp_board)
			tmp_board = Board{}
			cnt = 0
		} else {
			words := strings.Fields(line)
			for i, word := range words {
				val, err := strconv.Atoi(word)
				if err != nil {
					log.Fatal(err)
				}
				tmp_board.Lines[cnt][i] = val
			}
			cnt++
		}
	}
	boards = append(boards, tmp_board)
	fmt.Println(boards)
	return numbers, boards, nil
}

func main() {
	numbers, boards, err := get_input("./input.txt")
	if err != nil {
		log.Fatal(err)
	}

	for i := 0; i < len(numbers); i++ {
		num_tmp := numbers[0 : i+1]
		for j := 0; j < len(boards); j++ {
			res := boards[j].check_bingo(num_tmp)
			if res >= 0 {
				sum := boards[j].sum_unmarked(num_tmp)
				fmt.Printf("%v %v %v\n", sum, numbers[i], sum*numbers[i])
				goto NEXT
			}
		}
	}

NEXT:
	i := 0
	for {
		num_tmp := numbers[0 : i+1]
		j := 0
		for {
			res := boards[j].check_bingo(num_tmp)
			if res >= 0 && len(boards) == 1 {
				sum := boards[j].sum_unmarked(num_tmp)
				fmt.Printf("%v %v %v\n", sum, numbers[i], sum*numbers[i])
				return
			} else if res >= 0 {
				boards = append(boards[:j], boards[j+1:]...)
			} else {
				j += 1
			}

			if j == len(boards) {
				break
			}

		}
		i += 1
		if i == len(numbers) {
			break
		}
	}

	for i := 0; i < len(numbers); i++ {
		num_tmp := numbers[0 : i+1]
		for j := 0; j < len(boards); j++ {
			res := boards[j].check_bingo(num_tmp)
			if res >= 0 {
				sum := boards[j].sum_unmarked(num_tmp)
				fmt.Printf("%v %v %v\n", sum, numbers[i], sum*numbers[i])
				goto NEXT
			}
		}
	}
}
