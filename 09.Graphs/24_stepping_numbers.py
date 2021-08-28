# Stepping Numbers
# https://www.geeksforgeeks.org/stepping-numbers/


# A Python3 program to find all the Stepping Numbers
# in range [n, m] using DFS Approach

# Prints all stepping numbers reachable from num and in range [n, m]
def dfs(n, m, stepNum):

    # If Stepping Number is in the
    # range [n,m] then display
    if stepNum <= m and stepNum >= n:
        print(stepNum, end=" ")

    # If Stepping Number is 0 or greater
    # than m, then return
    if stepNum == 0 or stepNum > m:
        return

    # Get the last digit of the currently
    # visited Stepping Number
    lastDigit = stepNum % 10

    # There can be 2 cases either digit
    # to be appended is lastDigit + 1 or
    # lastDigit - 1
    stepNumA = stepNum * 10 + (lastDigit - 1)
    stepNumB = stepNum * 10 + (lastDigit + 1)

    # If lastDigit is 0 then only possible
    # digit after 0 can be 1 for a Stepping
    # Number
    if lastDigit == 0:
        dfs(n, m, stepNumB)

    # If lastDigit is 9 then only possible
    # digit after 9 can be 8 for a Stepping
    # Number
    elif lastDigit == 9:
        dfs(n, m, stepNumA)
    else:

        dfs(n, m, stepNumA)
        dfs(n, m, stepNumB)


# Method displays all the stepping
# numbers in range [n, m]
def displaySteppingNumbers(n, m):

    # For every single digit Number 'i'
    # find all the Stepping Numbers
    # starting with i
    for i in range(10):
        dfs(n, m, i)


n, m = 0, 21

# Display Stepping Numbers in
# the range [n,m]
displaySteppingNumbers(n, m)
