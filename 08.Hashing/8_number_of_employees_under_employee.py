# Find number of Employees Under every Employee
# https://www.geeksforgeeks.org/find-number-of-employees-under-every-manager/


def assign_pnd_print(t: tuple):
    # We will directly permute over t. Access 2nd element(i.e. manager) of certain tuple and assign the relation in
    # dictionary. We will assign list of employees to a particular manager so that with iterations, we can append
    # more employees to that list and list grows.
    d = dict()

    for pair in t:
        if pair[0] == pair[1]:
            continue

        if pair[0] not in d:
            d[pair[0]] = []

        if pair[1] not in d:
            d[pair[1]] = [pair[0]]
        else:
            d[pair[1]].append(pair[0])

    # now we know how many employees are directly under a particular manager.
    # now lets count the total number of employees under a particular manager.
    c = dict()

    for manager in d:
        c[manager] = len(d[manager])
        for employee in d[manager]:
            c[manager] += len(d[employee])
        print(f"{manager} : {c[manager]}")


# Driver Code
if __name__ == "__main__":
    # t is tuple containing employee and boss pair.
    t = (("A", "C"), ("B", "C"), ("C", "F"), ("D", "E"), ("E", "F"), ("F", "F"))
    assign_pnd_print(t)
