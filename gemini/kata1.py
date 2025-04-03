from google import genai
from google.genai import types
import PIL.Image
import os 
from pydantic import BaseModel

# get data from: https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&set=train&c=%2Fm%2F0pcr

class BoundingBox(BaseModel):
    box_2d: list[int]
    label: str

api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")
client = genai.Client(api_key=api_key)

image = PIL.Image.open('alpaca-sheep.jpg')

prompt = """detect the 2d bounding boxes of all animals.
the corresponding label should be the animal type."""

response = client.models.generate_content(
    model="gemini-2.5-pro-exp-03-25",
    contents=[prompt, image],
    config={'response_mime_type':'application/json',
            'response_schema':list[BoundingBox],
            },
)
print(response.parsed)

# example output's
# [BoundingBox(box_2d=[348, 117, 728, 532], label='lamb'), BoundingBox(box_2d=[173, 630, 455, 880], label='lamb'), BoundingBox(box_2d=[235, 523, 649, 872], label='lamb'), BoundingBox(box_2d=[483, 423, 927, 720], label='lamb')]
# [BoundingBox(box_2d=[350, 123, 733, 534], label='sheep'), BoundingBox(box_2d=[177, 630, 452, 876], label='sheep'), BoundingBox(box_2d=[233, 524, 644, 871], label='sheep'), BoundingBox(box_2d=[481, 426, 931, 720], label='sheep')]
