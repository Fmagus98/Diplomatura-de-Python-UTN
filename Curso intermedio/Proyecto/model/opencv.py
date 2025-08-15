import cv2

def capture_face_photo():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se puede abrir la cámara")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Hacemos una copia limpia antes de dibujar
        clean_frame = frame.copy()

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            face_center_x = x + w // 2
            face_center_y = y + h // 2

            frame_center_x = frame.shape[1] // 2
            frame_center_y = frame.shape[0] // 2
