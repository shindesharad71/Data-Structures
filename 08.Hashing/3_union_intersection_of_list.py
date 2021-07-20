# Union and Intersection of two linked lists
# https://www.geeksforgeeks.org/union-intersection-two-linked-lists-set-3-hashing/

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node


def linked_list_to_arr(head: Node) -> list:
    arr = []

    current = head

    while current:
        arr.append(current.data)
        current = current.next

    return arr


def print_arr(arr: list):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def get_union_intersection_of_list(head1: Node, head2: Node):
    arr1 = linked_list_to_arr(head1)
    arr2 = linked_list_to_arr(head2)

    intersection = []
    union = dict()

    for i in range(len(arr1)):
        union[arr1[i]] = arr1[i]

    for i in range(len(arr2)):
        if arr2[i] in union:
            intersection.append(arr2[i])
        else:
            union[arr2[i]] = arr2[i]

    print("First list is:")
    print_arr(arr1)

    print("Second list is:")
    print_arr(arr2)

    print("Intersection list is:")
    print_arr(intersection)

    print("Union list is:")


# Driver Code
if __name__ == "__main__":
    head1 = LinkedList()
    head1.push(1)
    head1.push(2)
    head1.push(3)
    head1.push(4)
    head1.push(5)

    head2 = LinkedList()
    head2.push(1)
    head2.push(3)
    head2.push(5)
    head2.push(6)

    get_union_intersection_of_list(head1, head2)
