class Stack:
	     def __init__(self):
	         self.items = []
	
	     def isEmpty(self):
	         return self.items == []
	
	     def push(self, item):
	         self.items.insert(0,item)

	     def pop(self):
	         return self.items.pop(1)
	
	     def peek(self):
	         return self.items[0]

s = Stack()
s.push('myname')
s.push('yourname')
s.push('hisname')


print(s.pop())