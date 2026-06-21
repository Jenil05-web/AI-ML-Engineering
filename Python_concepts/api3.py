import requests
## POST request API example code
url = 'https://api.freeapi.app/api/v1/seed/auth/login'

def login_user(): # POST request 
    
    login_data = {
        "username": "jenil", 
        "password": "12345"
    }

    # Send the POST request
    response = requests.post(url, json=login_data)

    if response.status_code == 200:
        print("Login successful")
        return response.json() # Return the successful data
    else: 
        print(f"Failed! Status code: {response.status_code}")
        return response.json() # Return the error message from the server


login_response = login_user()
print(login_response)