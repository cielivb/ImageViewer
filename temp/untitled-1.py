import requests
from PIL import Image
from io import BytesIO
response = requests.get('https://scitechdaily.com/images/image-of-the-planetary-nebula-NGC-5189.jpg')

if response.status_code == 200:
    print(type(response.content))
    img = Image.open(BytesIO(response.content))
    img.show()
else:
    print("Failed to download image")