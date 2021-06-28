# Evaluation of Expression Tree
# https://www.geeksforgeeks.org/evaluation-of-expression-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def evaluate_expression_tree(root: Node) -> int:
    # empty tree
    if root is None:
        return 0

    # leaf node
    if root.left is None and root.right is None:
        return int(root.data)

    # evaluate left tree
    left_sum = evaluate_expression_tree(root.left)

    # evaluate right tree
    right_sum = evaluate_expression_tree(root.right)

    # check which operation to apply
    if root.data == "+":
        return left_sum + right_sum

    elif root.data == "-":
        return left_sum - right_sum

    elif root.data == "*":
        return left_sum * right_sum

    else:
        return left_sum / right_sum


# Driver function to test above problem
if __name__ == "__main__":
    # creating a sample tree
    root = Node("+")
    root.left = Node("*")
    root.left.left = Node("5")
    root.left.right = Node("4")
    root.right = Node("-")
    root.right.left = Node("100")
    root.right.right = Node("20")
    print(evaluate_expression_tree(root))

    root = None

    # creating a sample tree
    root = Node("+")
    root.left = Node("*")
    root.left.left = Node("5")
    root.left.right = Node("4")
    root.right = Node("-")
    root.right.left = Node("100")
    root.right.right = Node("/")
    root.right.right.left = Node("20")
    root.right.right.right = Node("2")
    print(evaluate_expression_tree(root))
