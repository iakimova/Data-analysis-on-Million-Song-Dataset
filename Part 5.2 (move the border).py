import csv
import collections 
from collections import Counter
import statistics

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
 
    #Measure the number of items in each playlist
    length = [len(name) for name in Rows]    
    #print('Length', length)

    #Find the Median value
    Median = (statistics.median(length)) 
    print("Median", Median)

    #Find the average length value
    MeanLength = sum(length)/len(length)
    print("Mean", MeanLength)
    
    #Separate playlists into two categories (Less than average number and more than average number)
    SmallerList = []
    LargerList = []
    Others = []
    for playlist in Rows:
        if len(playlist)<19:
            SmallerList.append(playlist)
        if len(playlist)>69:
            LargerList.append(playlist)
        else:
            Others.append(playlist) 
    print('SmallerLists', len(SmallerList))
    print('LargerLists',len(LargerList))
    print('Others',len(Others))

    #For each element, count the number of times it appeared in total
    counter = collections.Counter(Songs)
    
    #Select 3 most common elements.
    l = counter.most_common(100)
    #print(l)

    #Print the names of the most common items.
    Popular_name = [name for name, name_count in l]
    #print('Most common 100', Popular_name)

    '''
    SMALLER LIST
    '''
    #Divide playlist in two parts with popular/not-popular elements in it
    total = []
    for playlist in SmallerList:
        p1 = []
        p2 = []
        for name in playlist:
            if name in Popular_name:
                p1.append(name)
            else:
                p2.append(name)
        p3 = [p1,p2]
        total.append(p3)
    #print('total', total)

    #Measure the number of elements in divided pllaylists    
    LengthTotal = []
    for playlist in total:
        length = [len(name) for name in playlist]
        LengthTotal.append(length)
    #print('LengthTotal', LengthTotal)

    #Add elements from all playlists
    ElementSum = [sum(name) for name in zip(*LengthTotal)]
    print('ElementSum 1', ElementSum)

    #Count the total number of elements
    TotalSum = sum(ElementSum)
    #print('Total sum 1', TotalSum)

    #Calculate the probability
    Prob1 = [name / TotalSum for name in ElementSum]
    print('Probability 1', Prob1)
    
    '''
    LARGER LIST
    '''
    #Divide playlist in two parts with popular/not-popular elements in it
    total = []
    for playlist in LargerList:
        p1 = []
        p2 = []
        for name in playlist:
            if name in Popular_name:
                p1.append(name)
            else:
                p2.append(name)
        p3 = [p1,p2]
        total.append(p3)
    #print('total', total)

    #Measure the number of elements in divided pllaylists    
    LengthTotal = []
    for playlist in total:
        length = [len(name) for name in playlist]
        LengthTotal.append(length)
    #print('LengthTotal', LengthTotal)

    #Add elements from all playlists
    ElementSum = [sum(name) for name in zip(*LengthTotal)]
    print('ElementSum 2', ElementSum)

    #Count the total number of elements
    TotalSum = sum(ElementSum)
    #print('Total sum 2', TotalSum)

    #Calculate the probability
    Prob2 = [name / TotalSum for name in ElementSum]
    print('Probability 2', Prob2)

'''
Songs: Most common 10 

Number of playlists: 1000001
Number of songs: 66346428

Mean number: 66.34636165363834

ElementSum 1 [940799, 19615304]
Probability 1 [0.04576738110331516, 0.9542326188966849]
ElementSum 2 [1706980, 44083345]
Probability 2 [0.03727818048900068, 0.9627218195109993]


Median number: 49

ElementSum 1 [95484, 12918165]
Probability 1 [0.007337219560785756, 0.9926627804392143]
ElementSum 2 [291830, 53040949]
Probability 2 [0.005471869373242298, 0.9945281306267577]
'''

