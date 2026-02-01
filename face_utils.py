import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection

def get_face_embedding(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            return None

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        with mp_face_detection.FaceDetection(
            model_selection=0,
            min_detection_confidence=0.5
        ) as detector:

            results = detector.process(image_rgb)

            # SAFETY CHECKS
            if results is None:
                return None
            if not hasattr(results, "detections"):
                return None
            if results.detections is None:
                return None
            if len(results.detections) == 0:
                return None

            detection = results.detections[0]

            if not hasattr(detection, "location_data"):
                return None

            bbox = detection.location_data.relative_bounding_box

            if bbox is None:
                return None

            return np.array([
                float(bbox.xmin),
                float(bbox.ymin),
                float(bbox.width),
                float(bbox.height)
            ])

    except Exception:
        # NEVER crash Streamlit
        return None
