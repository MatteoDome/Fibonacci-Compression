## Fibonacci Compression Algorithm

import sys
import os
import numpy as np

def generate_sequence(n):
	fib = [1]
	f0 = 1
	f1 = 1
	f_sum = f0 + f1
	while (n >= f_sum):
		fib.append(f_sum)
		tmp = f1
		f1 = f_sum
		f_sum = tmp + f1
	print(fib)
	return fib


def encode(n):
	if n >= 1 and n < 514228:
		fib = generate_sequence(n)
		code = '1'
		print(code)
		for i in reversed(fib):
			if n >= i:
				n = n - i
				code = '1' + code
			else:
				code = '0' + code
			print(code)
		return code
	else:
		print("Please enter a valid positive integer")
		return 0

def decode(n):
	

if __name__ == "__main__":
	if sys.argv[1] == 'e' and sys.argv[2].isdigit():
		n = int(sys.argv[2])
		print('Encoding ', n, ' using Fibonacci compression...')
		output = encode(n)
		print('The Fibonacci coding for ', n, 'is ', output)
	if sys.argv[1] == 'd' and sys.argv[2].isdigit():
		n = int(sys.argv[2])
		print('Decoding ', n, ' using Fibonacci compression...')
		output = encode(n)
		print('The input ', n, 'represents the Fibonacci code for ', output)