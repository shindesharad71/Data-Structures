# Leaf nodes from Preorder of a Binary Search Tree
# https://www.geeksforgeeks.org/leaf-nodes-preorder-binary-search-tree/


def leaf_nodes(preorder: list, n: int):
    s = []
    i = 0

    for j in range(1, n):
        found = False

        if preorder[i] > preorder[j]:
            s.append(preorder[i])

        else:
            while len(s) != 0:
                if preorder[j] > s[-1]:
                    s.pop(-1)
                    found = True
                else:
                    break

        if found:
            print(preorder[i], end=" ")
        i += 1

    # Since rightmost element is
    # always leaf node.
    print(preorder[n - 1])


# Driver code
if __name__ == "__main__":
    preorder = [890, 325, 290, 530, 965]
    n = len(preorder)

    leaf_nodes(preorder, n)
