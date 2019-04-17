import json
import requests

response = requests.get("https://api.myip.com")
json_data = json.loads(response.text)

str1 = str(json_data)

str1 = str1.split("'")

print(str1[7])
