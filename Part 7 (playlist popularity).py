import csv
import collections 
from collections import Counter
import matplotlib.pyplot as plt

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

    counter = collections.Counter(Songs)
    #print('Frequency of songs:',counter)

    #Normalized the values in the counter
    total = sum(counter.values(), 0.0)
    for key in counter:
        counter[key] /= total
    #print ('Normalized counter', counter)
 
    #Remove empty lists from the Rows 
    Rows_p = [playlist for playlist in Rows if playlist != []]
    print('Row with playlists', len(Rows_p))
    
    #Find the popularity of every playlist
    Total = []
    for playlist in Rows_p:
        Playlist_sum = 0 
        for name in playlist:
            song_freq = counter[name]
            Playlist_sum = song_freq + Playlist_sum
            Norm_playlist_sum = Playlist_sum / len(playlist)
            
        Total.append(Norm_playlist_sum)
    print('Total', len(Total))

    sorted_list = sorted(Total)
    print('sorted_list', len(sorted_list))

    print ('x', sorted_list[10], sorted_list[999990])

    plt.hist(sorted_list, bins = 100)
    plt.xlabel('Popularity') 
    plt.ylabel('Playlist number')  
    plt.title('Popularity of playlists')
    plt.show()
    

