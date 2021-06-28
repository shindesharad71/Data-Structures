# Expression Tree
# https://www.geeksforgeeks.org/expression-tree/

# Create a tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# A utility function to check if 'char' is an operator
def is_operator(char: str) -> bool:
    if char == "+" or char == "-" or char == "*" or char == "/" or char == "^":
        return True
    return False


# A utility function to do inorder traversal
def inorder(t: Node):
    if t is not None:
        inorder(t.left)
        print(t.data, end=" ")
        inorder(t.right)


# Returns root of constructed tree for given postfix expression
def construct_tree(postfix: str) -> str:
    stack = []

    # Traverse through every character of input expression
    for char in postfix:
        # if operand, simply push into stack
        t = Node(char)
        if not is_operator(char):
            stack.append(t)
        # Operator
        else:
            # Pop two top nodes
            t1 = stack.pop()
            t2 = stack.pop()

            t.right = t1
            t.left = t2

            stack.append(t)

    t = stack.pop()
    return t


# Driver Program
if __name__ == "__main__":
    postfix = "ab+ef*g*-"
    r = construct_tree(postfix)
    print("Infix expression is")
    inorder(r)
