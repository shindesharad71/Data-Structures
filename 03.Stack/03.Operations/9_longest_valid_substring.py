# Length of the longest valid substring
# https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/


def find_max_length(string):
    n = len(string)

    stack = []
    stack.append(-1)

    result = 0

    for i in range(n):
        # If opening bracket, push index of it
        if string[i] == "(":
            stack.append(i)

        else:
            # Pop the previous opening bracket's index
            if len(stack) != 0:
                stack.pop()

            # Check if this length formed with base of
            # current valid substring is more than max
            # so far
            if len(stack) != 0:
                result = max(result, i - stack[len(stack) - 1])

            # If stack is empty. push current index as
            # base for next valid substring (if any)
            else:
                stack.append(i)

    return result


# Driver code
string = "((()()"

# Function call
print(find_max_length(string))

string = "()(()))))"

# Function call
print(find_max_length(string))
