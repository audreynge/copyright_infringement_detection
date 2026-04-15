import os
import numpy as np
from PIL import Image
import pillow_avif
import torch
from transformers import AutoImageProcessor, AutoModel

device = "cuda" if torch.cuda.is_available() else "cpu"

# use DINOv2 for fine grained image embeddings
model_name = "facebook/dinov2-base"
processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name).to(device)
model.eval()

def generate_embedding(image_path: str):
    """
    Loads an image and returns a 1D embedding vector.
    """
    image = Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt").to(device)

    # generate embeddings
    with torch.no_grad():
        outputs = model(**inputs)

    # CLS token embedding usually used as img representation
    # last_hidden_state (1, num_patches+1, 768) -> contains CLS token at idx 0
    embedding = outputs.last_hidden_state[:, 0, :].squeeze() # squeeze gives tensor of shape (768,)
    return embedding.cpu().numpy()


if __name__ == "__main__":
    candidate_images_dir = 'data/candidate_images'
    reference_images_dir = 'data/reference_images'

    candidate_embeddings = []
    reference_embeddings = []

    candidate_images = sorted([f for f in os.listdir(candidate_images_dir)])
    reference_images = sorted([f for f in os.listdir(reference_images_dir)])

    for i in candidate_images:
        path = os.path.join(candidate_images_dir, i)
        candidate_embeddings.append(generate_embedding(path))

    for i in reference_images:
        path = os.path.join(reference_images_dir, i)
        reference_embeddings.append(generate_embedding(path))

    candidate_embeddings = np.array(candidate_embeddings)
    reference_embeddings = np.array(reference_embeddings)

    np.save('data/candidate_embeddings.npy', candidate_embeddings)
    np.save('data/reference_embeddings.npy', reference_embeddings)