class MinHeap:
    def __init__(self,h_list):
        self.heap_list = list(h_list)
        self.current_size = 0

    def upSifter(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.upSifter(self.current_size)

    def downSifter(self, i):
        while (i * 2) <= self.current_size:
            minn = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = minn

    def min_child(self, i):
        if (i * 2 ) +1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[ i *2] < self.heap_list[( i *2 ) +1]:
                return i * 2
            else:
                return (i * 2) + 1

    def getAndDeleteMinimum(self):
        if len(self.heap_list) == 1:
            return 'Empty'
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        *self.heap_list, _ = self.heap_list
        self.current_size -= 1
        self.downSifter(1)
        return root


