#stack implements - list, Collections.deque, queue.LifoQueue
#empty() T/F TC: O(1)
#size() TC: O(1)
#top()/peek() TC: O(1)
#push(_) insert at the top of the stack TC: O(1)
#pop(_) remove the topmost element TC: O(1)

stack = []

stack.append('1')
stack.append('2')
stack.append('3')

print(stack)

stack.pop() #3
stack.pop() #2
stack.pop() #1

print("Empty stack: ", stack)

from collections import deque

stack.append('1')
stack.append('2')
stack.append('3')

stack.pop()
stack.pop()
stack.pop()

from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print(stack.qsize())

stack.put('1')
stack.put('2')
stack.put('3')

#to pop

stack.get()
stack.get()
stack.get()

#stack is now empty