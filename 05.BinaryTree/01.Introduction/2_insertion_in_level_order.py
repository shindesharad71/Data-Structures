# Insertion in a Binary Tree in level order
# https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# Inorder traverse of binary tree
def inorder(temp):
    if not temp:
        return

    inorder(temp.left)
    print(temp.value, end=" ")
    inorder(temp.right)


# Function to insert element in binary tree
def insert(temp, key):
    if not temp:
        root = Node(key)
        return

    q = []
    q.append(temp)

    # Do level order traversal until we find an empty place.
    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
        else:
            q.append(temp.right)


# Driver code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    insert(root, key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)
    print()
