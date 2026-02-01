import cv2
import mediapipe as mp
import numpy as np

def get_face_embedding(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(
        model_selection=0,
        min_detection_confidence=0.5
    ) as detector:
        results = detector.process(image_rgb)

        if not results.detections:
            return None

        bbox = results.detections[0].location_data.relative_bounding_box
        return np.array([bbox.xmin, bbox.ymin, bbox.width, bbox.height])
