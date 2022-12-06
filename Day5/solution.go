package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func parsePuzzle() int {
	var fname string
	fname = "./sample.txt"
	if len(os.Args) > 1 {
		fname = os.Args[1]
	}
	var file, err = os.Open(fname)
	if err != nil {
		panic(err)
	}
	var scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		if strings.HasPrefix(scanner.Text(), "move") {
			fmt.Println(scanner.Text())
		}
	}
	return 2
}

func main() {
	fmt.Println("asdasd", parsePuzzle())
}
