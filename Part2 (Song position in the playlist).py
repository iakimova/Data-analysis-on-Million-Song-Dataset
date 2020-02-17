import csv
import collections 
from collections import Counter

#full playlists
filename = "C:/Users/Юлия/Desktop/Eurecom/Courses/Semester_project/data/track_uri_seq.csv"

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ';')

    Rows_full = []
    Songs_full = []
    
    for playlist in csvreader:
        Rows_full.append(playlist)
    print('Number of Rows_full:', len(Rows_full))    
    #Number of Rows_full: 1000001

    for playlist in Rows_full:
        for name in playlist:
            Songs_full.append(name)
    print('Number of Songs_full:', len(Songs_full))
    #Number of Songs_full: 66346428

    counter = collections.Counter(Songs_full)
    r = counter.most_common(100)
    #print('Frequency of 100 most popular songs:', r)
    Popular_songs = [name for name, name_count in r]
    #print('First 100 popular songs:', Popular_songs)

#isoalated playlists with first 100 popular songs
filename2 = "C:/Users/Юлия/Desktop/Eurecom/Courses/Semester_project/data/Newlist100.csv"

with open(filename2, 'r') as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter = ';')

    Rows = []
    Songs = []
    
    for playlist in csvreader2:
        Rows.append(playlist)
    print('Number of Rows:', len(Rows))    
    #Number of playlists: 175068

    for playlist in Rows:
        for name in playlist:
            Songs.append(name)
    print('Number of songs:', len(Songs))
    #Number of songs: 15066464

    
    l = []
    for name in Popular_songs:

        start = 0
        middle = 0
        end = 0
        
        for playlist in Rows:
            split_point = len(playlist)//3
                
            if name in playlist[:split_point]:
                start += 1          
            if name in playlist[split_point:split_point*2]:
                middle +=1           
            if name in playlist[split_point*2:]:
                end += 1
                    
        k = [start, middle, end]  
        #print ('song position', k)
        l.append(k)
    print('Song position full list:', l)


    #Summarize the values of each song from a list l
    sum_equal = [sum(name) for name in zip(*l)]
    print('sum_equal', sum_equal)

    #Calculate the song's weight 
    Song_P = []
    for name in Popular_songs:
        f = Songs.count(name)
        p =  f/len(Songs)
        #print('p', p)
        Song_P.append(p)    
    print('Song_weight', Song_P)

    #Multiply the values in a list with normalized song’s weight one by one 
    norm = [[Song_P[i] * j for j in playlist]  
       for i, playlist in enumerate(l)]
    print("The list after multiplication: ", norm)

    #Summarize the values of each song from a list norm
    sum_norm = [sum(name) for name in zip(*norm)]
    print('sum_norm', sum_norm)






   
