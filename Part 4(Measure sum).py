import csv
import collections 
from collections import Counter
import numpy as np
from functools import partial

filename = "C:/Users/Юлия/Desktop/Eurecom/Courses/Semester_project/data/track_uri_seq.csv"

#reading csv file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ';')
   
    Rows = []
    Songs = []
   
    for playlist in csvreader:
        Rows.append(playlist)
    print('Number of playlists:', len(Rows))    

    for playlist in Rows:
        for name in playlist:
            Songs.append(name)
    print('Number of songs:', len(Songs))

    #Counter - dictionary containing keys and counts
    l = Counter(Songs)

    #Measure the partial sum of all playlists divided into 2 parts:
    Unite_parts = []
    for playlist in Rows:
        split_point = len(playlist)//3

        First_sum = 0
        Second_sum = 0
        Fhird_sum = 0
        
        for name in playlist[:split_point]:
            freq = l[name]
            First_sum = freq + First_sum

        for name in playlist[split_point:split_point*2]:
            freq = l[name]
            Second_sum = freq + Second_sum

        for name in playlist[split_point*2:]:
            freq = l[name]
            Fhird_sum = freq + Fhird_sum
        
        t = [First_sum, Second_sum, Fhird_sum]
        Unite_parts.append(t)
        
    #print ('Unite', Unite_parts)   
   
    #Measure the total sum of the variables for divided playlists parts
    List = np.array(Unite_parts)
    np.sum = partial(np.sum, dtype=np.int64)
    res = np.sum(List,0)
    print('Total first/second sum', res)
   
 
