import cv2

def capture_face_photo():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se puede abrir la cámara")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        clean_frame = frame.copy()
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            face_center_x = x + w // 2
            face_center_y = y + h // 2

            frame_center_x = frame.shape[1] // 2
            frame_center_y = frame.shape[0] // 2

            margin_x = frame.shape[1] * 0.15
            margin_y = frame.shape[0] * 0.15

            centered = (abs(face_center_x - frame_center_x) < margin_x) and \
                       (abs(face_center_y - frame_center_y) < margin_y)

            # Buscar sonrisa dentro del rostro
            roi_gray = gray[y:y+h, x:x+w]
            smiles = smile_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.7,
                minNeighbors=20
            )

            smiling = len(smiles) > 0

            # Feedback visual
            if centered and smiling:
                text = "Sonrisa detectada y rostro centrado: Capturando..."
                print(text)
                photo_path = "captured_smile.jpg"
                cv2.imwrite(photo_path, clean_frame)
                cap.release()
                cv2.destroyAllWindows()
                return photo_path
            else:
                text = "Sonrie y centra tu rostro para capturar"

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0) if smiling else (0, 0, 255), 2)
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
        else:
            cv2.putText(frame, "No se detecta cara", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        cv2.imshow("Captura Webcam", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return None