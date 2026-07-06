"""
    Song:
    title, artist, duration, next_song, prev_song
"""

class Song:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next_song = None
        self.prev_song = None
        
    def show_song(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Title:',self.title)
        print('Artist:',self.artist)
        print('Duration:',self.duration)
        print('HashCode:',self)
        print('Next Song:',self.next_song)
        print('Prev Song:',self.prev_song)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

song1 = Song(title='1. Jaan se Guzarte Hai',artist='Shashwat Sachdev, Khan Saab, Irshad Kamil, Nusrat Fateh Ali Khan',duration=4.5)
song2 = Song(title='2. Mashooqa (From “Cocktail 2”)',artist='Pritam, Mahmood, Amitabh Bhattacharya, Raghav Chaitanya, Ruaa Kayy',duration=3.5)
song3 = Song(title='3. Jaiye Sajana',artist='Shashwat Sachdev, Jasmine Sandlas, Satinder Sartaaj',duration=6.5)
song4 = Song(title='4. Bandhu 2.0 (From "Cocktail 2")',artist='Pritam, Kavita Seth, Neeraj Sridhar, Irshad Kamil',duration=5.2)
song5 = Song(title='5. Gehra Hua (From "Dhurandhar")',artist='Shashwat Sachdev, Arijit Singh, Irshad Kamil, Armaan Khan',duration=4.3)

# Hard Coded songs for next and previous
song1.next_song = song2
song2.next_song = song3
song3.next_song = song4
song4.next_song = song5
song5.next_song = song1

song1.prev_song = song5
song2.prev_song = song1
song3.prev_song = song2
song4.prev_song = song3
song5.prev_song = song4

# Hard Coded the way to display songs
# song1.show_song()
# song2.show_song()
# song3.show_song()
# song4.show_song() #implicit statement -> Song.show_song(song4) -> explicit statement
# Song.show_song(song5)

# Traversing in forward direction
# song = song1
# while True:
#     song.show_song()
#     song = song.next_song
#     if song == song1:
#         break

# Traversing in Backward Direction
song = song5
while True:
    song.show_song()
    song = song.prev_song
    if song == song5:
        break