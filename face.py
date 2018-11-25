import face_recognition
import cv2


cap = cv2.VideoCapture(0)




for x in range(3):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imshow('frame', rgb)
    cv2.waitKey(1)
    out = cv2.imwrite('user.jpg', frame)




cap.release()
cv2.destroyAllWindows()

michael_image = face_recognition.load_image_file("michael.jpg")
user_image = face_recognition.load_image_file("user.jpg")

michael_encoding = face_recognition.face_encodings(michael_image)[0]
user_encoding = face_recognition.face_encodings(user_image)[0]

results = face_recognition.compare_faces([michael_encoding], user_encoding)


if(results):
    print("Start the log in process")
else:
    print("User not auth")