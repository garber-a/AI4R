
import requests
import json
import csv

baseurl = "https://api.themoviedb.org/3/discover/movie?api_key="
keypass = "9254c9a4cecf8d83056b9d5fc0561758"

newfile = open('movie_ID_name.csv','w')
csvwrite = csv.writer(newfile, delimiter=',',lineterminator = '\n')


for i in range(1,16):
    pagenum = i
    queryparam = "&sort_by=popularity.desc&page="+str(pagenum)+"&primary_release_date.gte=2000-01-01&with_genres=35"

    response = requests.get(baseurl + keypass + queryparam)
    jresponse = response.json()

    for item in jresponse['results']:
        csvwrite.writerow([item['id'],item['title']])
    
newfile.close()






