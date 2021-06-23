# Program for Page Replacement Algorithms | Set 2 (FIFO)
# https://www.geeksforgeeks.org/program-page-replacement-algorithms-set-2-fifo/

from queue import Queue


def page_faults(pages: list, n: int, capacity: int) -> int:
    # To represent set of current pages.
    # We use an unordered_set so that we
    # quickly check if a page is present
    # in set or not
    s = set()

    # To store the pages in FIFO manner
    indexes = Queue()

    # Start from initial page
    page_fault = 0

    for i in range(n):
        # Check if the set can hold
        # more pages
        if len(s) < capacity:

            # Insert it into set if not present
            # already which represents page fault
            if pages[i] not in s:
                s.add(pages[i])
                page_fault += 1

                indexes.put(pages[i])

        else:
            if pages[i] not in s:
                val = indexes.queue[0]
                indexes.get()

                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                page_fault += 1

    return page_fault


# Driver code
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4
    print(page_faults(pages, n, capacity))
