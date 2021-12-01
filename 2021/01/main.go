package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("./input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	val := -1
	cnt := 0

	window3 := []int{}
	cnt3 := 0
	for scanner.Scan() {
		inp, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}

		if val >= 0 && inp > val {
			cnt += 1
		}
		val = inp

		// 3 window case
		if len(window3) == 3 {
			val3 := window3[0]
			window3 = window3[1:]
			if inp > val3 {
				cnt3 += 1
			}
		}
		window3 = append(window3, inp)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	log.Printf("%v %v\n", cnt, cnt3)
}
