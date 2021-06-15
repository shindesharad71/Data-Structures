# The Stock Span Problem
# https://www.geeksforgeeks.org/the-stock-span-problem/


def calculate_span(price, S):
    n = len(price)

    # Create a stack and push first element to it
    st = []
    st.append(0)

    # Span value of first element is always 1
    S[0] = 1

    # Calculate span value of rest of the elements
    for i in range(1, n):
        # Pop elements from stack while stack is not empty
        # Top of stack is smaller that price[i]
        while len(st) > 0 and price[st[-1]] <= price[i]:
            st.pop()

        # If stack becomes empty then price[i] is greater than all
        # elements left of it
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1])

        # Push this elements to stack
        st.append(i)


# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price) + 1)]

# Fill the span values in array S[]
calculate_span(price, S)

# Print the calculated span values
for i in range(0, len(price)):
    print(S[i], end=" ")
