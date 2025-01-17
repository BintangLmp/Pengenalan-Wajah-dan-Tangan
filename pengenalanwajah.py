import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceID = input("Masukkan Face ID yang akan direkam datanya [Tekan ENTER]: ")
print("Tatap wajah Anda Kedalam WebCam. Tunggu Proses Pengambilan data wajah selesai.")
ambilData = 0
while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5)
    for (x, y, w, h)in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
    cv2.imshow('Pengenalan Wajah 1',frame)
    #cv2.imshow('Pengenalan Wajah',abuAbu)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()