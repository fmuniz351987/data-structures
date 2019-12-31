class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return f'<Node data={self.data}>'

	def insert_after(self, node):
		node.next = self.next
		self.next = node

	def delete_after(self):
		deleted = self.next
		self.next = deleted.next
		return deleted


class Iterator:
	def __init__(self, node, stop_value=None, use_nodes=False):
		self.current_node = node
		self.stop_value = stop_value
		self.use_nodes = use_nodes

	def __iter__(self):
		return self

	def __next__(self):
		self.current_node = self.current_node.next
		if self.current_node is self.stop_value:
			raise StopIteration
		if self.use_nodes:
			return self.current_node
		else:
			return self.current_node.data


class DynamicSet:
	def __init__(self, arr=None, key=None):
		self.size = 0
		self.sentinel = Node()
		self.sentinel.next = self.sentinel
		self.key = key
		if arr: self.build_from_arr(arr)

	@property
	def key(self):
		return self._key

	@key.setter
	def key(self, value):
		if type(value) is str:
			self._key = lambda x: getattr(x, value)
		elif callable(value):
			self._key = value
		elif value is None:
			self._key = lambda x: x
		else:
			raise NotImplementedError('Key must be str, callabe or None.')

	def _nodes(self):
		return Iterator(self.sentinel, stop_value=self.sentinel, use_nodes=True)

	def __iter__(self):
		return Iterator(self.sentinel, stop_value=self.sentinel)

	def __len__(self):
		return self.size

	def __str__(self):
		stem = ', '.join([str(data) for data in self])
		return f'<{type(self).__name__} [{stem}]>'

	def __repr__(self):
		return self.__str__()

	def empty(self):
		return self.size == 0

	def build_from_arr(self):
		raise NotImplementedError


class UnderflowError(ArithmeticError):
	pass


def swap(arr, i, j):
	aux = arr[i]
	arr[i] = arr[j]
	arr[j] = aux

