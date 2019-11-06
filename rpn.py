#!/usr/bin/env python3
#
# Reverse polish notation 


# Operation functions for calculator
operations = {}
operations['+'] = lambda x,y : x + y
operations['-'] = lambda x,y : x - y
operations['*'] = lambda x,y : x * y
operations['/'] = lambda x,y : x / y
operations['**'] = lambda x,y : x ** y
operations['%'] = lambda x,y : x % y


def rpn(expr):
	'''Expression should be split by spaces and consist of numbers 
	and operations in reverse polish notation. Returns result'''
	global operations

	stack = []
	parsed = expr.split()

	if len(parsed) == 1:
		return int(parsed[0])

	stack.append(int(parsed[0]))

	for i in range(1, len(parsed)):
		if parsed[i] in operations and len(stack) != 2:
			return None

		elif parsed[i] in operations:

			arg2 = stack.pop()
			arg1 = stack.pop()

			func = operations[parsed[i]]
			stack.append(func(arg1, arg2))

		else:
			stack.append(int(parsed[i]))

	return stack[0]


def main():
	try:	
		while(1):
			expr = input("rpn> ")
			print(rpn(expr))

	except KeyboardInterrupt:
		print("Quiting...\n")

if __name__ == '__main__':
	main()