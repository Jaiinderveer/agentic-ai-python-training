class TollPlazaQueue:
    def __init__(self):
        self.head = None  # For queue term is front
        self.tail = None # For queue term is End
        self.size = 0
        print('[TollPlazaQueue] [init] Queue Constructed',self)
        
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
            
        print(f'\nVehicle added to Queue. Size {self.size}')
        element.show()
        # After adding Vehicle, deduct toll
    
    def deduct_toll(self,element):
        print(f'FastTag Balance for {element.registration_no} ₹{element.fasttag.balance}')
        if element.type == '4W':
            element.fasttag.balance -= 100
        else:
            element.fasttag.balance -= 50
        
        print(f'Toll Deducted')
        print(f'New FastTag Balance for {element.registration_no} ₹{element.fasttag.balance}\n')
        self.delete()
            
    def delete(self):
        self.size -= 1
        self.head = self.head.next
        print(f'Vehicle Removed from Queue. Size {self.size}')
    def delete_in_stack(self):
        self.size -= 1
        self.tail = self.tail.prev
        print(f'Vehicle Removed from Stack. Size {self.size}')
    
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