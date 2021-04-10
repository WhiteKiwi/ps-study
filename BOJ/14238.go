// 2021-04-11
// 출근 기록 14238 https://www.acmicpc.net/problem/14238
package main

import (
	"fmt"
)

const A = 0
const B = 1
const C = 2
func travel(n int, a int, b int, before int, before2 int) bool {
	// A, B, C의 개수가 총 개수보다 초과된 경우
	if a > count[A] || b > count[B] || n - a - b > count[C] {
		return false
	}
	if n == N {
		if a == count[A] && b == count[B] {
			return true
		}
		return false
	}

	// 중복 케이스 방지
	if visited[n][a][b][before][before2] {
		return false
	}
	visited[n][a][b][before][before2] = true

	S[n] = 'A'
	if travel(n + 1, a + 1, b, A, before) {
		return true
	}

	S[n] = 'B'
	if before != B && travel(n + 1, a, b + 1, B, before) {
		return true
	}

	S[n] = 'C'
	if before != C && before2 != C && travel(n + 1, a, b, C, before) {
		return true
	}

	return false
}

var count [3]int
var N int
var S []rune
var visited [51][51][51][3][3]bool
func main() {
	for {
		var c byte
		fmt.Scanf("%c", &c)
		// 10 == '\n'
		if c == 10 { break }

		// 65 == 'A'
		count[c - 65]++
	}
	N = count[A] + count[B] + count[C]
	S = make([]rune, N)

	canWork := travel(0, 0, 0, 0, 0)
	if canWork {
		fmt.Println(string(S))
	} else {
		fmt.Println("-1")
	}
}
