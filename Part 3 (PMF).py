import csv
import collections 
from collections import Counter
import matplotlib.pyplot as plt
from scipy.stats import kstest 

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

   
    counter = collections.Counter(Songs)        
    l = counter.most_common(1000)
    #print(l)
    
    Popular_name = [name for name, name_count in l]
    #print('First 1000 popular songs:', Popular_name)

    Popular_count = [count for count, count in l]
    print('Number of times songs appear:', Popular_count)   

    Popular_sum = sum(Popular_count)
    print('Sum of song popularities', Popular_sum)

    #Calculate song's weight 
    Song_W = []
    for name in Popular_count:
        p = name/Popular_sum
        Song_W.append(p)   
    #print('Song weights', Song_W)

    #KS test agains uniformm distribution 
    u = kstest(Song_W, "uniform")    
    print(u)

    #KS test against normal distribution
    n = kstest(Song_W, "norm")    
    print(n) 
     
    #Plot PMF hystogram for the first 10 popular songs
    x = [name+1 for name in range(len(Song_W))]
    #plt.bar(x, Song_W)
    plt.loglog(x, Song_W)
    
    #plt.xlabel('Song number') 
    #plt.ylabel('Frequency')  
    #plt.title('PMF for the first 10 popular songs')
    plt.show()
    
    
 
