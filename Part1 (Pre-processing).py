import csv
import collections 
from collections import Counter
import time
import copy

filename = "C:/Users/Юлия/Desktop/Eurecom/Courses/Semester_project/data/track_uri_seq.csv"

#reading csv file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ';')

    Rows = []
    Songs = []
    
    for playlist in csvreader:
        Rows.append(playlist)
    print('Number of playlists:', len(Rows))    
    #Number of playlists: 1000001

    for playlist in Rows:
        for name in playlist:
            Songs.append(name)
    print('Number of songs:', len(Songs))
    #Number of songs: 66346428
    
    unique_songs = set(Songs)#Set — unordered collections of unique elements
    print('Number of unique songs:', len(unique_songs))
    #Number of unique songs: 2262292
	
    
    counter = collections.Counter(Songs)
    l = counter.most_common(100)
    #print('Frequency of 100 most popular songs:', l)
    Popular_songs = [name for name, name_count in l]
    #print('First 100 popular songs:', Popular_songs)
    
    '''  
    #Isolate lists with popular songs
    start = time.time()
    newlist = []
    for playlist in Rows:
        for name in playlist:
            if name in Popular_songs:
                if playlist not in newlist:
                    newlist.append(copy.copy(playlist))
                    print('Number of newlists:', len(newlist)) 
    print('Number of newlists:', len(newlist))
    end = time.time()
    print('Time', end - start)
	'''
    


    
    
    


        
