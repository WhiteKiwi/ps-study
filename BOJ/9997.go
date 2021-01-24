// 2021-01-24
// 폰트 9997 https://www.acmicpc.net/problem/9997
package main

import (
    "fmt"
	"bufio"
	"os"
)

func travel(index int, sentence int, N int, words []int) int {
    if sentence == 0b11111111111111111111111111 {
        // return int(math.Pow(2, float64(N - index)))
        return 1 << (N - index)
    }
    if index == N {
        return 0
    }
    return travel(index + 1, sentence, N, words) + travel(index + 1, sentence | words[index], N, words)
}

func char_to_bit(char rune) int {
    // a -> 1, z -> 10000 00000 00000 00000 00000 0
    return 1 << (int(char) - 97)
}

func main() {
    reader := bufio.NewReader(os.Stdin)

    var N int
    fmt.Fscanf(reader, "%d", &N)

    words := make([]int, N)
    for i := 0; i < N; i++ {
        var word_str string
        fmt.Fscan(reader, &word_str)

        word_bit := 0
        for _, char := range word_str {
            word_bit |= char_to_bit(char)
        }
        words[i] = word_bit
    }

    count_of_case := travel(0, 0, N, words)

	fmt.Println(count_of_case)
}
