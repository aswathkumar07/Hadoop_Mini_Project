
import sys

#Input comes from STDIN (standard input)
for line in sys.stdin:
    # Splitting each line of csv data into a list
    data = line.split(',')
    
    #Getting VIN number, Incident Type, Make, Year from the list
    vin_no = data[2]
    incident_type = data[1]
    make = data[3]
    year = data[5]

    value = (incident_type, make, year)

    #Printing in the format Vin NO <TAB> Incident Type, Make, Year
    print(f'{vin_no}\t{value}')

