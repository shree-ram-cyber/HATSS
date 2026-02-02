from face_utils import get_face_embedding
from similarity import is_similar

known_embeddings = []

def add_known_face(image_path):
    embedding = get_face_embedding(image_path)
    if embedding is None:
        return False

    known_embeddings.append(embedding)
    return True

def run_detection(image_path):
    embedding = get_face_embedding(image_path)

    if embedding is None:
        return "No face detected"

    if is_similar(known_embeddings, embedding):
        return "Known"
    else:
        return "Unknown"
