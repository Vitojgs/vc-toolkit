import numpy as np


def rgb_to_gray_manual(img_rgb):
    """
    Converte uma imagem RGB para tons de cinzento
    usando a fórmula clássica de luminância:

    Gray = 0.299R + 0.587G + 0.114B

    Parâmetros:
        img_rgb -> imagem RGB em formato NumPy array

    Retorna:
        imagem em tons de cinzento (uint8)
    """

    altura, largura, canais = img_rgb.shape

    # Criar imagem de saída
    img_gray = np.zeros((altura, largura), dtype=np.uint8)

    # Percorrer pixel a pixel (estilo C / loops manuais)
    for y in range(altura):
        for x in range(largura):

            r = img_rgb[y, x, 0]
            g = img_rgb[y, x, 1]
            b = img_rgb[y, x, 2]

            gray = int(
                0.299 * r +
                0.587 * g +
                0.114 * b
            )

            # Garantir intervalo válido
            if gray < 0:
                gray = 0
            elif gray > 255:
                gray = 255

            img_gray[y, x] = gray

    return img_gray

def rgb_negative_manual(img_rgb):
    """
    Calcula o negativo de uma imagem RGB.

    Fórmula:

    Novo Valor = 255 - Valor Atual

    Aplicado a cada canal:
    R, G e B

    Parâmetros:
        img_rgb -> imagem RGB em NumPy array

    Retorna:
        imagem negativa RGB
    """

    altura, largura, canais = img_rgb.shape

    img_negative = np.zeros((altura, largura, 3), dtype=np.uint8)

    for y in range(altura):
        for x in range(largura):

            r = img_rgb[y, x, 0]
            g = img_rgb[y, x, 1]
            b = img_rgb[y, x, 2]

            img_negative[y, x, 0] = 255 - r
            img_negative[y, x, 1] = 255 - g
            img_negative[y, x, 2] = 255 - b

    return img_negative

def extract_rgb_channel_manual(img_rgb, channel):
    """
    Extrai um canal RGB e devolve uma imagem
    em tons de cinzento.

    channel:
        0 -> Red
        1 -> Green
        2 -> Blue

    Parâmetros:
        img_rgb -> imagem RGB
        channel -> canal a extrair

    Retorna:
        imagem grayscale com o canal extraído
    """

    altura, largura, canais = img_rgb.shape

    img_channel = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(altura):
        for x in range(largura):

            valor = img_rgb[y, x, channel]

            img_channel[y, x] = valor

    return img_channel

def rgb_to_hsv_manual(img_rgb):
    """
    Converte imagem RGB para HSV.

    Retorna imagem HSV em uint8.

    H -> 0 a 179
    S -> 0 a 255
    V -> 0 a 255
    """

    altura, largura, canais = img_rgb.shape

    img_hsv = np.zeros((altura, largura, 3), dtype=np.uint8)

    for y in range(altura):
        for x in range(largura):

            r = img_rgb[y, x, 0] / 255.0
            g = img_rgb[y, x, 1] / 255.0
            b = img_rgb[y, x, 2] / 255.0

            max_val = max(r, g, b)
            min_val = min(r, g, b)
            delta = max_val - min_val

            # VALUE
            v = max_val

            # SATURATION
            if max_val == 0:
                s = 0
            else:
                s = delta / max_val

            # HUE
            if delta == 0:
                h = 0

            elif max_val == r:
                h = 60 * (((g - b) / delta) % 6)

            elif max_val == g:
                h = 60 * (((b - r) / delta) + 2)

            else:
                h = 60 * (((r - g) / delta) + 4)

            # Converter para escala OpenCV
            h = int(h / 2)        # 0–179
            s = int(s * 255)      # 0–255
            v = int(v * 255)      # 0–255

            img_hsv[y, x] = [h, s, v]

    return img_hsv


def hsv_segmentation_manual(
    img_hsv,
    h_min, h_max,
    s_min, s_max,
    v_min, v_max
):
    """
    Segmentação por HSV.

    Retorna imagem binária:
    255 -> dentro do intervalo
    0   -> fora do intervalo
    """

    altura, largura, canais = img_hsv.shape

    mask = np.zeros((altura, largura), dtype=np.uint8)

    for y in range(altura):
        for x in range(largura):

            h = img_hsv[y, x, 0]
            s = img_hsv[y, x, 1]
            v = img_hsv[y, x, 2]

            if (
                h_min <= h <= h_max and
                s_min <= s <= s_max and
                v_min <= v <= v_max
            ):
                mask[y, x] = 255
            else:
                mask[y, x] = 0

    return mask

