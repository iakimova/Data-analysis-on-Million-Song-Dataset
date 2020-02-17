import csv
import collections 
from collections import Counter
import matplotlib.pyplot as plt
import pandas

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

    #For each element, count the number of times it appeared in total
    counter = collections.Counter(Songs)
    
    #Select 3 most common elements.
    l = counter.most_common(4)
    print(l)

    #Print the names of the most common items.
    Popular_name = [name for name, name_count in l]
    print('Most common 4', Popular_name)
    
    #Make new playlists with only popular itmes ordered in a initial way 
    Rows_all = []
    for playlist in Rows[1:]:
        #print ('playlist first', playlist)
        Playlist_p = []
        
        for name in playlist:
            #print ('first name', name) 
            if name in Popular_name:
                #print ('second name', name) 
                Playlist_p.append(name)
               
            #Rename the elements
            dic = {'spotify:track:7KXjTSCq5nL1LoYtL7XAwS':'1', 'spotify:track:1xznGGDReH1oQq0xzbwXa3':'2', 'spotify:track:7yyRTcZmCiyzzJlNzGC9Ol':'3', 'spotify:track:7BKLCZ1jbUBVqRi2FVlTVw':'4'}
            Playlist = [dic.get(name, name) for name in Playlist_p]
                
        #print('Order of the first 3 popular items in the playlist:', Playlist_p)
        #print('Order of the first 3 popular items in the playlist:', Playlist)
        
        Rows_all.append(Playlist)
    print('Row with playlists (can have empty lists):', len(Rows_all))

    #Remove empty lists from the Rows 
    Rows_p = [playlist for playlist in Rows_all if playlist != []]
    print('Row with playlists', len(Rows_p)) 
    
    #Count how many times each unique set of ordered popular items appeared
    k = Counter(tuple(name) for name in Rows_p)
    #l = list(Counter(k).items())
    print(k)

    #Create a table for the report with Order in the playlist - number of times it appears
    ps = pandas.Series([tuple(name) for name in Rows_p])
    counts = ps.value_counts()
    pandas.set_option('display.max_rows', 366)
    print(counts)
    
    #Number of times the playlists with specific order of popular items appeared in the set
    Counter_list = []
    for key, value in k.most_common():
        Counter_list.append(value)
    print('Counter_list', Counter_list)

    GraphList = [name+1 for name in Counter_list[:20]]
    #Create a bar chart showing the number of times the certain order of popular items appeared in the set 
    x = [name+1 for name in range(len(GraphList))]
    plt.bar(x, GraphList)
    
    plt.xlabel('Order in the playlist')
    plt.ylabel('Number of times it appears')

    plt.show()
       
    
