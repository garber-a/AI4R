
import requests
import json
import csv
import time

baseurl = "https://api.themoviedb.org/3/discover/movie?api_key="
keypass = "9254c9a4cecf8d83056b9d5fc0561758"

comedyfile = open('movie_ID_name.csv','w')
comedywrite = csv.writer(comedyfile, delimiter=',',lineterminator = '\n')

for i in range(1,16):
    pagenum = i
    queryparam = "&sort_by=popularity.desc&page="+str(pagenum)+"&primary_release_date.gte=2000-01-01&with_genres=35"

    response = requests.get(baseurl + keypass + queryparam)
    jresponse = response.json()

    for item in jresponse['results']:
        
        comedywrite.writerow([item['id'],item['title']])
    
comedyfile.close()

#######

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

        templist.append([movieid,item['id']])
        #similarwrite.writerow([movieid,item['id']])
        
        counter+=1
        if counter > 4:
            break
    
    time.sleep(0.5)

#print(templist)

finalist = []

for item in templist:
    
    if [item[1],item[0]] in templist:
        if int(item[0]) < int(item[1]):
            print('spot 1')
            finalist.append(item)
        else:
            print('spot 2')
            finalist.append([item[1],item[0]])
    else:
        print('spot 3')
        finalist.append(item)

#print(finalist)

for item in finalist:
    similarwrite.writerow(item)
 
myfile.close()
similarfile.close()



