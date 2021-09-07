class MinHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def printSelf(self):
        print(self.storage)

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def getLeftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def getRightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def heapifyUp(self, index):
        index = self.size - 1
        if(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

    def insert(self, data):
        if(self.isFull()):
            raise("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)

    def heapifyDown(self, index):
        smallest = index
        if(self.hasLeftChild(index) and self.storage[smallest] > self.getLeftChild(index)):
            smallest = self.getLeftChildIndex(index)
        if(self.hasRightChild(index) and self.storage[smallest] > self.getRightChild(index)):
            smallest = self.getRightChildIndex(index)
        if(smallest != index):
            self.swap(index, smallest)
            self.heapifyDown(smallest)

    def removeMin(self):
        if(self.size == 0):
            raise("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return data


huge = MinHeap(8)
huge.printSelf()
