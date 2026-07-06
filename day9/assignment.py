from session9C import CircularDoublyLinkedList

playlist = CircularDoublyLinkedList()

class Video:
    
    def __init__(self,title,channel,duration):
        self.title = title
        self.channel = channel
        self.duration = duration
        self.next = None
        self.prev = None
        print('[Video] [init] Object Constructed',self)
    def show(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Title:',self.title)
        print('Channel:',self.channel)
        print('Duration:',self.duration)
        print('HashCode:',self)
        print('Next Video:',self.next)
        print('Prev Video:',self.prev)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
playlist.add_in_front(element=Video(title='How To Pass/Score in Engineering Mechanics | First Year Engineering | MU',channel='Last moment tuitions',duration=14.13))
playlist.add(element=Video(title='Introduction to Engineering Mechanics | Engineering Mechanics in Hindi',channel='Last moment tuitions',duration=15.49))
playlist.add_in_front(element=Video(title='Introduction to Coplanar forces | Engineering Mechanics in Hindi',channel='Last moment tuitions',duration=25.19))
playlist.add(element=Video(title='Equilibrium in Coplanar Forces | Engineering Mechanics in Hindi',channel='Last moment tuitions',duration=12.14))
playlist.add_in_front(element=Video(title='Couple Full Concept | Engineering Mechanics in Hindi',channel='Last moment tuitions',duration=10.56))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Before Deletion:')
playlist.show_list()
playlist.delete_front()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('After Deleting Front:')
playlist.show_list()
playlist.delete_last()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('After Deleting Last:')
playlist.show_list()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')