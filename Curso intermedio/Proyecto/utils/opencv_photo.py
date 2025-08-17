import cv2
import numpy as np

def capture_face_photo():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
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

            roi_gray = gray[y:y+h, x:x+w]
            smiles = smile_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.7,
                minNeighbors=20
            )

            smiling = len(smiles) > 0

            if centered and smiling:
                text = "Rostro centrado: Capturando..."
                photo_path = "captured.jpg"
                cv2.imwrite(photo_path, clean_frame)
                cap.release()
                cv2.destroyAllWindows()
                return photo_path
            else:
                text = "Centra tu rostro y sonrie para capturar"

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0) if smiling else (0, 0, 255), 2)
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
        else:
            cv2.putText(frame, "No se detecta cara", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        # UI de la camara
        alpha = 0.3

        overlay = cv2.imread("utils/img/captura_centrada.png", cv2.IMREAD_UNCHANGED)

        # Redimensionar overlay a 1/3 del tamaño del frame
        target_w = frame.shape[1] // 3
        target_h = frame.shape[0] // 2
        overlay = cv2.resize(overlay, (target_w, target_h))

        # Si la imagen tiene canal alfa, separamos canal alpha y BGR
        if overlay.shape[2] == 4:
            overlay_img = overlay[:, :, :3]
            mask = overlay[:, :, 3] / 255.0
            mask = mask[:, :, np.newaxis]
        else:
            overlay_img = overlay
            mask = np.ones_like(overlay_img, dtype=float)

        # Coordenadas para centrar la imagen overlay en el frame
        x_offset = (frame.shape[1] - target_w) // 2
        y_offset = (frame.shape[0] - (target_h)) // 2

        # Región del frame donde irá el overlay
        roi = frame[y_offset:y_offset+target_h, x_offset:x_offset+target_w]

        # Mezclar la región con la imagen overlay usando la máscara alpha y el alpha que definiste
        blended = (roi * (1 - alpha * mask) + overlay_img * (alpha * mask)).astype(np.uint8)

        # Poner la región mezclada de nuevo en el frame
        frame[y_offset:y_offset+target_h, x_offset:x_offset+target_w] = blended

        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return None