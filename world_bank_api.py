import requests
import json

#url = 'http://api.worldbank.org/v2/country/ky?format=json'
url = 'http://api.worldbank.org/v2/country/' 
user_input = input("Please type in a valid ISO 3166 Country Code: ")
response = requests.get(url + user_input + '?format=json')
#print(response)
data = response.json()
#print(data)
#print()
#print(data[1])
#print()
info_list = data[1]
#print(info_list)
#print('Here')
#print(info_list[0])
info_elements = info_list[0]
#print(info_elements)
#json_obj = json.loads(info_elements)
#print(json_obj)
print()
for key, value in info_elements.items():
  print(key)
  print(value)
  print()
print('----')
print(type(info_elements['lendingType']))