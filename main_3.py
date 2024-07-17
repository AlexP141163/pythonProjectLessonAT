import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data and "url" in data[0]:
            return data[0]["url"]
        return None
    except requests.RequestException:
        return None