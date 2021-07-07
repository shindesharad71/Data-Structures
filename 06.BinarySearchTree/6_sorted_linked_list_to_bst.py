# Sorted Linked List to Balanced BST
# https://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/

# Link list node
class LNode:
    def __init__(self):
        self.data = None
        self.next = None


# A Binary Tree node
class TNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


head = None


def count_nodes(head: LNode):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next

    return count


def sorted_list_to_bst_recur(n):
    global head

    if n <= 0:
        return None

    left = sorted_list_to_bst_recur(int(n / 2))

    root = TNode(head.data)
    root.left = left

    head = head.next

    root.right = sorted_list_to_bst_recur(n - int(n / 2) - 1)

    return root


# Function to insert a node
# at the beginging of the linked list
def push(head, new_data):
    # allocate node
    new_node = LNode()

    # put in the data
    new_node.data = new_data

    # link the old list off the new node
    new_node.next = head

    # move the head to point to the new node
    head = new_node
    return head


# Function to print nodes in a given linked list
def print_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next


# A utility function to
# print preorder traversal of BST
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# This function counts the number of
# nodes in Linked List and then calls
# sortedListToBSTRecur() to construct BST
def sorted_list_to_bst():
    global head

    n = count_nodes(head)

    return sorted_list_to_bst_recur(n)


# Driver code
if __name__ == "__main__":
    # Start with the empty list
    head = None

    # Let us create a sorted linked list to test the functions
    # Created linked list will be 1.2.3.4.5.6.7
    head = push(head, 7)
    head = push(head, 6)
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)

    print("Given Linked List ")
    print_list(head)

    # Convert List to BST
    root = sorted_list_to_bst()
    print("\nPreOrder Traversal of constructed BST ")
    preorder(root)
