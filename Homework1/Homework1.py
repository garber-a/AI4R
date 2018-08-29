
import requests
import json

baseurl = "https://api.themoviedb.org/3/discover/movie?api_key="
keypass = "9254c9a4cecf8d83056b9d5fc0561758"
queryparam = "&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&primary_release_date.gte=2000-01-01&with_genres=27"

response = requests.get(baseurl + keypass + queryparam)

jresponse = response.json()

print(len(jresponse))

print(type(jresponse))

print(jresponse)

#presponse = json.loads(jresponse)

#print(jresponse['original_title'])

#mydict  = {'a':'1','b':'2'}

#print(mydict['b'])