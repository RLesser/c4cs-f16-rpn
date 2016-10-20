#!/usr/bin/env python3

import operator
import readline
import fractions


operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'f': fractions.Fraction
}




def calculate(myarg):
	if myarg == 'q' or myarg == 'Q':
		return 'quit'

	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		#print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	quit = False;
	fractionMode = True;
	while not quit:
		result = calculate(input("rpn calc> "))
		if result == 'quit':
			print("Goodbye!")
			quit = True;
		else:
			print("Result: ", result)

if __name__ == '__main__':
	main()