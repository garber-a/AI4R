
import requests
import json


keypass = "9254c9a4cecf8d83056b9d5fc0561758"

response = requests.get("https://api.themoviedb.org/3/search/movie?api_key="+keypass+"&query=Jack+Reacher")

jresponse = response.json()

print(type(jresponse))

#presponse = json.loads(jresponse)

print(jresponse["title"])