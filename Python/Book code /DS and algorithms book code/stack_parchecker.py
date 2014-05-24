"""parenthesis checker

"""
from sys import Stack

def parChecker(symbolString):
	s = Stack()
	isBalanced = True
	index = 0
	while (index < len(symbolString) and isBalanced):
		if symbolString == '(':
			s.push('(')
		else: 
			if (s.isEmpty() == True):
				isBalanced == false
			else:
				s.pop()

		index = index+1
	if balanced and isEmpty():
		return True 

	else: 
		return false

print (parChecker('(())'))


