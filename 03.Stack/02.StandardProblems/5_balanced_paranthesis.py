# Check for Balanced Brackets in an expression (well-formedness) using Stack
# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/


def check_balanced_paranthesis(expr):
    stack = []

    opening_paranthesis = ("(", "[", "{")

    for char in expr:
        if char in opening_paranthesis:
            # Push the element in the stack
            stack.append(char)
        else:
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False

            current_char = stack.pop()

            if current_char == "(":
                if char != ")":
                    return False

            if current_char == "[":
                if char != "]":
                    return False

            if current_char == "{":
                if char != "}":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"

    # Function call
    if check_balanced_paranthesis(expr):
        print("Balanced")
    else:
        print("Not Balanced")
