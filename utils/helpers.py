from PIL import Image
from io import BytesIO
import numpy as np


def convert_numpy_to_downloadable_image(img_array):
    """
    Converte imagem NumPy para bytes
    para permitir download no Streamlit.

    Parâmetros:
        img_array -> imagem numpy

    Retorna:
        bytes da imagem PNG
    """

    if img_array.dtype != np.uint8:
        img_array = img_array.astype(np.uint8)

    image = Image.fromarray(img_array)

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    return buffer.getvalue()