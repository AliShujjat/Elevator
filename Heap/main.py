import random
import Heap
import time
import Floor_Elevator
random.seed(3856)


def gen():
    return random.randint(0,1)

if __name__ == '__main__':


    FloorList = Heap.BinHeap()
    FloorList.buildHeap([])
    ElevatorList = [Floor_Elevator.Elevator(50,2), Floor_Elevator.Elevator(200,3), Floor_Elevator.Elevator(15,4)]

    for i in range(1,50000):
        if gen() == 1 :
            p = random.randint(0,20)
            FloorList.insert(Floor_Elevator.Floor(i,p))

    # FloorList.insert(Floor_Elevator.Floor(3,5))
    # FloorList.insert(Floor_Elevator.Floor(6,15))

    prevmin = 0
    TimeTaken = False
    check = 0
    # print(FloorList.length())

    while FloorList.length() != 1:
    # while FloorList.length() <=1:
        min = float("inf")
        flag = False
        check +=1
        # print("visibly clear", FloorList.length())

        # for j in FloorList.heapList:

        for i in ElevatorList:
            # print("hey")

            j = FloorList.findMin()
            prevmin = i.differential(j)

            if i.CurrentFloor == j.FloorNumber :

                EleObj = i
                FlrObj = j
                flag = True ## Flag Showing that we are ready to board hence breaking
                break

            elif i.differential(j) < min or (prevmin == i.differential(j) and gen() == 1):

                EleObj = i
                FlrObj = j
                min = i.differential(j)
                prevmin = min

        if flag: # Breaking again for same reason
            break

        if time.process_time() > 10 and TimeTaken == False:
            for i in range(1,20):
                print("floor added")
                p = random.randint(0,20)
                FloorList.insert(Floor_Elevator.Floor(i,p))
            TimeTaken = True

        # print("yes")
        # for j in FloorList.heapList:
        #     j.check()
                
        EleObj.boarder(FlrObj)
        EleObj.CurrentFloor = FlrObj.FloorNumber

        # for i in ElevatorList:
        #     i.check()

        if EleObj.Capacity == 20:
            EleObj.CurrentFloor = 0
            FloorList.heapList[0].Passengers += EleObj.Capacity
            EleObj.Capacity = 0
            # print("xxxxxxx")
            # FloorList.heapList[0].check()

        if FlrObj.Passengers == 0: # Removing Floor Object
            # print("Agai")
            bx=FloorList.delMin()
            # print("     Floor removed:   ", bx.FloorNumber)

        # for j in FloorList.heapList:
        #     j.check()

        # for i in ElevatorList:
        #     i.check()
        # print("xxxxxxxxxxxxxxx")

    print("Time taken by programme: ", time.process_time())
    print("Floor length     ",FloorList.length())


