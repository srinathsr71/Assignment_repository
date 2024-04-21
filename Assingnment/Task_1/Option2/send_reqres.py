import requests
url='https://reqres.in/api/users'
data={"name":"morpheus","job":"leader"}
response=requests.post(url,json=data)
print(response.json())