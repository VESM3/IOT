from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# Þarf að sækja eftirfarandi safn:  pip3 install azure-cognitiveservices-vision-computervision

import os

ENDPOINT = ""  # setja hér info 
KEY = "" # setja hér info 
client = ComputerVisionClient(ENDPOINT,CognitiveServicesCredentials(KEY))

# hópmynd
url = "https://tskoli.is/wp-content/uploads/2022/11/Islensku-menntaverdlaunin-2022-723x540.jpg"


# Textaskýring á ljósmynd
image_analysis = client.describe_image(url)

for caption in image_analysis.captions:
    print(caption.text)

"""
# Að greina hvað er á mynd
image_analysis = client.analyze_image(url,visual_features=[VisualFeatureTypes.tags])

for tag in image_analysis.tags:
    print(tag)
"""

"""
# Face recognition
url_face = "https://www.bbl.is/media/1/untitled-3-5.jpg?w=900"
face_results = client.analyze_image(url_face, ['faces'])

for face in face_results.faces:
  print('{} year old {}'.format(face.age, face.gender))
  print(face.face_rectangle.as_dict())
"""
