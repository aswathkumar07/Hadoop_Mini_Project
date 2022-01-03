
import sys

##Initializing empty dictionary
masterinfo = {}

def flush():
    for key, value in masterinfo.items():
        print(f'{key},{value}')

#Input comes from STDIN (standard input)
for line in sys.stdin:
    # Splitting each line of data into a list
    data = line.split('\t')
    
    make_year = data[0]

    accident_count = int(data[1])

    if make_year not in masterinfo:
        masterinfo[make_year] = accident_count
    else:
        masterinfo[make_year] += accident_count

flush()

