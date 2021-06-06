# Write a function to get the intersection point of two Linked Lists
# https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/

# We are going to use Hashing here

# Method 7 (Use Hashing)
# Basically, we need to find a common node of two linked lists. So we hash all nodes of the first list and then check the second list.
# 1) Create an empty hash set.
# 2) Traverse the first linked list and insert all nodes’ addresses in the hash set.
# 3) Traverse the second list. For every node check if it is present in the hash set. If we find a node in the hash set, return the node.


def intersection_node(list1, list2):
    set = set()

    temp = list1.head
    while temp:
        set.add(temp)
        temp = temp.next

    temp = list2.head
    while temp:
        if temp in set:
            return temp
        temp = temp.next
