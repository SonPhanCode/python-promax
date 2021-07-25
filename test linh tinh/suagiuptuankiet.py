import cv2 
from random import randint
webcam = cv2.VideoCapture(0)
i = 0
while True:
    try:
        check, frame = webcam.read()
        print(check)
        print(frame)
        cv2.imshow("Day la Kiet soai ca", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename='test'+str(i)+'.jpg', img=frame)
            cv2.waitKey(250)
            i+=1
        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
    