#!/usr/bin/python3

import operator

def add(a,b):
	return a + b;

operators = {
	'+' : operator.add,
	'-' : operator.sub,
	'*' : operator.mul,
	'/' : operator.truediv
}


def calculate(string):
	stack = []
	for token in string.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = operators[token]
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError
	return stack.pop()

def main():
	while True:
		calculate(raw_input("rpn calc> "))

if __name__ == '__main__':
	main()