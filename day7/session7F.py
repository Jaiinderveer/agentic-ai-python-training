from session7E import flights

def sort(flights,key,low_to_high=True):
    for i in range(len(flights)-1):
        for j in range(len(flights)-i-1):
            if low_to_high:
                # if(flights[j]['fare']>flights[j+1]['fare']):
                if(flights[j][key]>flights[j+1][key]):
                    flights[j],flights[j+1] = flights[j+1],flights[j]
            else:
                # if(flights[j]['fare']<flights[j+1]['fare']):
                if(flights[j][key]<flights[j+1][key]):
                    flights[j],flights[j+1] = flights[j+1],flights[j]

criteria = input('Enter Sorting Criteria: fare/duration: ')
sort(flights,criteria)
for flight in flights:
    print(flight)
    print('~~~~~~~~~~~~~~~~~~~')