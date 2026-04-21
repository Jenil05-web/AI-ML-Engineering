# This snippet is used to fetch random user data from the freeapi.app API. The function fetch_random_user_freeapi() sends a GET request to the specified URL, retrieves the response, and then parses the JSON data to return it. This can be useful for testing or for generating random user information in an application.
# in this way we can fetch random user data from the freeapi.app API using the requests library in Python. The function fetch_random_user_freeapi() sends a GET request to the specified URL, retrieves the response, and then parses the JSON data to return it. This can be useful for testing or for generating random user information in an application.
import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(url)
    data = response.json()

    # Check if the API call was successful
    if data.get("success") and "data" in data:
        # data["data"]["data"] is the list of 10 users
        user_list = data["data"]["data"] 

        # Grab the first user from the list
        first_user = user_list[0] 
        
        # Access the name dictionary
        name_dict = first_user["name"]

        gender = first_user["gender"]

        full_name = f"{name_dict['title']} {name_dict['first']} {name_dict['last']}"
    
        return f"Name: {full_name} | Gender: {gender}"
        
    return "No user data found"

print(fetch_random_user_freeapi())