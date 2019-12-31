from base import UnderflowError, Node, DynamicSet


class Stack(DynamicSet):
	def peek(self):
		if self.empty():
			raise UnderflowError('Peeking at an empty stack is not allowed.')
		return self.sentinel.next.data

	def push(self, data):
		new_node = Node(data=data)
		self.sentinel.insert_after(new_node)
		self.size += 1

	def pop(self):
		if self.empty():
			raise UnderflowError('Trying to pop from an empty stack.')
		removed_node = self.sentinel.delete_after()
		self.size -= 1
		return removed_node.data

	def build_from_arr(self, arr):
		for i in range(len(arr) - 1, -1, -1):
			self.push(arr[i])

