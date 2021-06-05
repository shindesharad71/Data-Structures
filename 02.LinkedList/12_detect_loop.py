# Detect loop in a linked list
# https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/


def detect_loop(self):
    s = set()
    temp = self.head

    while temp:
        # If we have already has
        # this node in hashmap it
        # means their is a cycle
        # (Because you we encountering
        # the node second time).
        if temp in s:
            return True

        # If we are seeing the node for
        # the first time, insert it in hash
        s.add(temp)
        temp = temp.next
    return False
