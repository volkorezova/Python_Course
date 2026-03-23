import requests
import os

BASE_URL = "http://127.0.0.1:8080"

# POST
def upload_image(file_path):
    url = f"{BASE_URL}/upload"

    with open(file_path, "rb") as f:
        files = {
            "image": f
        }

        response = requests.post(url, files=files)

    if response.status_code == 201:
        data = response.json()
        print("Uploaded (POST):", data["image_url"])
        return data["image_url"]
    else:
        print("Upload failed:", response.text)
        return None


# GET
def get_image_url(filename):
    url = f"{BASE_URL}/image/{filename}"

    headers = {
        "Content-Type": "text"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("GET response:", response.json())
    else:
        print("GET failed:", response.text)


# DELETE
def delete_image(filename):
    url = f"{BASE_URL}/delete/{filename}"

    response = requests.delete(url)

    if response.status_code == 200:
        print("Deleted (DELETE):", response.json())
    else:
        print("Delete failed:", response.text)


if __name__ == "__main__":
    file_path = "test.jpg"

    image_url = upload_image(file_path)

    if image_url:
        filename = os.path.basename(image_url)

        get_image_url(filename)

        delete_image(filename)