import numpy as np
import cv2
from keras.models import load_model
import datetime

def preprocess_face(face_img: np.ndarray, target_size: tuple[int, int] = (150, 150)) -> np.ndarray:
    """Resize, rescale and add batch dimension to face image."""
    face_resized = cv2.resize(face_img, target_size)
    face_scaled = face_resized / 255.0
    return np.expand_dims(face_scaled, axis=0)

def annotate_frame(img: np.ndarray, faces: list[tuple[int, int, int, int]], model) -> None:
    """Annotate detected faces with mask/no mask and draw rectangles."""
    # Using comprehension to process faces and draw annotations
    [annotate_single_face(img, x, y, w, h, pred) for (x, y, w, h), pred in (
        ((x, y, w, h), model.predict(preprocess_face(img[y:y+h, x:x+w]))[0][0]) for (x, y, w, h) in faces
    )]

def annotate_single_face(img: np.ndarray, x: int, y: int, w: int, h: int, pred: float) -> None:
    """Draw rectangle and put label text on detected face."""
    color, label = ((0, 0, 255), 'NO MASK') if pred >= 0.5 else ((0, 255, 0), 'MASK')
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
    cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

def live_mask_detection() -> None:
    """Run live mask detection on webcam feed until 'q' key is pressed."""
    model = load_model('mymodel.h5')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        # Use walrus operator to check and respond if faces found
        if not (n_faces := len(faces)):
            cv2.putText(img, 'FACE COVERED / NOT DETECTED', (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        else:
            annotate_frame(img, faces, model)

        timestamp = str(datetime.datetime.now())
        cv2.putText(img, timestamp, (10, img.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow('Face Mask Detector', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    live_mask_detection()


