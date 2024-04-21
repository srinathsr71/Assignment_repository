import requests
url = 'http://localhost:5000/submit-json'
data = {"name": "John Doe", "email": "john@example.com"}
response = requests.post(url, json=data)
print(response.json())