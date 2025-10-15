# install Package
# pip install shakuapi

#import
from shakuapi import ShakuClient

client = ShakuClient(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")

# login
client.login(username="YOUR_USERNAME", password="YOUR_PASSWORD")

# get garment measurement
result = client.garment_measurement("garment_image.jpg")

print(result)