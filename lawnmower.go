package main

import (
	"fmt"
	"log"
)

type Problem struct {
	width, height int
	pattern       [][]int
}

func readProblem() Problem {
	var w, h int
	fmt.Scanf("%d %d\n", &h, &w)
	pattern := make([][]int, h)
	for i := 0; i < h; i++ {
		line := make([]int, w)
		for j := 0; j < w; j++ {
			var k int
			fmt.Scanf("%d", &k)
			line[j] = k
		}
		pattern[i] = line
	}
	return Problem{w, h, pattern}
}

func solve(p Problem) {
	horizontal := make([]int, p.height)
	vertical := make([]int, p.width)

	for y := 0; y < p.height; y++ {
		max := 1
		for x := 0; x < p.width; x++ {
			if p.pattern[y][x] > max {
				max = p.pattern[y][x]
			}
		}
		horizontal[y] = max
	}
	log.Println("horizontal:", horizontal)

	for x := 0; x < p.width; x++ {
		max := 1
		for y := 0; y < p.height; y++ {
			if p.pattern[y][x] > max {
				max = p.pattern[y][x]
			}
		}
		vertical[x] = max
	}
	log.Println("vertical:", vertical)

	for y := 0; y < p.height; y++ {
		for x := 0; x < p.width; x++ {
			h := p.pattern[y][x]
			if h != horizontal[y] && h != vertical[x] {
				fmt.Println("NO")
				return
			}
		}
	}
	fmt.Println("YES")
}

func main() {
	var t int
	fmt.Scanf("%d\n", &t)
	log.Println("T=", t)

	for i := 1; i <= t; i++ {
		problem := readProblem()
		fmt.Printf("Case #%d: ", i)
		solve(problem)
	}
}
