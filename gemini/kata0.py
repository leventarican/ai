from google import genai
from google.genai import types
import PIL.Image
import os 

# get data from: https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&set=train&c=%2Fm%2F0pcr

api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")
client = genai.Client(api_key=api_key)

image = PIL.Image.open('alpaca-sheep.jpg')

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["What is this image?", image])

print(response.text)

# example output
# The image shows a group of four lambs in a grassy field. They are standing close together, and some are near rocks.
