def heapsort(list):
  #initialize Heap
  heap = Heap()
  list_sorted = []

  for item in list:
    heap.insert(item)
  while heap.size > 0:
    list_sorted.append(heap.delete())
    #list_sorted.insert(0, heap.delete()) -- if you do this you don't need to reverse
    #however it adds another O(n)
  list_sorted.reverse()
  return list_sorted


class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    retval = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return retval 

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index // 2] < self.storage[index]:
        self.storage[index], self.storage[index // 2] = self.storage[index // 2], self.storage[index]
      index = index // 2

  def _sift_down(self, index):
    while (index * 2) <= self.size:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1