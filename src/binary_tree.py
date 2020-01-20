from dataclasses import dataclass
from .base import DynamicSet, UnderflowError

class Tree(DynamicSet):
	def __init__(self, arr=None, key=None, data=None, parent=None, left=None, right=None):
		self.size = 0
		self.data = data
		self.parent = parent
		self.left = left
		self.right = right
		self.key = key
		if arr: self.build_from_arr(arr)

	def __str__(self):
		return f'<Tree '\
			f"parent={getattr(self.parent, 'data', None)}, "\
			f'data={self.data}, '\
			f"left={getattr(self.left, 'data', None)}, "\
			f"right={getattr(self.right, 'data', None)}>"

	def build_from_arr(tree, arr):
		for item in arr:
			tree.insert(item)

	def height(tree):
		if tree is None:
			return 0
		else:
			return 1 + max(Tree.height(tree.left), Tree.height(tree.right))

	def root(node):
		while node.parent is not None:
			node = node.parent
		return node

	def inorder_walk(tree, node=False):
		if tree is None: return
		yield from Tree.inorder_walk(tree.left, node=node)
		yield tree if node else tree.data
		yield from Tree.inorder_walk(tree.right, node=node)

	def preorder_walk(tree, node=False):
		if tree is None: return
		yield tree if node else tree.data
		yield from Tree.preorder_walk(tree.left, node=node)
		yield from Tree.preorder_walk(tree.right, node=node)

	def postorder_walk(tree, node=False):
		if tree is None: return
		yield from Tree.postorder_walk(tree.left, node=node)
		yield from Tree.postorder_walk(tree.right, node=node)
		yield tree if node else tree.data

	def search(tree, key, node=False):
		while key != tree.key(tree.data):
			if tree is None: raise KeyError(f'Key {key} does not exist in BinaryTree.')
			if k < tree.key(tree.data):
				tree = tree.left
			else:
				tree = tree.right
		return tree if node else tree.data

	def min(tree, node=False):
		while tree.left is not None:
			tree = tree.left
		return tree if node else tree.data

	def max(tree, node=False):
		while tree.right is not None:
			tree = tree.right
		return tree if node else tree.data

	def successor(tree, node=False):
		if tree.right is not None:
			return Tree.min(tree.right, node=node)
		parent = tree.parent
		if parent is None: raise OverflowError('Trying to get successor of max.')
		while parent is not None and node is parent.right:
			node = parent
			parent = parent.parent
		return parent

	def predecessor(tree, node=False):
		if tree.left is not None:
			return Tree.max(tree.left, node=node)
		parent = tree.parent
		if parent is None: raise UnderflowError('Trying to get predecessor of min.')
		while parent is not None and tree is parent.left:
			node = parent
			parent = parent.parent
		return parent if node else parent.data

	def insert(T, z):
		z = Tree(key=T.key, data=z)
		y = None
		x = T.root()
		while x is not None and x.data is not None:
			y = x
			x = x.left if T.key(z.data) < T.key(x.data) else x.right
		z.parent = y
		if y is None:
			pass
		elif T.key(z) < T.key(y):
			y.left = z
		else:
			y.right = z
		T.size += 1

