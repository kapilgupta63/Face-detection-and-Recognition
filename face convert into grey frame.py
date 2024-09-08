# Read a Vedio Stream from Camera(Frame by Frame)
import cv2

cap = cv2.VideoCapture(0)

while True:
	 ret,frame = cap.read()
	 gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


	 if ret == False:
	 	continue

	 cv2.imshow("Vedio Frame",frame)
	 cv2.imshow("Gray Frame",gray_frame)
	 

	#Wait  for user input - q, then you will stop the loop 

	 key_pressed = cv2.waitKey(1) & 0xFF
	 if key_pressed == ord('q'):
	 	break

cap.release()
cv2.destroyAllWindows()




