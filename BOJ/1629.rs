// 2021-08-03
// 곱셈 1629 https://www.acmicpc.net/problem/1629
use std::io;

fn pow(base: u64, exponent: u64, mod_: u64) -> u64 {
	if exponent == 0 { return 1; }
	if exponent == 1 { return base % mod_; }
	// 홀수
	if exponent % 2 == 1 { return pow(base, exponent - 1, mod_) * base % mod_; }

	let half: u64 = pow(base, exponent / 2, mod_);
	let half = half % mod_;
	return half * half % mod_;
}

fn main() {
	let mut input = String::new();

	io::stdin().read_line(&mut input).unwrap();
	let input: Vec<&str> = input.split_whitespace().collect();

	let a = input[1].parse::<u64>().unwrap();
	let b = input[1].parse::<u64>().unwrap();
	let c = input[2].parse::<u64>().unwrap();

	let result = pow(a, b, c);
	println!("{}", result);
}
