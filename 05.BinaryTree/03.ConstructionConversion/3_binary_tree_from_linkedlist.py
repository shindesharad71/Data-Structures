# Construct Complete Binary Tree from its Linked List Representation
# https://www.geeksforgeeks.org/given-linked-list-representation-of-complete-tree-convert-it-to-linked-representation/

# LinkedList Node
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Binary Tree Node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Class to convert the linked list to Binary Tree
class Conversion:

    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self, data=None):
        self.head = None
        self.root = None

    def push(self, data):
        node = ListNode(data)

        # Make next of new node as head
        node.next = self.head

        # Move the head to point to new node
        self.head = node

    def convert_list_to_binary(self):
        # Queue to store parent node
        q = []

        # Base case
        if self.head is None:
            self.root = None
            return

        # 1.) The first node is always the root node,
        # and add it to the queue
        self.root = TreeNode(self.head.data)
        q.append(self.root)

        # Advance the pointer to the next node
        self.head = self.head.next

        # Until the end of the linked list is reached, do:
        while self.head:
            # 2.a) Take the parent node from the q and
            # and remove it from q
            parent = q.pop(0)  # Front of the queue

            # 2.c) Take next two nodes from the linked list.
            # We will add them as children of the current
            # parent node in step 2.b.
            # Push them into the queue so that they will be
            # parent to the future node
            left_child = None
            right_child = None

            left_child = TreeNode(self.head.data)
            q.append(left_child)
            self.head = self.head.next

            if self.head:
                right_child = TreeNode(self.head.data)
                q.append(right_child)
                self.head = self.head.next

            # 2.b) Assign the left and right children of parent
            parent.left = left_child
            parent.right = right_child

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)


# Driver Code
if __name__ == "__main__":
    conv = Conversion()
    conv.push(36)
    conv.push(30)
    conv.push(25)
    conv.push(15)
    conv.push(12)
    conv.push(10)

    conv.convert_list_to_binary()

    print("Inorder Traversal of the constructed Binary Tree is:")
    conv.inorder_traversal(conv.root)
