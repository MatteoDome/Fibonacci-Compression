## Fibonacci Compression Algorithm

import sys
import os
import numpy as np

def generate_sequence(n, mode):
	fib = [1]
	f0 = 1
	f1 = 1
	f_sum = f0 + f1
	if mode == 'e':
		while (n >= f_sum):
			fib.append(f_sum)
			tmp = f1
			f1 = f_sum
			f_sum = tmp + f1
	elif mode == 'd':
		n = list(map(int, str(n)))
		n = n[:-1]
		for i in range (len(n)+1):
			fib.append(f_sum)
			tmp = f1
			f1 = f_sum
			f_sum = tmp + f1
	return fib


def encode(n, mode):
	if n >= 1 and n < 514228:
		fib = generate_sequence(n, mode)
		code = '1'
		for i in reversed(fib):
			if n >= i:
				n = n - i
				code = '1' + code
			else:
				code = '0' + code
		return code

def decode(n, mode):
	if len(n) > 1:
		result = 0
		fib = generate_sequence(int(n), mode)
		n = list(map(int, str(n)))
		n = n[:-1]
		for pos in range (0, len(n)):
			result = result + fib[pos]*n[pos]

		return result

	else:
		print('Please enter a valid sequence')

if __name__ == "__main__":
	if sys.argv[1] == 'e' and sys.argv[2].isdigit():
		mode = str(sys.argv[1])
		n = int(sys.argv[2])
		print('Encoding ', n, ' using Fibonacci compression...')
		output = encode(n, mode)
		print('The Fibonacci coding for ', n, 'is ', output)
	elif sys.argv[1] == 'd' and sys.argv[2].isdigit():
		mode = str(sys.argv[1])
		n = str(sys.argv[2])
		print('Decoding ', n, ' using Fibonacci compression...')
		output = decode(n, mode)
		print('The input ', n, 'represents the Fibonacci code for ', output)
	else:
		print('Please use the format "compression.py <e|d> <integer to encode/decode>".')