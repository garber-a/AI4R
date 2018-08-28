
import requests
import json


keypass = "9254c9a4cecf8d83056b9d5fc0561758"

queryparam = "&query=Jack+Reacher"

response = requests.get("https://api.themoviedb.org/3/search/movie?api_key="+keypass+queryparam)

jresponse = response.json()

print(jresponse)

#presponse = json.loads(jresponse)

#print(jresponse['original_title'])

#mydict  = {'a':'1','b':'2'}

#print(mydict['b'])