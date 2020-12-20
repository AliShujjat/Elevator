import Floor_Elevator



class BinHeap(Floor_Elevator.Floor, Floor_Elevator.Elevator):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i].FloorNumber < self.heapList[i // 2].FloorNumber:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          # print("xxxxxxxxxxxx","      ",i,"  ",mc,"  ", self.currentSize)
          if self.heapList[i].FloorNumber > self.heapList[mc].FloorNumber:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2].FloorNumber < self.heapList[i*2+1].FloorNumber:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      #print(self.heapList)
      return retval

    def findMin(self):
      return self.heapList[1]

    def remove(self,i):
      a = self.heapList.index(i)
      x = self.heapList.pop(a)
      self.percDown(a)
      print(self.heapList)
      return x

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [Floor_Elevator.Floor(0,0)] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
      #print(self.heapList)

    def length(self):
      return len(self.heapList)

# bh = BinHeap()
# bh.buildHeap([])
# bh.insert(Floor_Elevator.Floor(0,0))
# print(bh.heapList)
# bh.insert(Floor_Elevator.Floor(3,0))
# print(bh.heapList)
# bh.insert(Floor_Elevator.Floor(1,0))
# print(bh.heapList)
# bh.insert(Floor_Elevator.Floor(9,0))
# print(bh.heapList)
# bh.insert(Floor_Elevator.Floor(12,0))
# print(bh.heapList)
# bh.insert(Floor_Elevator.Floor(13,0))
# print(bh.heapList)
# bh.insert(Floor_Elevator.Floor(14,0))
# print(bh.heapList)
