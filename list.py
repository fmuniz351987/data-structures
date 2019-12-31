from base import Node, UnderflowError, DynamicSet


class List(DynamicSet):
	def __getitem__(self, index):
		self._raise_if_invalid_index(index)
		for i, data in enumerate(self):
			if i == index:
				return data

	def __setitem__(self, index, data):
		self._raise_if_invalid_index(index)
		for i, node in enumerate(self._nodes()):
			if i == index:
				node.data = data

	def _raise_if_invalid_index(self, index):
		if index >= len(self) or index < 0: raise IndexError('List index out of bounds')

	def search(self, key):
		for data in self:
			if self.key(data) == key:
				return data
		else:
			return None

	def insert(self, data):
		new_node = Node(data)
		self.sentinel.insert_after(new_node)
		self.size += 1

	def delete(self, key):
		node = self.sentinel
		while node.next != self.sentinel:
			if self.key(node.next.data) == key:
				break
			node = node.next
		else:
			return None
		removed_node = node.delete_after()
		self.size -= 1
		return removed_node.data

	def build_from_arr(self, arr):
		for element in arr:
			self.insert(element)
