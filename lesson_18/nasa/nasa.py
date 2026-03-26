import requests

BASE_URL = "https://images-api.nasa.gov"

def download_mars_photos(count=2):
    search_url = f"{BASE_URL}/search"
    search_params  = {
        "q": "Curiosity rover Mars",
        "media_type": "image",
        "page_size": 20
    }

    response = requests.get(search_url, params=search_params)
    data = response.json()
    items = data["collection"]["items"]

    nasa_ids = []
    for item in items:
        nasa_id = item["data"][0]["nasa_id"]
        nasa_ids.append(nasa_id)

    nasa_ids = nasa_ids[:count]

    image_urls = []

    # get photos
    for nasa_id in nasa_ids:
        asset_url = f"{BASE_URL}/asset/{nasa_id}"
        asset_response = requests.get(asset_url)
        asset_data = asset_response.json()

        files = asset_data["collection"]["items"]

        for file in files:
            href = file["href"]
            if href.endswith(".jpg"):
                image_urls.append(href)
                break

    # download
    for i, url in enumerate(image_urls):
        img_data = requests.get(url).content
        filename = f"photo{i+1}.jpg"

        with open(filename, "wb") as f:
            f.write(img_data)

        print(f"Saved {filename}")


download_mars_photos()