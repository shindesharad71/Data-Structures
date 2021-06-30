# Populate Inorder Successor for all nodes
# https://www.geeksforgeeks.org/populate-inorder-successor-for-all-nodes/


def populate_next(node):
    # The first visited node will be the rightmost node
    # next of the rightmost node will be NULL
    populate_next_recur(node, next)


# Set next of all descendants of p by
# traversing them in reverse Inorder
def populate_next_recur(p, next_ref):
    if p is not None:
        # First set the next pointer in right subtree
        populate_next_recur(p.right, next_ref)

        # Set the next as previously visited node in reverse Inorder
        p.next = next_ref

        # Change the prev for subsequent node
        next_ref = p

        # Finally, set the next pointer in right subtree
        populate_next_recur(p.left, next_ref)
