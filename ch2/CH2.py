from collections import defaultdict
import json as js
from collections import Counter


path = 'ch2/ch2.txt'

records = [js.loads(line) for line in open(path, 'rb')]
print(records[0])
print(records[1]['tz'])

'''
gather all timezone in this data
loop should handle if tz exists condition
'''

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

print(len(time_zones))

'''
write a loop so that we can find the counts in time_zone
Count may be different cause lot of are blank value in the list
'''

def findcounts():
    counts =0
    for i in time_zones:
        if(len(i)>0):
            #print(i)
            counts = counts +1
    return counts

print(findcounts())

'''
convert entire sequence (in this case timezone) into a dictionary where key is the timezone
and the value is the count of how many time that timezone appeared in the sequence
'''
def find_number_of_appearence_in_the_timezone(sequence):
    number_of_appearence = defaultdict(int) # values will initialize to 0
    for x in sequence:
        number_of_appearence[x] += 1
    return number_of_appearence


tz_count_dictionary = find_number_of_appearence_in_the_timezone(time_zones)
print(tz_count_dictionary['America/New_York'])
print(tz_count_dictionary['America/Denver'])
print(tz_count_dictionary['Asia/Riyadh'])

'''
Find Top 10 Time zone appearence from the dictionary
that gets created in find_number_of_appearence_in_the_timezone
'''
def find_top_appearence(dictionary, n=10):
    value_key_pairs = [(count, tz) for tz, count in dictionary.items()] # This line switches keys and values
    value_key_pairs.sort()
    return value_key_pairs[-n:] # return last 10 items of the dictionary which has top appearences

print(find_top_appearence(tz_count_dictionary))

'''
Another way to find top appearance is using collections and counter
'''
my_counts = Counter(time_zones)
print(my_counts.most_common(10))