class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.value == data:
            return False
        elif


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)