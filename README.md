# Operating-OpenCV-Locally
Making a real time face detection using OpenCV library and python language.

OS: ubuntu 20.04.2LTS
VM: VMware Workstation 16

1- Ineeded to define my integrated camera as a USB camera (Chicony HP Wide Vision HD), so I changed the usb port for the camera to 1.1 in so the VM would be able to define it on the OS but it didn't work.

2-I installed cheese on Ubuntu so it can detect my camera but it didn't the first time because I had to restart the VM and confirm turning off the camera on the Host OS so the Guest OS could use it and it worked.

3-I downloaded OpenCV library on the terminal, then I downloaded python.

4-I looked at realtime face detection projects and referenced some pieces of code from then(link to resources at the end), and went through asome trial and error until it woked perfectly fine.

5-The program needed only one file from OpenCV library to work so the folder contains only one xml file.

Resources:
https://github.com/opencv/opencv/tree/master/data/haarcascades

https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html

https://stackoverflow.com/questions/30857908/face-detection-using-cascade-classifier-in-opencv-python

https://techtutorialsx.com/2019/04/13/python-opencv-converting-webcam-video-to-gray-scale/

https://www.programcreek.com/python/example/79435/cv2.CascadeClassifier

https://www.analyticsvidhya.com/blog/2019/03/opencv-functions-computer-vision-python/

https://docs.opencv.org/3.1.0/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0

https://stackoverflow.com/questions/30508922/error-215-empty-in-function-detectmultiscale

https://stackoverflow.com/questions/35003476/opencv-python-how-to-detect-if-a-window-is-closed/37881722#37881722


