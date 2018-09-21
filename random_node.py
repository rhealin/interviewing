import random

class Node():
	def __init__(self):
		self.value = None
		self.left = None
		self.right = None
		self.num_left_children = None
		self.num_right_children = None

def random_node(root):
	denominator = root.num_left_children + root.num_right_children + 1
	random_number = random.randint(denominator)

	if random_number <= root.num_left_children:
		return random_node(root.left)
	elif random_number == root.num_left_children + 1:
		return root
	else:
		return random_node(root.right)	