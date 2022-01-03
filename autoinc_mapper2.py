
import sys

for line in sys.stdin:
    #Splitting the input from reducer 1
    data = line.split(',')

    make = data[0]
    year = data[1]
    accident_count = data[2]

    composite_key = make + year

    print(f'{composite_key}\t1')