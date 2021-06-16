# Next Greater Element
# https://www.geeksforgeeks.org/next-greater-element/

# Python program to print next greater element using stack

# Stack Functions to be used by printNGE()


def isEmpty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()


"""prints element and NGE pair for all elements of
arr[] """


def printNGE(arr):
    stack = []
    element = 0
    next = 0

    # push the first element to stack
    # push(stack, arr[0])
    stack.append(arr[0])

    # iterate for rest of the elements
    for i in range(1, len(arr), 1):
        next = arr[i]

        if len(stack) != 0:

            # if stack is not empty, then pop an element from stack
            element = pop(stack)

            """If the popped element is smaller than next, then
				a) print the pair
				b) keep popping while elements are smaller and
				stack is not empty """
            while element < next:
                print(str(element) + " -- " + str(next))
                if isEmpty(stack) == True:
                    break
                element = pop(stack)

            """If element is greater than next, then push
			the element back """
            if element > next:
                stack.append(element)

        """push next to stack so that we can find
		next greater for it """
        stack.append(next)

    """After iterating over the loop, the remaining
	elements in stack do not have the next greater
	element, so print -1 for them """

    while len(stack) != 0:
        element = stack.pop()
        next = -1
        print(str(element) + " -- " + str(next))


# Driver code
arr = [11, 13, 21, 3]
printNGE(arr)
