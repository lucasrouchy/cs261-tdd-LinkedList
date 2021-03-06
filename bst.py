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
            return
         else:
               return self.left.insert(child)
      if child.key > self.key:
         if self.right is None:
            self.right = child
            self.right.parent = self
            return
         else:
            return self.right.insert(child)
   def search(self, key):
      if key is self.key:
         return self
      elif key < self.key:
         if self.left == None:
            return None
         else:
               return self.left.search(key)
      else:
            if self.right == None:
               return None
            else: 
               return self.right.search(key)
   def delete(self, target_node):
      if target_node != self.key:
         return self
      if target_node.left != None and target_node.right != None:
         if target_node.value < target_node.parent.value:
            target_node.parent.left = None
         else:
            target_node.parent.right = None
         
            




