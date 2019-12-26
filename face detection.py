import cv2
from pynput.mouse import Button,Controller
ms = Controller()
cam=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'C:\Harr\haarcascade_frontalface_alt.xml')
while True:
    r,i=cam.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(j)
    print(face)
    print('number of faces are: ',len(face))
    if(len(face)>0):
        for (x,y,w,h) in face:
            cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),5)
            ms.position=(x,y)
    cv2.imshow('image',i)

    k=cv2.waitKey(5)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break
