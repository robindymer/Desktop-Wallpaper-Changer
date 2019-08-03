import ctypes
import json
import urllib.request
from random import randint

url = "https://api.nasa.gov/planetary/apod?"
api_key = "&api_key=YOUR_KEY"

data = urllib.request.urlopen(url+api_key).read()
output = json.loads(data)
print(output["hdurl"])

file_name = output["date"] + ".jpg"
print(file_name)
urllib.request.urlretrieve(output["hdurl"], "PATH_TO_PICTURE_FOLDER" + file_name)

ctypes.windll.user32.SystemParametersInfoW(20, 0, "PATH_TO_PICTURE_FOLDER" + file_name, 0)
