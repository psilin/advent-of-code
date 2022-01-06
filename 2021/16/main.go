package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
)

func getInput(path string) []int {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	str := scanner.Text()
	fmt.Printf("%v\n", str)
	res := []int{}
	for _, s := range str {
		val := int(s)
		if val > 60 {
			val -= 55
		} else {
			val -= 48
		}
		for i := 3; i >= 0; i-- {
			rr := int(math.Pow(2, float64(i)))
			r := val / rr
			res = append(res, r)
			val -= r * rr
		}
	}
	return res
}

func num(i, j int, res []int) int {
	val := 0
	for n := i; n < j; n++ {
		val = val*2 + res[n]
	}
	return val
}

func process(id int, op []int) int {
	if id == 0 {
		sum := 0
		for _, p := range op {
			sum += p
		}
		return sum
	} else if id == 1 {
		mul := 1
		for _, p := range op {
			mul *= p
		}
		return mul
	} else if id == 2 {
		min := op[0]
		for _, p := range op {
			if min > p {
				min = p
			}
		}
		return min
	} else if id == 3 {
		max := op[0]
		for _, p := range op {
			if max < p {
				max = p
			}
		}
		return max
	} else if id == 5 {
		if op[0] > op[1] {
			return 1
		}
		return 0
	} else if id == 6 {
		if op[0] < op[1] {
			return 1
		}
		return 0
	} else {
		if op[0] == op[1] {
			return 1
		}
		return 0
	}
}

func decodePacket(i *int, sum *int, res []int) int {
	*sum += num(*i, *i+3, res)
	t := num(*i+3, *i+6, res)
	*i += 6

	if t == 4 {
		val := 0
		for {
			flag := res[*i]
			val = val*16 + num(*i+1, *i+5, res)
			*i += 5
			if flag == 0 {
				break
			}
		}
		return val
	} else {
		I := res[*i]
		*i += 1
		op := []int{}
		if I == 0 {
			lenBits := num(*i, *i+15, res)
			*i += 15
			target := *i + lenBits
			for *i < target {
				op = append(op, decodePacket(i, sum, res))
			}
		} else {
			len := num(*i, *i+11, res)
			*i += 11
			for j := 0; j < len; j++ {
				op = append(op, decodePacket(i, sum, res))
			}
		}
		return process(t, op)
	}
}

func main() {
	res := getInput("./input.txt")
	fmt.Printf("%v\n", res)
	i := 0
	sum := 0
	result := decodePacket(&i, &sum, res)
	fmt.Printf("%v %v\n", sum, result)
}
