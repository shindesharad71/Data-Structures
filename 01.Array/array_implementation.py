# Implementing array data structure
# https://medium.com/swlh/data-structure-and-algorithms-implement-dynamic-array-in-python-be47e1d6ce06
class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = self._create_array(self.capacity)

    @staticmethod
    def _create_array(capacity):
        return [None] * capacity

    def __getitem__(self, index):
        if self.size >= (index + 1):
            return self.arr[index]
        raise IndexError(f"GIven index {index} is greater than array size {self.size}")

    def _resize(self, new_capacity):
        new_arr = self._create_array(new_capacity)

        for i in range(self.capacity):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def append(self, element):
        if self.size == self.capacity:
            self.capacity = self.capacity * 2

        self.arr[self.size] = element
        self.size += 1

    def clear(self):
        self.size = 0
        self.capacity = 1
        self.arr = self._create_array(self.size)

    def copy(self, new_arr):
        for i in range(self.capacity):
            new_arr[i] = self.arr[i]

        return new_arr

    def count(self, element):
        count = 0
        for i in range(self.capacity):
            if arr[i] == element:
                count += 1
        return count

    def extend(self, new_arr):
        for elm in new_arr:
            self.append(elm)
        return self.arr

    def index(self, element):
        for i in range(self.capacity):
            if arr[i] == element:
                break
        return i

    def insert(self):
        pass

    def __len__(self):
        return self.size

    def pop(self):
        element = None

        if self.size > 0:
            element = self.array[self.size - 1]
            self.array[self.size - 1] = None
            self.size -= 1

            if self.size <= self.capacity // 4:
                self._resize(self.capacity // 2)

        return element

    def remove(self):
        pass

    def reverse(self):
        pass

    def sort(self):
        pass

# Test code
dynamic = DynamicArray()
dynamic._create_array(2)
dynamic.append(1)
print(dynamic)