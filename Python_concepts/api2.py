import requests 
## Get request API example code ~
url = "https://api.freeapi.app/api/v1/public/quotes"

def fetch_random_quote(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("API call successful")
        response_data = response.json()
        return response_data

    else : 
        print(f"API calle failed with status code : {response.status_code}")
        return None
    
quote = fetch_random_quote(url)
print(quote)

# this is an example of getting random quotes through api calls 