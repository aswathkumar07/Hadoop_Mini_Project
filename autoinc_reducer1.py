
import sys

#Initializing empty dictionary
masterinfo = {}

def flush():
    """
        Delivering the output for use in Mapper 2
    """
    for key in masterinfo.keys():
        print(f'''{masterinfo[key]['make']},{masterinfo[key]['year']},{masterinfo[key]['accident_count']}''')

#Splitting each line from mapper1 output into a list
for line in sys.stdin:
    data = line.split('\t')
    #Getting Vin no from list
    vin_no = data[0]

    #Getting Incident_Type, Make, Year in appropriate list for further use
    incidenttype_make_year_list =  [val.replace("'", "").replace("(", "").replace(")", "").replace(" ", "").replace('\n', '') for val in data[1].split(",")]

    #Saving Incident_Type, Make, Year in individual variables
    incident_type = incidenttype_make_year_list[0]
    make = incidenttype_make_year_list[1]
    year = incidenttype_make_year_list[2]

    #Initiate a new vin_no key if it does not exist master dictionary
    if vin_no not in masterinfo:
        masterinfo[vin_no] = {'make': None, 'year': None, 'accident_count': 0}

    #Populate dictionary with make and year values
    if incident_type == 'I':
        masterinfo[vin_no]['make'] = make
        masterinfo[vin_no]['year'] = year

    #Calculate accident_count value
    if incident_type == 'A':
        masterinfo[vin_no]['accident_count'] += 1

flush()

