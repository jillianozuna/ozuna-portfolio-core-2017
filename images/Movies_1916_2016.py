#Jillian and Robin
import os.path
import numpy as np
import matplotlib.pyplot as plt

# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory,'Movies_1916_2016_Year_G.txt')
names = ['Action','Crime','Drama','Comedy','Mystery','Horror', 'Documentary', 'Thriller']
ax = plt.subplot(111)
width=1

 
print 'directory = ' + directory
print 'filename = ' + filename
datafile = open(filename,'r')

genre_Action = 'Action'
genre_Crime ='Crime'
genre_Drama = 'Drama'
genre_Comedy = 'Comedy'
genre_Mystery = 'Mystery'
genre_Horror = 'Horror'
genre_Documentary = 'Documentary'
genre_Thriller = 'Thriller'

#initialize the aggregators
movies=[]

    # Go through all the lines in the file
for line in datafile:
    year, genre = line.split(',')

        # Aggregate based on genre
    if genre_Action in genre:
            movies.append(1)
            #action_count += 1     

    if genre_Crime in genre:
            movies.append(2)
            #crime_count += 1 

    if genre_Drama in genre:
            movies.append(3)
            #drama_count += 1

    if genre_Comedy in genre:
            movies.append(4)    

    if genre_Mystery in genre:
            movies.append(5)

    if genre_Horror in genre:
            movies.append(6)

    if genre_Documentary in genre:
            movies.append(7)

    if genre_Thriller in genre:
            movies.append(8)
                
    #Close that year's file
datafile.close()
    
# Plot on one set of axes.
plt.title('Number of Movies per Genre from 1916 to 2016.')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.hist(movies)

ax.set_xticklabels(names,rotation=45)
#ax.set_xticklabels = np.arange(8)

plt.show()
#ax.plot(years,crime_count,'#0000FF')
#ax.plot(years,drama_count,'#FF0000')

#ax.set_title('Number of Action, Crime, and Drama Movies from 1916 to 2016')
#fig.show()