from .base import swap

class Heap:
	@staticmethod
	def parent(i):
		return i // 2

	@staticmethod
	def left(i):
		return 2 * i

	@staticmethod
	def right(i):
		return 2 * i + 1

	def max_heapify(self, i=0, cap=None):
		if cap is None: cap = len(self)
		l = Heap.left(i)
		r = Heap.right(i)
		max = l if l < cap and self[l] > self[i] else i
		if r < cap and self[r] > self[max]: max = r
		if max != i:
			swap(self, max, i)
			Heap.max_heapify(self, max, cap)

	def build_max_heap(self):
		n = len(self)
		for i in range(n // 2 + 1):
			Heap.max_heapify(self, n // 2 - i)

	def min_heapify(self, i=0, cap=None):
		if cap is None: cap = len(self)
		l = Heap.left(i)
		r = Heap.right(i)
		min = l if l < cap and self[l] < self[i] else i
		if r < cap and self[r] < self[min]: min = r
		if min != i:
			swap(self, i, min)
			Heap.min_heapify(self, min, cap)

	def build_min_heap(self):
		n = len(self)
		for i in range(n // 2 + 1):
			Heap.min_heapify(self, n // 2 - i)
