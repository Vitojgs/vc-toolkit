# VC Toolkit — Visão por Computador

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/Status-Acad%C3%A9mico-success)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

Projeto académico desenvolvido em Python + Streamlit para estudo, teste e demonstração de algoritmos fundamentais de Visão por Computador.

Este projeto permite carregar imagens (.ppm, .pgm, .pbm, .jpg, .png, .jpeg) e aplicar operações manuais implementadas em Python, acompanhadas por explicação teórica e pseudocódigo.

---

# Objetivo

Criar uma plataforma interativa que permita testar e compreender os principais algoritmos abordados na disciplina de Visão por Computador.

O foco principal do projeto é:

- implementação manual dos algoritmos
- utilização de pseudocódigo académico
- comparação visual dos resultados
- compreensão prática da teoria

---

# Funcionalidades Implementadas

## 1. Espaços de Cor

- RGB para Gray
- Negativo
- Extração de Canais RGB
- RGB para HSV
- Segmentação HSV

---

## 2. Segmentação

- Threshold Manual
- Threshold por Média Global

---

## 3. Operadores Morfológicos

- Dilatação
- Erosão
- Abertura (Opening)
- Fecho (Closing)

---

## 4. Filtros Espaciais

### Passa-Baixo

- Filtro da Média
- Filtro da Mediana
- Filtro Gaussiano

---

## 5. Deteção de Contornos

### Passa-Alto

- Sobel
- Prewitt
- Roberts
- Laplaciano

---

## 6. Histogramas

- Histograma Gray
- Equalização de Histograma

---

## 7. Blobs e Etiquetagem

- Blob Labelling
- Área dos Blobs
- Centro de Massa

---

## 8. Fourier

- FFT e Espectro de Frequências
- Filtro Passa-Baixo FFT
- Filtro Passa-Alto FFT

---

# Tecnologias Utilizadas

- Python
- Streamlit
- NumPy
- OpenCV
- Pillow
- Matplotlib

---

# Estrutura do Projeto

```text
vc-toolkit/
│
├── app.py
│
├── functions/
│   ├── color.py
│   ├── segmentation.py
│   ├── morphology.py
│   ├── filters.py
│   ├── edges.py
│   ├── histogram.py
│   ├── blobs.py
│   └── fourier.py
│
├── pseudo/
│   └── pseudocodes.py
│
├── utils/
│   ├── image_loader.py
│   └── helpers.py
│
├── samples/
│
├── requirements.txt
│
└── README.md