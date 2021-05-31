# Implementing array data structure
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
        pass

    def copy(self):
        pass

    def count(self):
        pass

    def extend(self):
        pass

    def index(self):
        pass

    def insert(self):
        pass

    def __len__(self):
        return self.size

    def pop(self):
        pass

    def remove(self):
        pass

    def reverse(self):
        pass

    def sort(self):
        pass

dynamic = DynamicArray()
dynamic.s