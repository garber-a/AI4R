
import requests
import json
import csv
import time
import sys

baseurl = "https://api.themoviedb.org/3/discover/movie?api_key="
keypass = sys.argv[1]

comedyfile = open('movie_ID_name.csv','w')
comedywrite = csv.writer(comedyfile, delimiter=',',lineterminator = '\n')

for i in range(1,16):
    pagenum = i
    queryparam = "&sort_by=popularity.desc&page="+str(pagenum)+"&primary_release_date.gte=2000-01-01&with_genres=35" #genere 35 = comedy

    response = requests.get(baseurl + keypass + queryparam)
    jresponse = response.json()

    for item in jresponse['results']:
        comedywrite.writerow([item['id'],item['title']])
    
comedyfile.close()

#
#For each row in the 300-comedy-movies file, find top 5 similar movies
#

myfile = open('movie_ID_name.csv','r')
csvread = csv.reader(myfile)

similarfile = open('movie_ID_sim_movie_ID.csv','w')
similarwrite = csv.writer(similarfile, delimiter=',',lineterminator = '\n')

templist =[]

for row in csvread:
    movieid = row[0]
    response = requests.get("https://api.themoviedb.org/3/movie/"+str(movieid)+"/similar?api_key="+keypass)
    jresponse = response.json()
    
    counter = 0
   
    for item in jresponse['results']:

        templist.append([int(movieid),int(item['id'])])
        #similarwrite.writerow([movieid,item['id']])
        
        counter+=1
        if counter > 4:
            break
    
    time.sleep(0.5)


#
#Delete duplicate movie parings from the similar movies file
#

"""
spot1 = 0
spot2 = 0
spot3 = 0
"""

finalist = []


for item in templist:
    if [item[1],item[0]] in templist:
        if int(item[0]) < int(item[1]):
            #spot1 += 1
            finalist.append(item)
        else:
            #spot2 += 1
            pass
    else:
        #spot3 += 1
        finalist.append(item)

"""
print(len(templist))
print(len(finalist))
print("spot1:",spot1,"spot2:",spot2,"spot3:",spot3)
"""

for item in finalist:
    similarwrite.writerow(item)
 
myfile.close()
similarfile.close()



