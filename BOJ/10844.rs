// 2021-08-03
// 쉬운 계단 수 10844 https://www.acmicpc.net/problem/10844
use std::io;

fn main() {
	let mut input = String::new();
	io::stdin().read_line(&mut input).unwrap();
	let n = input.trim().parse::<usize>().unwrap();

	let mut dp: [[u64; 11]; 101] = [[0; 11]; 101];

	for i in 1..10 {
		dp[1][i] = 1;
	}

	for i in 2..n+1 {
        dp[i][0] = dp[i - 1][1];
		for j in 1..10 {
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000;
		}
	}
 
    let mut sum = 0;
    for i in 0..10 {
        sum += dp[n][i];
    }
    
	println!("{}", sum % 1000000000);
}
