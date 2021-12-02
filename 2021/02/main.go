package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

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
	aim := 0
	depth := 0
	length := 0

	lines, err := get_input("./input.txt")
	if err != nil {
		log.Fatal(err)
	}

	for _, str := range lines {
		words := strings.Fields(str)
		command := words[0]
		val, err := strconv.Atoi(words[1])
		if err != nil {
			log.Fatal(err)
		}

		if command == "forward" {
			length += val
			depth += aim * val
		} else if command == "up" {
			aim -= val
			if aim < 0 {
				depth = 0
			}
		} else if command == "down" {
			aim += val
		}

	}

	fmt.Printf("%v %v %v %v %v\n", depth, length, aim, aim*length, depth*length)
}
