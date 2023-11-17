class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def inorder_traversal(self):
        self.inorder(self.root)


# Example usage:
bst = BST()
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    bst.insert_key(key)

print("Inorder Traversal:")
bst.inorder_traversal()
