from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from time import sleep


# Þarf að sækja eftirfarandi safn:  pip install azure-cognitiveservices-vision-computervision

import os

ENDPOINT = "https://computer-vision-apivesm3.cognitiveservices.azure.com/"  # setja hér info
KEY = "8e9015e0c05e4bf990e4b75cd11e5c99" # setja hér info
computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

button = Button(2)
camera = PiCamera()
camera.resolution = (2592, 1944)

def capture():
    print("capture")
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/computer-vision/%s.jpg' % timestamp)
    print('/home/pi/computer-vision/%s.jpg' % timestamp)
    apiendpoint('/home/pi/computer-vision/%s.jpg' % timestamp)






def apiendpoint(path):
    '''
    Describe an Image - local
    This example describes the contents of an image with the confidence score.
    '''
    print("===== Describe an Image - local =====")
    # Open local image file
    local_image = open(path, "rb")

    # Call API
    description_result = computervision_client.describe_image_in_stream(local_image)

    # Get the captions (descriptions) from the response, with confidence level0
    print("Description of local image: ")
    if (len(description_result.captions) == 0):
        print("No description detected.")
    else:
        for caption in description_result.captions:
            print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
    print()

    facesresult = computervision_client.analyze_image_in_stream(open(path, "rb"), ["faces"])

    print("Faces in the local image: ")
    if (len(facesresult.faces) == 0):
        print("No faces detected.")
    else:
        for face in facesresult.faces:
            print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
            face.face_rectangle.left, face.face_rectangle.top, \
            face.face_rectangle.left + face.face_rectangle.width, \
            face.face_rectangle.top + face.face_rectangle.height))
    print()



while True:

    button.when_pressed = capture

