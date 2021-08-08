class Node:
    def __init__(self, elem=None):
        self.elem = elem
        self.next = None


class SingLink:

    def __init__(self, node=None):
        self._head = node
        self.temp = node

    def is_empty(self):
        return self._head == None

    def add(self, item):
        pass

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            try:
                cur = cur.next
            except AttributeError:
                break
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next


    def travel_two(self):
        cur = self._head
        while True:
            try:
                yield cur.elem
                cur = cur.next
            except AttributeError:
                break




s = SingLink()
s.append(11)
s.append(22)
s.append(33)
s.append(44)
# s.travel()
a = s.travel_two()
for i in a:
    print(i)

s.append(55)
a = s.travel_three()
while True:
    print(111)
