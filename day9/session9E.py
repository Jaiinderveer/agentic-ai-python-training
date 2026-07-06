from session9B import Song 
from session9C import CircularDoublyLinkedList

song_list = CircularDoublyLinkedList()

song_list.add(element=Song(title='1. Jaan se Guzarte Hai',artist='Shashwat Sachdev, Khan Saab, Irshad Kamil, Nusrat Fateh Ali Khan',duration=4.5))
song_list.add(element=Song(title='2. Mashooqa (From “Cocktail 2”)',artist='Pritam, Mahmood, Amitabh Bhattacharya, Raghav Chaitanya, Ruaa Kayy',duration=3.5))
song_list.add(element=Song(title='3. Jaiye Sajana',artist='Shashwat Sachdev, Jasmine Sandlas, Satinder Sartaaj',duration=6.5))
song_list.add(element = Song(title='4. Bandhu 2.0 (From "Cocktail 2")',artist='Pritam, Kavita Seth, Neeraj Sridhar, Irshad Kamil',duration=5.2))
song_list.add(element=Song(title='5. Gehra Hua (From "Dhurandhar")',artist='Shashwat Sachdev, Arijit Singh, Irshad Kamil, Armaan Khan',duration=4.3))

song_list.show_list(False)

# Implement the functions in circular doubly linked list on some different object (flight,chat_message, etc. of your choice)