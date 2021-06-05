# Write a function that counts the number of times a given int occurs in a Linked List
# https://www.geeksforgeeks.org/write-a-function-that-counts-the-number-of-times-a-given-int-occurs-in-a-linked-list/


def occurrence_count(self, keyword):
    count = 0
    temp = self.head

    while temp:
        if temp.data == keyword:
            count += 1
        temp = temp.next

    print(count)
    return count
