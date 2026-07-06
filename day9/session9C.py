class CircularDoublyLinkedList:
    
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print('[CDLL] [init] Object Constructed',self)
        
    def add(self,element):
        self.size += 1
        if self.head == None:
            self.head = element
            self.tail = element
            element.next = element
            element.prev = element
        else:
            self.tail.next = element
            self.head.prev = element
            element.prev = self.tail
            element.next = self.head
            self.tail = element
            
    def add_in_front(self,element):
        self.size += 1
        if self.head == None:
            self.head = element
            self.tail = element
            element.next = element
            element.prev = element
        else:
            element.next = self.head
            element.prev = self.tail
            self.head.prev = element
            self.tail.next = element
            self.head = element 
    
    def add_in_between(self,element,element1,element2):
        if self.size < 2:
            print('Choose Another Method to add')
            return
        if element1.next != element2 or element2.prev != element1:
            print("The given nodes are not adjacent.")
            return
        self.size += 1   
        element1.next = element
        element2.prev = element
        element.prev = element1
        element.next = element2
    def delete_last(self):
        if self.tail == None:
            print('No element to delete!')
            return
        
        if self.head == self.tail:
            del self.tail
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            del temp
        self.size -= 1
    def delete_front(self):
        if self.head is None:
            print("No element to delete!")
            return

        if self.head == self.tail:
            del self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            del temp
        self.size -= 1
        
    def delete(self, element):
        if self.head is None:
            print("No element to delete!")
            return

        # Single node
        if self.head == self.tail:
            if self.head == element:
                del self.head
                self.head = None
                self.tail = None
                self.size -= 1
            else:
                print("Element not found")
            return

        temp = self.head

        while True:
            if temp == element:
                break

            temp = temp.next

            if temp == self.head:
                print("Element not found")
                return

        if temp == self.head:
            self.head = self.head.next

        if temp == self.tail:
            self.tail = self.tail.prev

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

        del temp
        self.size -= 1
    def show_list(self,traverse = True):
        if self.head is None:
            print("List is empty")
            return
        if traverse:
            element = self.head
            while True:
                element.show()
                element = element.next

                if element == self.head:
                    break
        else:
            element = self.tail
            while True:
                element.show()
                element = element.prev
                if element == self.tail:
                    break