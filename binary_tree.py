from dataclasses import dataclass

@dataclass
class Tree:
	data = None
	parent:'Tree' = None
	left:'Tree' = None
	right:'Tree' = None

	def inorder_tree_walk(self):
		if self is None: return
		yield from Tree.inorder_tree_walk(self.left)
		yield self.data
		yield from Tree.inorder_tree_walk(self.right)

	def search(self, key):
		pass
