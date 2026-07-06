class Song:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None
        self.prev = None
        print('[Song] [init] Object Constructed',self)
        
    def show(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Title:',self.title)
        print('Artist:',self.artist)
        print('Duration:',self.duration)
        print('HashCode:',self)
        print('Next Song:',self.next)
        print('Prev Song:',self.prev)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')