# K’th smallest element in BST using O(1) Extra Space
# https://www.geeksforgeeks.org/kth-smallest-element-in-bst-using-o1-extra-space/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def kth_smallest(root: Node, k: int):
    # Count to iterate over elements
    # till we get the kth smallest number
    count = 0
    k_small = -999999999

    current = root

    while current:
        # Like Morris traversal if current does
        # not have left child rather than
        # printing as we did in inorder, we
        # will just increment the count as the
        # number will be in an increasing order
        if current.left is None:
            count += 1

            # if count is equal to K then we
            # found the kth smallest, so store
            # it in ksmall
            if count == k:
                k_small = current.data

            # go to current's right child
            current = current.right

        else:
            # we create links to Inorder Successor
            # and count using these links
            pre = current.left
            while pre.right is not None and pre.right is not current:
                pre = pre.right

            # building links
            if pre.right is None:

                # link made to Inorder Successor
                pre.right = current
                current = current.left

            # While breaking the links in so made
            # temporary threaded tree we will check
            # for the K smallest condition
            else:
                # Revert the changes made in if part
                # (break link from the Inorder Successor)
                pre.right = None
                count += 1

                # If count is equal to K then we
                # found the kth smallest and so
                # store it in ksmall
                if count == k:
                    k_small = current.data

                current = current.right

    return k_small


def insert(root: Node, data: int):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Driver Code
if __name__ == "__main__":

    # Let us create following BST
    #         50
    #       /    \
    #      30    70
    #    /  \  /  \
    #   20 40 60 80
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    for k in range(1, 8):
        print(kth_smallest(root, k), end=" ")
