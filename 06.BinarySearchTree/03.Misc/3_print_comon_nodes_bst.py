# Print Common Nodes in Two Binary Search Trees
# https://www.geeksforgeeks.org/print-common-nodes-in-two-binary-search-trees/


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = self.right = None


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def insert(root: Node, data: int):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def print_common(root1: Node, root2: Node):
    # Create two stacks for two inorder
    # traversals
    s1 = []
    s2 = []

    while 1:

        # append the Nodes of first
        # tree in stack s1
        if root1:
            s1.append(root1)
            root1 = root1.left

        # append the Nodes of second tree
        # in stack s2
        elif root2:
            s2.append(root2)
            root2 = root2.left

        # Both root1 and root2 are NULL here
        elif len(s1) != 0 and len(s2) != 0:
            root1 = s1[-1]
            root2 = s2[-1]

            # If current keys in two trees are same
            if root1.data == root2.data:
                print(root1.data, end=" ")
                s1.pop(-1)
                s2.pop(-1)

                # move to the inorder successor
                root1 = root1.right
                root2 = root2.right

            elif root1.data < root2.data:

                # If Node of first tree is smaller, than
                # that of second tree, then its obvious
                # that the inorder successors of current
                # Node can have same value as that of the
                # second tree Node. Thus, we pop from s2
                s1.pop(-1)
                root1 = root1.right

                # root2 is set to NULL, because we need
                # new Nodes of tree 1
                root2 = None
            elif root1.data > root2.data:
                s2.pop(-1)
                root2 = root2.right
                root1 = None

        # Both roots and both stacks are empty
        else:
            break


# Driver Code
if __name__ == "__main__":
    # Create first tree as shown in example
    root1 = None
    root1 = insert(root1, 5)
    root1 = insert(root1, 1)
    root1 = insert(root1, 10)
    root1 = insert(root1, 0)
    root1 = insert(root1, 4)
    root1 = insert(root1, 7)
    root1 = insert(root1, 9)

    # Create second tree as shown in example
    root2 = None
    root2 = insert(root2, 10)
    root2 = insert(root2, 7)
    root2 = insert(root2, 20)
    root2 = insert(root2, 4)
    root2 = insert(root2, 9)

    print("Tree 1 : ")
    inorder(root1)
    print()

    print("Tree 2 : ")
    inorder(root2)
    print()

    print("Common Nodes: ")
    print_common(root1, root2)
