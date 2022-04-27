
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def lprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

    #assumes index 0,1,2,3
    def get(self, position:int):
        # print("Position! " + str(position))
        if type(position) is not int or position < 0 or position > self.length:
            return None
        elif position == 0:
            return self.head
        else:
            current = self.head
            for _ in range(position):
                current = current.next
            return current

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.length = 1
        else:
            tail = self.get(self.length - 1)
            tail.next = Node(data)
            self.length += 1
   
    def insert(self, data:int, position:int = -1):
        if type(position) is not int or position < -1:
            return None
        elif position == -1 or position >= self.length:
            self.push(data)
        elif position == 0:
            current = self.head
            self.head = Node(data, current)
            self.length += 1
        else:
            prev = self.get(position - 1)
            current = prev.next
            prev.next = Node(data, current)
            self.length += 1

    # def pop(self, position):
    #     if type(position) is not int or position < 0:
    #         return None
    #     if position > self.length - 1:
    #         return None
    #     elif position == -1 or position == self.length - 1:
    #         new_tail = self.get(self.length - 2)
    #         new_tail.next = None
    #     else:

    def arrayFill(self, arr):
        if type(arr) is not list:
            return None            
        for i in range(len(arr)):
            self.push(arr[i])



# l = LinkedList()
# l.head = Node(3)
# e2 = Node("Tue")
# e3 = Node("Wed")

# # Link first Node to second node
# l.head.next = e2

# # Link second Node to third node
# e2.next = e3

# l.lprint()


llist = LinkedList()
llist.lprint()

# llist.push("MON")
# print(llist.length)
# llist.lprint()
# print("-----\n")

# llist.push("TUES")
# print(llist.length)
# llist.lprint()
# print("-----\n")

# llist.push("WED")
# print(llist.length)
# llist.lprint()
# print("-----\n")

# llist.push("THU")
# print(llist.length)
# llist.lprint()

# print("-----\n")

llist.insert("FRI-")
print(llist.length)
llist.lprint()

llist.insert("LUR?-", 0)
print(llist.length)
llist.lprint()

llist.insert("blup?-", 0)
print(llist.length)
llist.lprint()


llist.insert("mmmbop-", llist.length - 1)
print(llist.length)
llist.lprint()

llist.insert("chickablow-", llist.length)
print(llist.length)
llist.lprint()


llist.arrayFill([24, 24.23, "L", "f"])
llist.lprint()