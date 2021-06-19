# Delete array elements which are smaller than next or become smaller
# https://www.geeksforgeeks.org/delete-array-elements-which-are-smaller-than-next-or-become-smaller/


def delete_elements(arr, n, k):
    # create an empty stack
    st = []
    st.append(arr[0])

    # index to maintain top of the stack
    top = 0
    count = 0

    for i in range(1, n):
        # pop till the present element
        # is greater than stack's top element

        while len(st) != 0 and count < k and st[top] < arr[i]:
            st.pop()
            count += 1
            top -= 1

        st.append(arr[i])
        top += 1

    # print the remaining elements
    for i in range(0, len(st)):
        print(st[i], " ", end="")
    print()


# Driver code
k = 2
arr = [20, 10, 25, 30, 40]
delete_elements(arr, len(arr), k)
