from bst_node import Node

def getInorder(root):
    if root == None:
        return ""
    return getInorder(root.left) + (str(root.val) + "-") + getInorder(root.right)

def getPostorder(root):
    if root == None:
        return ""
    return getPostorder(root.left) + getPostorder(root.right) + (str(root.val) + "-")

def getPreorder(root):
    if root == None:
        return ""
    return (str(root.val) + "-") + getPreorder(root.left) + getPreorder(root.right)

def insert(root, key):
    if root == None:
        root = Node(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    else: #key > root.val
        root.right = insert(root.right, key)
    #print(getInorder(root))
    return root

def isBST(root):
    if root == None:
        return True
    if root.left != None:
        if root.left.val >= root.val:
            return False
    if root.right != None:
        if root.right.val <= root.val:
            return False
    return isBST(root.left) and isBST(root.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(9)

    print("Preorder traversal of binary tree is")
    print(getPreorder(root))

    print("\nInorder traversal of binary tree is")
    print(getInorder(root))

    print("\nPostorder traversal of binary tree is")
    print(getPostorder(root))

    root = insert(root, 8)
    print("\nInorder traversal of binary tree with 8 inserted is")
    print(getInorder(root))

    print(isBST(root))