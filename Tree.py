class BinaryTree:
    def _init_(self, root):
        # Initialize the BinaryTree with a root value, and set left and right children to None.
        self.key = root
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, new_node):
        # Insert a new node as the left child.
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right(self, new_node):
        # Insert a new node as the right child.
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
            
    def get_right_child(self):
        # Get the right child.
        return self.right_child
    
    def get_left_child(self):
        # Get the left child.
        return self.left_child
    
    def set_root_val(self, obj):
        # Set the root value.
        self.key = obj
        
    def get_root_val(self):
        # Get the root value.
        return self.key

    # Implement traversal:
    def preorder(self):       
        # Preorder traversal: Root, Left, Right.
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
            
    def inorder(self):
        # Inorder traversal: Left, Root, Right.
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()
    
    def postorder(self):
        # Postorder traversal: Left, Right, Root.
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)

# Test your BinaryTree class:
root = BinaryTree('a')
print("root value:", root.get_root_val())
print("left child:", root.get_left_child())
root.insert_left('b')
print("left child:", root.get_left_child().get_root_val())  # Corrected line
print("root of left subtree:", root.get_left_child().get_root_val())
root.insert_right('c')
print("right child:", root.get_right_child().get_root_val())  # Corrected line
print("root of right subtree:", root.get_right_child().get_root_val())
root.get_right_child().set_root_val("hello")
print("root of right subtree:", root.get_right_child().get_root_val())