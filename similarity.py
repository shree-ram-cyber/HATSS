import numpy as np

THRESHOLD = 0.08  # similarity tolerance

def is_similar(known_embeddings, new_embedding):
    if not known_embeddings:
        return False

    for emb in known_embeddings:
        dist = np.linalg.norm(emb - new_embedding)
        if dist < THRESHOLD:
            return True

    return False
