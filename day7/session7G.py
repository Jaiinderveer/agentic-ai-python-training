from session7E import flights
#Assignment: Complete Filter Code
def display(flight):
    print("------------------------")
    print(flight)
    print("------------------------")

def filter_flights(flights,criteria):
        if criteria == 'fare' or criteria == 'duration':
            value = float(input('Enter Value to Filter: '))
            choice = input("1. Greater Than\n2. Less Than\nEnter Choice: ")
            if choice == '0':
                for flight in flights:
                    if flight[criteria] > value:
                        display(flight)
            else:
                for flight in flights:
                    if flight[criteria] < value:
                        display(flight)
        else:
            value = input('Enter Value to Filter: ').lower()
            for flight in flights:
                if flight[criteria] == value:
                    display(flight)
                    
criteria = input('Enter Filtering Criteria: ').lower()
valid = ['carrier','fare','duration','source','destination']

if criteria not in valid:
    print("Invalid Criteria")
    exit()
filter_flights(flights,criteria)