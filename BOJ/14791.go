// 2021-02-21
// Tidy Numbers (Large) 14791 https://www.acmicpc.net/problem/14791
package main

import (
	"bufio"
	"fmt"
	"os"
)

const CODE_NINE = 57
const CODE_ZERO = 48

func printTidyNumber(no int, N []byte) {
	fmt.Print("Case #", no, ": ")
	// 첫 글자가 0이면 스킵함
	// 단, 숫자가 0 자체면 출력
	if N[0] != CODE_ZERO || len(N) == 1 {
		fmt.Print(string(N[0]))
	}
	for i := 1; i < len(N); i++ {
		fmt.Print(string(N[i]))
	}
	fmt.Println()
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	var T int
	fmt.Fscanf(reader, "%d", &T)

	for t := 0; t < T; t++ {
		var N []byte
		fmt.Fscan(reader, &N)

		for last := len(N) - 1; last > 0; last-- {
			for i := last; i > 0; i-- {
				// 같은 경우 비교할 곳을 앞으로 밈
				if N[i-1] == N[last] {
					continue
				}
				if N[i-1] > N[last] {
					// 0이면 9로 아니면 1을 뺌
					if N[i-1] == CODE_ZERO {
						N[i-1] = CODE_NINE
					} else {
						N[i-1]--
					}
					// 현재 검사한 위치부터 끝까지 9로 초기화
					for zero := i; zero < len(N); zero++ {
						N[zero] = CODE_NINE
					}
				}
				break
			}
		}
		printTidyNumber(t+1, N)
	}
}
