package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

type Deque struct {
	queue [][2]int
}

func (d *Deque) Size() int {
	return len(d.queue)
}

func (d *Deque) PopFront() [2]int {
	res := d.queue[0]
	d.queue = d.queue[1:]
	return res
}

func (d *Deque) PushBack(val [2]int) {
	d.queue = append(d.queue, val)
}

func NewDeque() Deque {
	q := make([][2]int, 0)
	var res Deque
	res.queue = q
	return res
}

func getInput(path string) [100][100]int {
	var res [100][100]int
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for i := 0; i < 100; i++ {
		scanner.Scan()
		s := scanner.Text()
		for j := 0; j < 100; j++ {
			val, err := strconv.Atoi(string(s[j]))
			if err != nil {
				log.Fatal(err)
			}
			res[i][j] = val
		}

	}
	return res
}

func ConstructTable(t [100][100]int) [500][500]int {
	var nt [500][500]int
	for ii := 0; ii < 5; ii++ {
		for jj := 0; jj < 5; jj++ {
			for i := 0; i < 100; i++ {
				for j := 0; j < 100; j++ {
					nt[100*ii+i][100*jj+j] = (t[i][j]+ii+jj-1)%9 + 1
				}
			}
		}
	}
	return nt
}

func main() {
	// 100 case
	table := getInput("./input.txt")
	fmt.Printf("%v\n", table)
	var cov_table [100][100]int
	d := NewDeque()
	d.PushBack([2]int{0, 0})

	for d.Size() > 0 {
		p := d.PopFront()
		i := p[0]
		j := p[1]

		bval := cov_table[i][j]

		if i > 0 {
			val := cov_table[i-1][j]
			if val == 0 || val > (bval+table[i-1][j]) {
				cov_table[i-1][j] = bval + table[i-1][j]
				d.PushBack([2]int{i - 1, j})
			}
		}
		if i < 99 {
			val := cov_table[i+1][j]
			if val == 0 || val > (bval+table[i+1][j]) {
				cov_table[i+1][j] = bval + table[i+1][j]
				d.PushBack([2]int{i + 1, j})
			}
		}
		if j > 0 {
			val := cov_table[i][j-1]
			if val == 0 || val > (bval+table[i][j-1]) {
				cov_table[i][j-1] = bval + table[i][j-1]
				d.PushBack([2]int{i, j - 1})
			}
		}
		if j < 99 {
			val := cov_table[i][j+1]
			if val == 0 || val > (bval+table[i][j+1]) {
				cov_table[i][j+1] = bval + table[i][j+1]
				d.PushBack([2]int{i, j + 1})
			}
		}
	}
	fmt.Printf("RESULT 100: %v\n", cov_table)

	// 500 case
	table500 := ConstructTable(table)
	fmt.Printf("%v\n", table500)
	var cov_table500 [500][500]int
	d.PushBack([2]int{0, 0})

	for d.Size() > 0 {
		p := d.PopFront()
		i := p[0]
		j := p[1]

		bval := cov_table500[i][j]

		if i > 0 {
			val := cov_table500[i-1][j]
			if val == 0 || val > (bval+table500[i-1][j]) {
				cov_table500[i-1][j] = bval + table500[i-1][j]
				d.PushBack([2]int{i - 1, j})
			}
		}
		if i < 499 {
			val := cov_table500[i+1][j]
			if val == 0 || val > (bval+table500[i+1][j]) {
				cov_table500[i+1][j] = bval + table500[i+1][j]
				d.PushBack([2]int{i + 1, j})
			}
		}
		if j > 0 {
			val := cov_table500[i][j-1]
			if val == 0 || val > (bval+table500[i][j-1]) {
				cov_table500[i][j-1] = bval + table500[i][j-1]
				d.PushBack([2]int{i, j - 1})
			}
		}
		if j < 499 {
			val := cov_table500[i][j+1]
			if val == 0 || val > (bval+table500[i][j+1]) {
				cov_table500[i][j+1] = bval + table500[i][j+1]
				d.PushBack([2]int{i, j + 1})
			}
		}
	}
	fmt.Printf("RESULT 500: %v\n", cov_table500)
	fmt.Printf("%v\n", -1%9)
}
