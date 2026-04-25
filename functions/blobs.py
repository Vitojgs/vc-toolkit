import numpy as np


def flood_fill(img, labels, y, x, label):
    """
    Flood fill manual para etiquetagem.
    """

    altura, largura = img.shape

    stack = [(y, x)]

    while stack:
        cy, cx = stack.pop()

        if cy < 0 or cy >= altura:
            continue

        if cx < 0 or cx >= largura:
            continue

        if img[cy, cx] == 0:
            continue

        if labels[cy, cx] != 0:
            continue

        labels[cy, cx] = label

        # 4-connectivity
        stack.append((cy - 1, cx))
        stack.append((cy + 1, cx))
        stack.append((cy, cx - 1))
        stack.append((cy, cx + 1))


def blob_count_manual(img_binary):
    """
    Etiquetagem manual de blobs.

    Parâmetros:
        img_binary -> imagem binária

    Retorna:
        labels -> imagem etiquetada
        total_labels -> número de blobs
    """

    altura, largura = img_binary.shape

    labels = np.zeros((altura, largura), dtype=np.int32)

    current_label = 0

    for y in range(altura):
        for x in range(largura):

            if img_binary[y, x] == 255 and labels[y, x] == 0:
                current_label += 1

                flood_fill(
                    img_binary,
                    labels,
                    y,
                    x,
                    current_label
                )

    return labels, current_label


def blob_properties_manual(labels, total_labels):
    """
    Calcula área e centro de massa
    de cada blob.

    Parâmetros:
        labels -> imagem etiquetada
        total_labels -> número de blobs

    Retorna:
        lista com:
        [
            {
                "label": 1,
                "area": ...,
                "centroid": (x, y)
            }
        ]
    """

    propriedades = []

    for label in range(1, total_labels + 1):

        area = 0
        soma_x = 0
        soma_y = 0

        altura, largura = labels.shape

        for y in range(altura):
            for x in range(largura):

                if labels[y, x] == label:
                    area += 1
                    soma_x += x
                    soma_y += y

        if area > 0:
            centroid_x = int(soma_x / area)
            centroid_y = int(soma_y / area)

            propriedades.append({
                "label": label,
                "area": area,
                "centroid": (centroid_x, centroid_y)
            })

    return propriedades




