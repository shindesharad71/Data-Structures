# Prefix to Postfix Conversion
# https://www.geeksforgeeks.org/prefix-postfix-conversion/


def prefix_to_postfix(s):

    # Stack to store the operands
    stack = []

    operators = set(["+", "-", "*", "/", "^"])

    # Reversing the order
    s = s[::-1]

    # iterating through individual tokens
    for i in s:
        if i in operators:
            # pop two elements from stack
            a = stack.pop()
            b = stack.pop()

            # concatenate them as operand1 + operand2 + operator
            temp = a + b + i
            stack.append(temp)
        else:
            # its operand
            stack.append(i)

    # Printing final output
    print(*stack)


if __name__ == "__main__":
    s = "*-A/BC-/AKL"
    prefix_to_postfix(s)
