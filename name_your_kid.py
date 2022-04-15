import os
import csv
from collections import OrderedDict
import pprint

total_names_to_print = 1000
names2019 = OrderedDict({})
names2020s = OrderedDict({})

sex = 'M'
total = 0

for year in range(1999, 2020):
    # print('Year: %s' % year)
    file = os.getcwd() + '\\yob%s.txt' % year

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[1] == sex:
                line_count += 1

                # get the latest data from 2019
                if year == 2019:
                    total += int(row[2])
                    names2019['%s' % row[0]] = {'Rank': line_count, 'Number': int(row[2])}
                    # if line_count < total_names_to_print:
                    #     print(f'\t Name: {row[0]}, sex: {row[1]}, Total in 2019: {row[2]}.')

                # create cumulative name totals for the 2000s
                if names2020s.get(row[0]) is not None:  #
                    names2020s[row[0]] += int(row[2])
                else:
                    names2020s['%s' % row[0]] = int(row[2])

        print(f'Processed {line_count} lines for year %s' % year)

print(total)

# create ranking for the names
sortednames2020s = OrderedDict(sorted(names2020s.items(), key=lambda t: -t[1]))
# pprint.pprint(sortednames2020s)

# Specific name searches
rank = 0
for key, value in sortednames2020s.items():
    rank += 1
    sortednames2020s[key] = {'Rank': rank, 'Number': value}
    # if 1000 < rank < 2000:
    #     print(f'Name {key}, rank {rank}, number {value}')
    # if key[0] == 'X':
    #     print(f'Name {key}, rank {rank}, number {value}')
    # if 'J' in key and 'ji' in key:
    #    print(f'Name {key}, rank {rank}, number {value}')
    # if key[0] == 'L':
    #     print(f'Name {key}, rank {rank}, number {value}')
    # if 'ili' in key:
    #     print(f'Name {key}, rank {rank}, number {value}')
    # if key[-2:] == 'ji':
    #     print(f'Name {key}, rank {rank}, number {value}')


names = [
    'Ezra',  
    'Leo', 
    'Elias', 
    'Waldo', 
    'Emerson',
    'Apollo', 
    'Odin', 
	'Oliver', 
	'Luca', 
	'Samuel', 
	'Denver', 
	'Franklin', 
	'Finn', 
	'Jude', 
	'Reuben', 
	'Micah', 
	'Orion', 
	'Ty', 
	'Asa', 
	'Noah', 
	'Isaiah', 
    ]

for name in names:
    try:
        print(f'"{name}" is ranked {names2019.get(name).get("Rank")} with {names2019.get(name).get("Number")} boys '
              f'in 2019.')
    except Exception as e:
        print('%s - No 2019 data on that name' % name)

    try:
        print(f'\t\tUsing 1999-2019 data, "{name}" is ranked {sortednames2020s.get(name).get("Rank")} with '
              f'{sortednames2020s.get(name).get("Number")} boys.')
    except Exception as e:
        print('\t\t%s - No 2000s data on that name' % name)
