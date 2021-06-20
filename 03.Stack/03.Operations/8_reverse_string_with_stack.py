# Reverse a string using stack
# https://www.geeksforgeeks.org/stack-set-3-reverse-string-using-stack/

# Function to reverse a string
def reverse1(string):
    string = string[::-1]
    return string


# A stack based function to reverse a string
def reverse(string):
    n = len(string)

    # Create a empty stack
    stack = []

    # Push all characters of string to stack
    for i in range(0, n, 1):
        stack.append(string[i])

    # Making the string empty since all
    # characters are saved in stack
    string = ""

    # Pop all characters of string and
    # put them back to string
    for i in range(0, n, 1):
        string += stack.pop()

    return string


# Driver Code
if __name__ == "__main__":
    string = "GeeksQuiz"
    string = reverse(string)
    print(f"Reversed string is {string}")
