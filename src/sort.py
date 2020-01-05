from math import inf
from random import randint

from .base import swap
from .stack import Stack
from .heap import Heap

def insertion_sort(arr):
	for j in range(len(arr)):
		key = arr[j]
		# insert arr[j] into the ordered sequence arr[0:j]
		i = j - 1
		while i >= 0 and arr[i] > key:
			arr[i+1] = arr[i]
			i -= 1
		arr[i+1] = key

def merge(arr, low, split, high):
	left = Stack(arr[low : split + 1] + [inf])
	right = Stack(arr[split + 1 : high] + [inf])
	for i in range(low, high):
		if left.peek() < right.peek():
			arr[i] = left.pop()
		else:
			arr[i] = right.pop()

def mergesort(arr, low=0, high=None):
	if high is None: high = len(arr)
	if high - low > 1:
		split = (low + high - 1) // 2
		mergesort(arr, low, split + 1)
		mergesort(arr, split + 1, high)
		merge(arr, low, split, high)

def heapsort(arr):
	Heap.build_max_heap(arr)
	N = len(arr)
	for i in range(1, N):
		swap(arr, 0, N - i)
		Heap.max_heapify(arr, 0, N - i)

def heapsort_reverse(arr):
	Heap.build_min_heap(arr)
	N = len(arr)
	for i in range(1, N):
		swap(arr, 0, N - i)
		Heap.min_heapify(arr, 0, N - i)

def partition(arr, low=0, high=None):
	if high is None: high = len(arr) - 1
	piv = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] <= piv:
			i += 1
			swap(arr, i, j)
	swap(arr, i+1, high)
	return i + 1

def randomized_partition(arr, low=0, high=None):
	if high is None: high = len(arr) - 1
	piv = randint(low, high)
	swap(arr, piv, high)
	return partition(arr, low, high)

def hoare_partition(arr, low=0, high=None):
	if high is None: high = len(arr) - 1
	piv = arr[high]
	i, j = low, high
	while True:
		while arr[j] > piv: j -= 1
		while arr[i] < piv: i += 1
		if i < j:
			swap(arr, i, j)
			j -= 1; i += 1
		else:
			return j

def quicksort(arr, low=0, high=None):
	if high is None: high = len(arr) - 1
	if low < high:
		piv = partition(arr, low, high)
		quicksort(arr, low, piv - 1)
		quicksort(arr, piv + 1, high)

def quicksort_random(arr, low=0, high=None):
	if high is None: high = len(arr) - 1
	if low < high:
		piv = randomized_partition(arr, low, high)
		quicksort_random(arr, low, piv - 1)
		quicksort_random(arr, piv + 1, high)

def quicksort_hoare(arr, low=0, high=None):
	if high is None: high = len(arr) - 1
	if low < high:
		piv = hoare_partition(arr, low, high)
		quicksort_hoare(arr, low, piv - 1)
		quicksort_hoare(arr, piv + 1, high)

def randomized_select(arr, i, low=0, high=None):
	if high is None: high = len(arr) - 1
	if low == high: return arr[low]
	piv = randomized_partition(arr, low, high)
	k = piv - low + 1
	if i == k:
		return arr[piv]
	elif i < k:
		return randomized_select(arr, i, low, piv - 1)
	else:
		return randomized_select(arr, i - k, piv + 1, high)

