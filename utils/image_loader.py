import os
from PIL import Image
import numpy as np


def load_sample_images():
    """
    Lista imagens disponíveis
    na pasta samples/
    """

    sample_path = "samples"

    if not os.path.exists(sample_path):
        return []

    files = []

    for file in os.listdir(sample_path):
        if file.lower().endswith(
            (".ppm", ".pgm", ".pbm", ".jpg", ".jpeg", ".png")
        ):
            files.append(file)

    return sorted(files)


def load_selected_sample(filename):
    """
    Carrega imagem da pasta samples
    """

    path = os.path.join(
        "samples",
        filename
    )

    image = Image.open(path)
    img_array = np.array(image)

    is_rgb = len(img_array.shape) == 3

    return image, img_array, is_rgb


