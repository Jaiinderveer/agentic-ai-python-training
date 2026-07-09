"""
    Vehicle,5
    FastTag,5
    TollPlazaQueue,1


"""

file = open('day10/session10B.py','r')
lines = file.readlines()
vehicle_count = 0
fasttag_count = 0
tollplazaqueue_count = 0
for line in lines:
    if 'import' not in line:
        if 'Vehicle' in line and 'Vehicles' not in line:
            vehicle_count+=1
        if 'FastTag' in line:
            fasttag_count+=1
        if'TollPlazaQueue' in line:
            tollplazaqueue_count +=1
with open('objectAnalysis.csv','a') as output:
    output.write(f'Vehicle,{vehicle_count}\nFastTag,{fasttag_count}\nTollPlazaQueue,{tollplazaqueue_count}\n')
