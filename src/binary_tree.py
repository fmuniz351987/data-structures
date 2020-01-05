from dataclasses import dataclass

@dataclass
class Tree:
	data = None
	parent:'Tree' = None
	left:'Tree' = None
	right:'Tree' = None

	def inorder_walk(self):
		if self is None: return
		yield from Tree.inorder_walk(self.left)
		yield self.data
		yield from Tree.inorder_walk(self.right)

	def preorder_walk(self):
		if self is None: return
		yield self.data
		yield from Tree.preorder_walk(self.left)
		yield from Tree.preorder_walk(self.right)

	def postorder_walk(self):
		if self is None: return
		yield from Tree.postorder_walk(self.left)
		yield from Tree.postorder_walk(self.right)
		yield self.data

	def search(self, key):
		pass
