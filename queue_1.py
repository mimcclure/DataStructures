#can be implemented with list, collections.deque, or queue.Queue

#using a list

#initalization
queue = []

#appending elements
queue.append('1')
queue.append('2')
queue.append('3')


#pop/remove elements from queue
queue.pop(0)
queue.pop(0)
queue.pop(0)


#using collections.deque

from collections import deque

q = deque()

q.append('1')
q.append('2')
q.append('3')

#popleft() removes and returns the left most element
q.popleft()
q.popleft()
q.popleft()

#if we call popleft again we'll raise an error since the queue is empty

#using queue module
from queue import Queue

q = Queue(maxsize=3)

#q.qsize() gives maxsize of queue

#add elements
q.put('1')
q.put('2')
q.put('3')

#boolean for a full queue
q.full()

#remove elements
q.get()
q.get()
q.get()

#boolean for an empty queue
q.empty()

#using q.put once the queue is empty and miscalling this boolean will result in an infinite loop since the queue is now empty.
