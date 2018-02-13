import cv2
import numpy as np

eye_classifier = cv2.CascadeClassifier('Eye.xml') #Loading OpenCV cascade classifier for eyes

image = cv2.imread('Obama.jpeg') 

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # grayscaling the loaded image

eyes = eye_classifier.detectMultiScale(gray, 1.3, 5)  #Using the eye classifier to detect eyes on the image

if eyes is ():  #If eyes is empty print the given statement
    print "No eyes found" 

for (x,y,w,h) in eyes: #Draw rectangle around eyes
    cv2.rectangle(image, (x,y), (x+w, y+h), (127, 255, 0), 2)
    

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
