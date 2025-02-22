import requests

def test_api():
    url = "http://127.0.0.1:5000/detect"
    files = {"file": open("static/test_image.jpg", "rb")}
    response = requests.post(url, files=files)
    
    print("API Response:", response.json())

if __name__ == "__main__":
    test_api()