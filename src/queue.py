from .base import Node, Iterator, UnderflowError, DynamicSet


class Queue(DynamicSet):
	def __init__(self, arr=None):
		self.size = 0
		self.sentinel = Node()
		self.sentinel.next = self.sentinel
		self._last_node = self.sentinel
		if arr: self.build_from_arr(arr)

	def peek(self):
		if self.empty():
			raise UnderflowError('Trying to peek at an empty queue.')
		return self.sentinel.next.data

	def enqueue(self, data):
		last = self._last_node
		new_node = Node(data=data)
		last.insert_after(new_node)
		self._last_node = new_node
		self.size += 1

	def dequeue(self):
		if self.empty():
			raise UnderflowError('Trying to dequeue from an empty queue.')
		removed_node = self.sentinel.delete_after()
		self.size -= 1
		return removed_node.data

	def build_from_arr(self, arr):
		for element in arr:
			self.enqueue(element)

