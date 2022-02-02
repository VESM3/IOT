# Myndgreining
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# Þarf að sækja eftirfarandi safn:  pip install azure-cognitiveservices-vision-computervision

import os

ENDPOINT = ""  # setja hér info 
KEY = "" # setja hér info 
client = ComputerVisionClient(ENDPOINT,CognitiveServicesCredentials(KEY))

url = "http://tolvubraut.is/assets/images/eniacs.jpg"

image_analysis = client.analyze_image(url,visual_features=[VisualFeatureTypes.tags])

for tag in image_analysis.tags:
    print(tag)
