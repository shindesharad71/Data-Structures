# Construct BST from given preorder traversal
# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversal-set-2/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# The main function that constructs BST from pre[]
def construct_tree(pre: list, size: int):
    # The first element of pre[] is always root
    root = Node(pre[0])

    s = []

    # append root
    s.append(root)

    i = 1

    # Iterate through rest of the size-1
    # items of given preorder array
    while i < size:
        temp = None

        # Keep on popping while the next value
        # is greater than stack's top value.
        while len(s) > 0 and pre[i] > s[-1].data:
            temp = s.pop()

        # Make this greater value as the right child
        # and append it to the stack
        if temp is not None:
            temp.right = Node(pre[i])
            s.append(temp.right)

        # If the next value is less than the stack's top
        # value, make this value as the left child of the
        # stack's top node. append the new node to stack
        else:
            temp = s[-1]
            temp.left = Node(pre[i])
            s.append(temp.left)
        i = i + 1

    return root


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Driver Code
if __name__ == "__main__":
    pre = [10, 5, 1, 7, 40, 50]
    size = len(pre)
    root = construct_tree(pre, size)
    print("Inorder traversal of the constructed tree is ")
    inorder(root)
