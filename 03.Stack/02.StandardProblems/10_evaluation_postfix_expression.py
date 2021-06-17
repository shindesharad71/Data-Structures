# Evaluation of Postfix Expression
# https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/


def evaluate(expr):
    stack = []
    for i in expr:

        # if the component of the list is an integer
        try:
            stack.append(int(i))
        # if the component of the list is not an integer,
        # it must be an operator. Using ValueError, we can
        # evaluate components of the list other than type int
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()

            # switch statement to perform operation
            switcher = {
                "+": val2 + val1,
                "-": val2 - val1,
                "*": val2 * val1,
                "/": val2 / val1,
                "^": val2 ** val1,
            }
            stack.append(switcher.get(i))
    return int(stack.pop())


# Driver Program
str = "100 200 + 2 / 5 * 7 +"

# splitting the given string to obtain
# integers and operators into a list
expr = str.split(" ")
print(evaluate(expr))
