# Find postorder traversal of BST from preorder traversal
# https://www.geeksforgeeks.org/find-postorder-traversal-of-bst-from-preorder-traversal/


def get_postorder_bst(pre: list, n: int):
    pivot = 0

    # Run loop from 1 to length of pre
    for i in range(1, n):
        if pre[0] <= pre[i]:
            pivot = i
            break

    # Perform pivot length -1 to zero
    for i in range(pivot - 1, 0, -1):
        print(pre[i], end=" ")

    # Perform end to pivot length
    for i in range(n - 1, pivot - 1, -1):
        print(pre[i], end=" ")
    print(pre[0])


# Driver Code
if __name__ == "__main__":
    pre = [40, 30, 32, 35, 80, 90, 100, 120]
    n = len(pre)
    get_postorder_bst(pre, n)
