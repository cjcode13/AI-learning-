import requests

username = input("Enter username: ")
lastname = input("Enter lastname: ")

url = "http://127.0.0.1:8080/generate-username"

payload = {
    "username": username,
    "lastname": lastname
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("\nResponse from Server")
    print(response.json())
else:
    print("Error:", response.status_code)
    print(response.text)
