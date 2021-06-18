# Delete middle element of a stack
# https://www.geeksforgeeks.org/delete-middle-element-stack/


def delete_middle_element(stack, n, current):
    # If stack is empty or all items are traversed
    if len(stack) == 0 or current == n:
        return

    # Remove the current item
    x = stack[-1]
    stack.pop()

    # Remove other items
    delete_middle_element(stack, n, current + 1)

    # Put all items back except middle
    if current != int(n / 2):
        stack.append(x)


# Driver Code
if __name__ == "__main__":
    st = []
    st.append("1")
    st.append("2")
    st.append("3")
    st.append("4")
    st.append("5")
    st.append("6")
    st.append("7")

    delete_middle_element(st, len(st), 0)

    for i in st[::-1]:
        print(str(i) + " ", end="")
    print()
