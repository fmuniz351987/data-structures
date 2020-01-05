from base import DynamicSet
from list import List


class Hash(DynamicSet):
	def __init__(self, slots, key=None):
		self.slots = slots
		self.data = []
		for i in range(slots):
			self.data.append(List(key=key))
		self.key = key
		self.size = 0

	def __iter__(self):
		for i in range(self.slots):
			for element in self.data[i]:
				yield element

	def _nodes(self):
		raise AttributeError('Hash has no _nodes attribute.')

	def _mod_hash(self, value):
		return value % self.slots

	def _index(self, key):
		out = hash(key)
		return self._mod_hash(out)

	def insert(self, value):
		index = self._index(self.key(value))
		self.data[index].insert(value)
		self.size += 1

	def search(self, key):
		index = self._index(key)
		return self.data[index].search(key)

	def delete(self, key):
		index = self._index(key)
		out = self.data[index].delete(key)
		self.size -= 1
		return out
