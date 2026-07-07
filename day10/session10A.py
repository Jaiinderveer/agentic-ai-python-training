class TollPlazaQueue:

    def __init__(self):
        self.head = None      # Front
        self.tail = None      # Rear
        self.size = 0
        print('[TollPlazaQueue] [init] Queue Constructed', self)

    def add(self, element):
        self.size += 1

        if self.head is None:
            self.head = element
            self.tail = element
            element.next = element
            element.prev = element
        else:
            self.tail.next = element
            element.prev = self.tail
            element.next = self.head
            self.head.prev = element
            self.tail = element

        print(f'\nVehicle Added to Queue. Size: {self.size}')
        element.show()

    def deduct_toll(self):

        if self.head is None:
            print("Queue is Empty")
            return

        element = self.head

        print(f'FastTag Balance for {element.registration_no}: ₹{element.fasttag.balance}')

        toll = 100 if element.type == '4W' else 50

        if element.fasttag.balance < toll:
            print("======================================")
            print("LOW FASTTAG BALANCE")
            print(f'Vehicle : {element.registration_no}')
            print(f'Balance : ₹{element.fasttag.balance}')
            print("Vehicle NOT removed from Queue.")
            print("======================================\n")
            return

        element.fasttag.balance -= toll

        print("Toll Deducted Successfully")
        print(f'New Balance: ₹{element.fasttag.balance}\n')

        self.delete()

    def delete(self):

        if self.head is None:
            print("Queue Empty")
            return

        if self.head == self.tail:
            print(f'Vehicle Removed from Queue. Size 0')
            self.head = None
            self.tail = None
            self.size = 0
            return

        temp = self.head

        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head

        del temp

        self.size -= 1

        print(f'Vehicle Removed from Queue. Size {self.size}\n')

    def delete_in_stack(self):

        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = 0
            return

        temp = self.tail

        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail

        del temp

        self.size -= 1

        print(f'Vehicle Removed from Stack. Size {self.size}')

    def show_list(self, traverse=True):

        if self.head is None:
            print("Queue is Empty")
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