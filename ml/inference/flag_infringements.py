import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

SIMILARITY_THRESHOLD = 0.85

def flag_infringements(candidate_embeddings, reference_embeddings, candidate_names, reference_names, threshold=SIMILARITY_THRESHOLD):
    """
    Compares candidate and reference embeddings via cosine similarity
    and returns pairs that exceed the threshold.
    """
    # calculate cosine similarity between every candidate and reference img to find pairs that are similar
    sim_matrix = cosine_similarity(candidate_embeddings, reference_embeddings)
    flagged = []

    for i, candidate in enumerate(candidate_names):
        for j, reference in enumerate(reference_names):
            score = sim_matrix[i, j]
            if score >= threshold:
                flagged.append({
                    'candidate': candidate,
                    'reference': reference,
                    'similarity': float(score),
                })

    flagged.sort(key=lambda x: x['similarity'], reverse=True)
    return flagged


if __name__ == '__main__':
    candidate_embeddings = np.load('data/candidate_embeddings.npy')
    reference_embeddings = np.load('data/reference_embeddings.npy')

    candidate_names = sorted(os.listdir('data/candidate_images'))
    reference_names = sorted(os.listdir('data/reference_images'))

    flagged = flag_infringements(candidate_embeddings, reference_embeddings, candidate_names, reference_names)

    if not flagged:
        print(f'No infringements found above threshold {SIMILARITY_THRESHOLD}')
    else:
        print(f'Found {len(flagged)} potential infringement(s):\n')
        for match in flagged:
            print(f"  {match['candidate']} <-> {match['reference']}  (similarity: {match['similarity']:.4f})")
