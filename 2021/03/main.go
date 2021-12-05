package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

const LENGTH = 12

func get_input(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func main() {
	var ones [LENGTH]int
	var zeros [LENGTH]int

	lines, err := get_input("./input.txt")
	if err != nil {
		log.Fatal(err)
	}

	for _, str := range lines {
		for pos, char := range str {
			if char == '0' {
				zeros[pos] += 1
			} else if char == '1' {
				ones[pos] += 1
			}
		}
	}

	gamma := 0
	epsilon := 0
	for i := 0; i < LENGTH; i++ {
		if zeros[i] > ones[i] {
			epsilon += int(math.Pow(2, float64(LENGTH-1-i)))
		} else {
			gamma += int(math.Pow(2, float64(LENGTH-1-i)))
		}
	}

	fmt.Printf("%v %v %v %v %v\n", zeros, ones, gamma, epsilon, gamma*epsilon)

	var oxygen_generator_rating string
	tmp_lines := lines
	for i := 0; i < LENGTH; i++ {
		var tmp0_lines []string
		var tmp1_lines []string
		for _, l := range tmp_lines {
			if l[i] == '1' {
				tmp1_lines = append(tmp1_lines, l)
			} else {
				tmp0_lines = append(tmp0_lines, l)
			}
		}
		if len(tmp1_lines) >= len(tmp0_lines) {
			tmp_lines = tmp1_lines
		} else {
			tmp_lines = tmp0_lines
		}

		if len(tmp_lines) == 1 {
			oxygen_generator_rating = tmp_lines[0]
			break
		}
	}

	ogr, err := strconv.ParseInt(oxygen_generator_rating, 2, 64)
	if err != nil {
		log.Fatal(err)
	}

	var co2_scrubber_rating string
	tmp_lines = lines
	for i := 0; i < LENGTH; i++ {
		var tmp0_lines []string
		var tmp1_lines []string
		for _, l := range tmp_lines {
			if l[i] == '1' {
				tmp1_lines = append(tmp1_lines, l)
			} else {
				tmp0_lines = append(tmp0_lines, l)
			}
		}
		if len(tmp0_lines) <= len(tmp1_lines) {
			tmp_lines = tmp0_lines
		} else {
			tmp_lines = tmp1_lines
		}

		if len(tmp_lines) == 1 {
			co2_scrubber_rating = tmp_lines[0]
			break
		}
	}
	csr, err := strconv.ParseInt(co2_scrubber_rating, 2, 64)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("%v %v %v\n", ogr, csr, csr*ogr)
}
