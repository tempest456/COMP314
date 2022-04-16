"""Binary Search TreeImplementaion."""


class Node:
    """Represents a node in the Binary Search Tree."""
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return f"Node({self.key}, {self.value}, {self.left}, {self.right})"


class BinarySearchTree:
    """Binary Search Tree class."""
    
    def __init__(self):
        self._size = 0
        self._root = None
    
    def size(self):
        """Returns the number of nodes in the tree."""
        return self._size
    
    def add(self, key, value):
        "Add a node to a BST."
        node = Node(key, value)
        prev = None
        current = self._root
        while current is not None:
            prev = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        if prev is None:
            self._root = node
        elif key < prev.key:
            prev.left = node
        else:
            prev.right = node
        self._size += 1
    
    def search(self, target):
        """Searchs the BST for the requested key and returns the corresponding value.
        Returns false if the key does not exist."""
        node = self._search(self._root, target)
        if node:
            return node.value
        return False
    
    def _search(self, root, key):
        """Helper function for search."""
        node = root
        while node is not None:
            if node.key == key:
                break
            if node.key > key:
                node = node.left
            else:
                node = node.right
        return node
    
    def smallest(self):
        """Returns a key-value tuple of the smallest node in the tree."""
        smallest_node = self._smallest(self._root)
        if smallest_node:
            return (smallest_node.key, smallest_node.value)
        return ()
    
    def _smallest(self, root):
        """Helper function for the smallest method."""
        if root:
            while root.left is not None:
                root = root.left
        return root
    
    def largest(self):
        """Returns a key-value tuple of the largest node in the tree."""
        largest_node = self._largest(self._root)
        if largest_node:
            return (largest_node.key, largest_node.value)
        return ()
    
    def _largest(self, root):
        """Helper function for the largest method."""
        if root:
            while root.right is not None:
                root = root.right
        return root
    
    def remove(self, key):
        """Deletes a key from a BST. Returns false if key does not exist."""
        if self._search(self._root, key):
            self._root = self._remove(self._root, key)
            self._size -= 1
            return True
        return False
    
    def _remove(self, root, key):
        """Helper function for remove."""
        if not root:
            return root
        if key < root.key:
            root.left = self._remove(root.left, key)
            return root
        if key > root.key:
            root.right = self._remove(root.right, key)
            return root
        if not root.left and not root.right:
            return None
        if not root.left or not root.right:
            return root.left if root.left else root.right
        successor = self._largest(root.left)
        root.key, root.value = successor.key, successor.value
        root.left = self._remove(root.left, successor.key)
        return root
    
    def inorder_walk(self):
        """Returns a list of keys visited in inorder way."""
        walk = []
        node = self._root
        def traverse(subtree, walk):
            if subtree is None:
                return
            traverse(subtree.left, walk)
            walk.append(subtree.key)
            traverse(subtree.right, walk)
        traverse(node, walk)
        return walk
    
    def preorder_walk(self):
        """Returns a list of keys visited in preorder way."""
        walk = []
        node = self._root
        def traverse(subtree, walk):
            if subtree is None:
                return
            walk.append(subtree.key)
            traverse(subtree.left, walk)
            traverse(subtree.right, walk)
        traverse(node, walk)
        return walk
    
    def postorder_walk(self):
        """Returns a list of keys visited in postorder way."""
        walk = []
        node = self._root
        def traverse(subtree, walk):
            if subtree is None:
                return
            traverse(subtree.left, walk)
            traverse(subtree.right, walk)
            walk.append(subtree.key)
        traverse(node, walk)
        return walk
    