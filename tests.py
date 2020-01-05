import unittest
from dataclasses import dataclass

import random
from unittest import TestCase

from src import sort, Stack, Queue, List, Hash


class SortTest(TestCase):
	def setUp(self):
		self.subject = list(range(15))
		random.shuffle(self.subject)

	def assert_sorted(self, arr, **kwargs):
		self.assertEqual(arr, sorted(arr, **kwargs))

	def test_insertion_sort(self):
		sort.insertion_sort(self.subject)
		self.assert_sorted(self.subject)

	def test_merge(self):
		# tests if merge properly orders an array whose sides are individually ordered
		arr = [1, 3, 4, 6, 9, 2, 5, 7, 8]
		n = len(arr)
		sort.merge(arr, 0, n // 2, n)
		self.assert_sorted(arr)

	def test_mergesort(self):
		sort.mergesort(self.subject)
		self.assert_sorted(self.subject)

	def test_heapsort(self):
		sort.heapsort(self.subject)
		self.assert_sorted(self.subject)

	def test_heapsort_reverse(self):
		sort.heapsort_reverse(self.subject)
		self.assert_sorted(self.subject, reverse=True)

	def assert_partition(self, arr, pivot):
		n = len(arr)
		for i in range(pivot):
			self.assertLessEqual(arr[i], pivot)
		for i in range(pivot + 1, n):
			self.assertGreater(arr[i], pivot)

	def test_partition(self):
		piv = sort.partition(self.subject)
		self.assert_partition(self.subject, piv)

	def test_randomized_partition(self):
		piv = sort.randomized_partition(self.subject)
		self.assert_partition(self.subject, piv)

	def test_hoare_partition(self):
		piv = sort.hoare_partition(self.subject)
		self.assert_partition(self.subject, piv)

	def test_quicksort(self):
		sort.quicksort(self.subject)
		self.assert_sorted(self.subject)

	def test_quicksort_random(self):
		sort.quicksort_random(self.subject)
		self.assert_sorted(self.subject)

	def _test_quicksort_hoare(self):
		# TODO - fix quicksort hoare not working
		print(self.subject)
		sort.quicksort_hoare(self.subject)
		self.assert_sorted(self.subject)

	def test_randomized_select(self):
		ith_order_stats = []
		for i in range(len(self.subject)):
			ith_order_stats.append(sort.randomized_select(self.subject, i + 1))
		self.assertEqual(ith_order_stats, sorted(self.subject))

class StackTest(TestCase):
	def setUp(self):
		self.subject = Stack(arr=list(range(6)))
		# self.subject.build_from_arr(list(range(6)))

	def test_length(self):
		self.assertEqual(len(self.subject), 6)

	def test_pop(self):
		x = self.subject.pop()
		self.assertEqual(x, 0)

	def test_peek_does_not_change_length(self):
		self.subject.peek()
		self.assertEqual(len(self.subject), 6)

	def test_push(self):
		self.subject.push(6)
		self.assertEqual(self.subject.peek(), 6)

	def test_empty(self):
		for i in range(len(self.subject)):
			self.subject.pop()
		self.assertTrue(self.subject.empty())


class QueueTest(TestCase):
	def setUp(self):
		self.subject = Queue(list(range(6)))

	def test_peek(self):
		self.assertEqual(self.subject.peek(), 0)

	def test_length(self):
		self.assertEqual(len(self.subject), 6)

	def test_dequeue(self):
		x = self.subject.dequeue()
		self.assertEqual(x, 0)
		self.assertEqual(len(self.subject), 5)

	def test_empty(self):
		for i in range(len(self.subject)):
			self.subject.dequeue()
		self.assertTrue(self.subject.empty())


class SimpleListTest(TestCase):
	def setUp(self):
		self.subject = List(arr=list(range(6)))

	def test_len(self):
		self.assertEqual(len(self.subject), 6)

	def test_search(self):
		for i in range(6):
			self.assertEqual(self.subject.search(i), i)

	def test_delete(self):
		x = self.subject.delete(3)
		self.assertEqual(x, 3)

	def test_getitem(self):
		for i in range(6):
			self.assertEqual(self.subject[i], 5 - i)

	def test_setitem(self):
		self.subject[2] = 10
		self.assertEqual(self.subject[2], 10)

@dataclass
class Data:
	name:str
	age:int

class KeyListTest(TestCase):
	def setUp(self):
		self.subject = List(key='name')
		for i in range(10):
			data = Data(name=f'Person#{i}', age= i * 10)
			self.subject.insert(data)

	def test_delete(self):
		data = self.subject.delete(f'Person#5')
		self.assertEqual(len(self.subject), 9)
		self.assertEqual(data.age, 50)

	def test_search(self):
		data = self.subject.search(f'Person#1')
		self.assertEqual(data.age, 10)


class HashTest(TestCase):
	def setUp(self):
		self.subject = Hash(slots=5, key='name')
		for i in range(10):
			data = Data(name=f'Person#{i}', age= i * 10)
			self.subject.insert(data)

	def test_search(self):
		person = self.subject.search('Person#4')
		self.assertEqual(person.age, 40)

	def test_delete(self):
		person = self.subject.delete('Person#3')
		self.assertEqual(len(self.subject), 9)
		self.assertEqual(person.age, 30)
		self.assertEqual(self.subject.search(person.name), None)


if __name__ == '__main__':
	unittest.main()
