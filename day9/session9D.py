from session9B import Song 
from session9C import CircularDoublyLinkedList

song_list = CircularDoublyLinkedList()
print(vars(song_list))

song1 = Song(title='1. Jaan se Guzarte Hai',artist='Shashwat Sachdev, Khan Saab, Irshad Kamil, Nusrat Fateh Ali Khan',duration=4.5)

print(vars(song1))


song_list.add(song1)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('After Addition of Song1:')
print(vars(song_list))
print(vars(song1))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

song2 = Song(title='2. Mashooqa (From “Cocktail 2”)',artist='Pritam, Mahmood, Amitabh Bhattacharya, Raghav Chaitanya, Ruaa Kayy',duration=3.5)

song_list.add(song2)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('After Addition of Song2:')
print(song_list)
print(song1)
print(song2)
print(vars(song1))
print(vars(song2))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

song3 = Song(title='3. Jaiye Sajana',artist='Shashwat Sachdev, Jasmine Sandlas, Satinder Sartaaj',duration=6.5)

song_list.add(song3)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('After Addition of Song:')
print(vars(song_list))
print(song1)
print(song2)
print(song3)
print(vars(song1))
print(vars(song2))
print(vars(song3))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
