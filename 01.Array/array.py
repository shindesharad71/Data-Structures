# Experiments using arrays in Python

def array_test():
    arr: list = [i for i in range(1, 11)]

    print(f"Generated Array - {arr}")

    arr.pop()
    print(f"Array - {arr}")

    arr.reverse()
    print(f"Array - {arr}")

    arr.sort()
    print(f"Array - {arr}")

    arr.append(10)
    print(f"Array - {arr}")

    print(f"Index of 2 - {arr.index(2)}")

    arr.remove(5)
    print(f"Remove by value {arr}")

def main():
    array_test()

if __name__ == "__main__":
    main()