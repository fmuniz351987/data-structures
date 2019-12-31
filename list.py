from base import Node, Iterator, UnderflowError, DynamicSet


class List(DynamicSet):
	def search(self, position):
		for i, data in enumerate(self):
			if i == position:
				return data
		else:
			return None

	def swap(self, i, j):
		if i == j: return
		if i > j: i, j = j, i
		if i == 0: first = self.sentinel
		k = 0
		for node in self._nodes():
			if k == i - 1:
				first = node
			elif k == j - 1:
				last = node
			k += 1
		node_i = first.delete_after()
		node_j = last.delete_after()
		first.insert_after(node_j)
		last.insert_after(node_i)

	def insert(self, data, position=None):
		if position is None: position = len(self)
		if position > len(self) or position < 0:
			raise IndexError('Invalid position to insert on a list.')
		new_node = Node(data)
		node = self.sentinel
		for i in range(position):
			node = node.next
		node.insert_after(new_node)
		self.size += 1

	def delete(self, position):
		if position < 0 or position >= len(self):
			raise IndexError('Invalid position to delete element from list.')
		node = self.sentinel
		for i in range(position):
			node = node.next
		removed_node = node.delete_after()
		self.size -= 1
		return removed_node.data

	def build_from_arr(self, arr):
		for element in arr:
			self.insert(element)
