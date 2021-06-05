# Function to check if a singly linked list is palindrome
# https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/


def is_palindrome(self):
    stack = []
    temp = self.head
    is_list_palindrome = False

    while temp:
        stack.append(temp.data)
        temp = temp.next

    temp = self.head
    while temp:
        el = stack.pop

        if el == temp.data:
            is_list_palindrome = True
        else:
            is_list_palindrome = False
            break

    return is_list_palindrome
