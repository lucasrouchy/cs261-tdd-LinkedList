# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# YOUR NAME

class BinarySearchTree:
   def __init__(self, key=None):
      self.key = key
      self.parent = None
      self.left = None
      self.right= None
   def insert(self, child):
      if child.key <= self.key:
         if self.left is None:
            self.left = child
            self.left.parent = self
      else:
         if self.right is None:
            self.right = child
            self.right.parent = self

