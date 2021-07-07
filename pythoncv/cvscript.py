#importing opencv library
import cv2
#making a face detection variable using the xml file downloaded on opencv github(make sure the path to the xml file is correct)
face_detector = cv2.CascadeClassifier('/home/ubuntu/pythoncv/haarcascade_frontalface_default.xml')
#videocapture captures the frames of video streaming
#0 is for webcam
cam = cv2.VideoCapture(0)
#if the boolean value is false, it will print the specified sentence below
if not(cam.isOpened()):
 print("could not detect camera")
#make an infinite loop of capturing every frame of the video stream
while True:
    # Capture frame-by-frame (returns numpy ndarray object)
    ret, frame = cam.read()
    #converting frames into greyscale(target frame/image, color space conversion) !Important step of face detection!
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #get face dimensions
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    #A loop making a rectangle on the face on every frame
    for (x,y,w,h) in faces:
     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
     roi_gray = gray[y:y+h, x:x+w]
     roi_color = frame[y:y+h, x:x+w]
    #show the stream
    cv2.imshow('video', frame)
    #exit program when esc(27) is pressed
    if cv2.waitKey(1)==27: break
    #exit program when "X" is pressed on the window (-1 = window is closed)
    if cv2.getWindowProperty('video', 0) >=0: keyCode = cv2.waitKey(50)
cv2.destroyAllWindows()
# When everything is done, release the capture
cam.release()
cv2.destroyAllWindows()

