# Prefix to Infix Conversion
# https://www.geeksforgeeks.org/prefix-infix-conversion/


def prefix_to_infix(prefix):
    stack = []

    i = len(prefix) - 1

    # read prefix in reverse order
    while i >= 0:
        if not is_operator(prefix[i]):
            # symbol is operand
            stack.append(prefix[i])
        else:
            # symbol is operator
            str = f"({stack.pop()}{prefix[i]}{stack.pop()})"
            stack.append(str)
        i -= 1

    return stack.pop()


def is_operator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    return False


# Driver code
if __name__ == "__main__":
    str = "*-A/BC-/AKL"
    print(prefix_to_infix(str))
