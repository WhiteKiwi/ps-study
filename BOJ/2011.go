// 2021-01-31
// 암호코드 2011 https://www.acmicpc.net/problem/2011
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	var code string
	fmt.Fscan(reader, &code)

	dp := make([]int, 10000)
	dp[len(code)] = 1
	// 마지막 자리가 0인 케이스 처리
	if code[len(code) - 1] == '0' {
		dp[len(code) - 1] = 0
	} else {
		dp[len(code) - 1] = 1
	}
	for i := len(code) - 2; i >= 0; i-- {
		// dp['1223'] = 0
		// 앞 한자리가 0이 아니면
		// dp['1223'] += dp['223']
		// 앞 두자리가 1~26 사이면
		// dp['1223'] += dp['23']
		dp[i] = 0
		if code[i] != '0' {
			dp[i] += dp[i + 1]
		}
		// 앞자리가 1~2 이고 뒷자리가 7보다 작아야 함, char(55) == '7'
		if code[i] == '1' || (code[i] == '2' && int(code[i + 1]) < 55) {
			dp[i] += dp[i + 2]
		}
		dp[i] %= 1000000
	}
	fmt.Println(dp[0] % 1000000)
}
