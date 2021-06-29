# Print Postorder traversal from given Inorder and Preorder traversals
# https://www.geeksforgeeks.org/print-postorder-from-given-inorder-and-preorder-traversals/

# A utility function to search x in
# arr[] of size n
def search(arr: list, x: int, n: int) -> int:
    for i in range(n):
        if arr[i] == x:
            return i

    return -1


# Prints postorder traversal from
# given inorder and preorder traversals
def print_postorder(inorder: list, preorder: list, n: int):
    # The first element in pre[] is always
    # root, search it in in[] to find left
    # and right subtrees
    root = search(inorder, preorder[0], n)

    # If left subtree is not empty,
    # print left subtree
    if root != 0:
        print_postorder(inorder, preorder[1:n], root)

    # If right subtree is not empty,
    # print right subtree
    if root != n - 1:
        print_postorder(inorder[root + 1 : n], preorder[root + 1 : n], n - root - 1)

    print(preorder[0], end=" ")


# Driver Code
if __name__ == "__main__":
    inorder = [4, 2, 5, 1, 3, 6]
    preorder = [1, 2, 4, 5, 3, 6]
    n = len(inorder)

    print("Postorder Traversal")
    print_postorder(inorder, preorder, n)
