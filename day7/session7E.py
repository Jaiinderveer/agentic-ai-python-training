flight1 = {
    'code':'6E6673',
    'carrier':'indigo',
    'source':'delhi',
    'destination':'bengaluru',
    'fare':4500,
    'duration':4.5
}
flight2 = {
    'code':'IX5962',
    'carrier':'air india',
    'source':'delhi',
    'destination':'bengaluru',
    'fare':5000,
    'duration':3.5
}
flight3 = {
    'code':'IX5647',
    'carrier':'air india',
    'source':'delhi',
    'destination':'bengaluru',
    'fare':3500,
    'duration':2.5
}
flight4 = {
    'code':'IH6734',
    'carrier':'air india',
    'source':'delhi',
    'destination':'bengaluru',
    'fare':5500,
    'duration':1.5
}
flight5 = {
    'code':'IA2346',
    'carrier':'air india',
    'source':'delhi',
    'destination':'bengaluru',
    'fare':6000,
    'duration':0.5
}

#List of Dictionaries
#             0       1       2       3       4
flights = [flight1,flight2,flight3,flight4,flight5]

# Search a flight -> code
# sort Flights -> fare,duration
# Filter Flights -> carrier,fare,duration,source,destination

def search(flights,code):
    for flight in flights:
       if flight['code'] == code:
           print(flight)
           break
    else:
        print('No matching flight found for code',code) 
def main():
    search(flights,'IA2346')
    search(flights,'IH6794')
if __name__ == '__main__':
    main()