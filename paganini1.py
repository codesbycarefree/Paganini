# Python program to insert a node
# in a BST

# Given Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Function to insert a new node with
# given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # Return the node pointer
    return node


# Function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Driver Code
if __name__ == '__main__':
    """
    Let us create following BST
        50
    /	 \
    30	 70
    / \ / \
    20 40 60 80
    """
    root = None

    # Inserting value 50
    root = insert(root, 50)

    # Inserting value 30
    insert(root, 30)

    # Inserting value 20
    insert(root, 20)

    # Inserting value 40
    insert(root, 40)

    # Inserting value 70
    insert(root, 70)

    # Inserting value 60
    insert(root, 60)

    # Inserting value 80
    insert(root, 80)

    # Print the BST
    inorder(root)



class Node():
    def __init__(self,key):
        self.key=key
        self.left = None
        self.right = None

def insert(node,key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left=insert(node.left,key)
    elif key > node.key:
        node.right = insert(node.right,key)

    return node

def search(root , key):
    if root is None or root.key == key:
        return root

    if root.key<key:
        return search(root.right,key)

    if root.key>key:
        return search(root.left,key)


if __name__=="__main__":
    root = None
    root = insert(root,30)
    insert(root,30)
    insert(root,20)
    insert(root,40)
    insert(root,70)
    insert(root,60)
    insert(root,80)

    key =6

    if search(root,key) is None:
        print(key, "not found")
    else:
        print(key, "found")

    key  = 60

    if search(root,key) is None:
        print(key , "not found")
    else:
        print(key,"found")


