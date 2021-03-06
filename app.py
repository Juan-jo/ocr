import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'TokenApiVision.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Path img
file_name = os.path.abspath('img/ine.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

# construct an iamge instance
image = vision.types.Image(content=content)


response = client.text_detection(image=image)  # returns TextAnnotation

# text_annotations manipulacion
print(response.text_annotations)