package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Path struct {
	Path []int
}

func (p Path) can_visit(node int, names [13]string) bool {
	if names[node] == strings.ToUpper(names[node]) {
		return true
	}

	for _, nd := range p.Path {
		if nd == node {
			return false
		}
	}
	return true
}

func (p Path) can_visit_advanced(node int, names [13]string) bool {
	if names[node] == strings.ToUpper(names[node]) {
		return true
	}

	if names[node] == "start" {
		return false
	}

	var cnt [13]int
	for _, nd := range p.Path {
		cnt[nd] += 1
	}

	has_two := false
	for i := 0; i < 13; i++ {
		if (cnt[i] > 1) && names[i] != strings.ToUpper(names[i]) {
			has_two = true
		}
	}

	for _, nd := range p.Path {
		if nd == node {
			return !has_two
		}
	}
	return true
}

func (p Path) extend(node int) Path {
	var newp Path
	newp.Path = make([]int, len(p.Path)+1)
	copy(newp.Path, p.Path)
	newp.Path[len(p.Path)] = node
	return newp
}

func (p Path) where_can_go(conns [13][13]bool) []int {
	res := []int{}
	if len(p.Path) == 0 {
		return res
	}

	node := p.Path[len(p.Path)-1]

	for i, connected := range conns[node] {
		if connected == true {
			res = append(res, i)
		}
	}
	return res
}

func get_input(path string) ([13][13]bool, [13]string) {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	cnt := 0
	nums := make(map[string]int)
	var conns [13][13]bool
	var names [13]string
	for scanner.Scan() {
		strs := strings.Split(scanner.Text(), "-")
		for i := 0; i <= 1; i++ {
			_, ok := nums[strs[i]]
			if ok == false {
				nums[strs[i]] = cnt
				names[cnt] = strs[i]
				cnt++
			}
		}
		conns[nums[strs[0]]][nums[strs[1]]] = true
		conns[nums[strs[1]]][nums[strs[0]]] = true
	}
	fmt.Printf("%v\n", cnt)
	return conns, names
}

func search(start_idx, end_idx int, conns [13][13]bool, names [13]string, advanced bool) {
	var p Path
	p = p.extend(start_idx)
	cur_paths := []Path{p}
	success_paths := []Path{}
	for len(cur_paths) > 0 {
		new_paths := []Path{}
		for _, pth := range cur_paths {
			possible_nodes := pth.where_can_go(conns)
			for _, nd := range possible_nodes {
				if nd == end_idx {
					success_paths = append(success_paths, pth.extend(nd))
				} else if advanced == false && pth.can_visit(nd, names) == true {
					new_paths = append(new_paths, pth.extend(nd))
				} else if advanced == true && pth.can_visit_advanced(nd, names) == true {
					new_paths = append(new_paths, pth.extend(nd))
				}
			}
		}
		cur_paths = new_paths
	}
	fmt.Printf("%v\n", len(success_paths))
}

func main() {
	conns, names := get_input("./input.txt")
	fmt.Printf("%v\n%v\n", conns, names)

	start_idx := -1
	end_idx := -1
	for i, n := range names {
		if n == "start" {
			start_idx = i
		} else if n == "end" {
			end_idx = i
		}
	}
	if start_idx < 0 || end_idx < 0 {
		log.Fatal("Can not find start/end index")
	}

	search(start_idx, end_idx, conns, names, false)
	search(start_idx, end_idx, conns, names, true)
}
