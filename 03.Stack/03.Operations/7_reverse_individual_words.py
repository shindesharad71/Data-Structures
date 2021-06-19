# Reverse individual words
# https://www.geeksforgeeks.org/reverse-individual-words/


# Python3 program to reverse individual words
# in a given string using STL list

# reverses individual words of a string
def reverse_words(string):
    st = list()

    # Traverse given string and push all characters
    # to stack until we see a space.
    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])

        # When we see a space, we print
        # contents of stack.
        else:
            while len(st) > 0:
                print(st[-1], end="")
                st.pop()
            print(end=" ")

    # Since there may not be space after
    # last word.
    while len(st) > 0:
        print(st[-1], end="")
        st.pop()
    print()


# Driver Code
if __name__ == "__main__":
    string = "Geeks for Geeks"
    reverse_words(string)
