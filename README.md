# VC Toolkit — Visão por Computador

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/Status-Acad%C3%A9mico-success)
![Study Guide](https://img.shields.io/badge/Study%20Guide-Included-purple)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

Projeto académico desenvolvido em Python + Streamlit para estudo, teste e demonstração de algoritmos fundamentais de Visão por Computador.

A aplicação permite carregar imagens (.ppm, .pgm, .pbm, .jpg, .jpeg, .png), aplicar algoritmos manuais implementados em Python, visualizar resultados lado a lado, consultar pseudocódigo académico e ainda utilizar um Guia de Estudo completo para preparação de testes.

---

# Objetivo

Criar uma plataforma interativa que permita:

- testar algoritmos de Visão por Computador
- compreender a teoria associada
- visualizar resultados práticos
- estudar para avaliação da disciplina
- comparar diferentes abordagens de processamento

O foco principal do projeto é:

- implementação manual dos algoritmos
- utilização de pseudocódigo académico
- explicação teórica reforçada
- perguntas frequentes de exame
- respostas explicadas
- aprendizagem prática e visual

---

# Funcionalidades Implementadas

## 1. Espaços de Cor

- RGB para Gray
- Negativo RGB
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

## 9. Guia de Estudo Integrado

Inclui apoio direto para preparação do teste com:

- resumo teórico por tema
- fórmulas importantes
- diferenças entre algoritmos
- perguntas frequentes
- respostas explicadas
- tópicos que costumam sair no exame

Temas disponíveis:

- Espaços de Cor
- Segmentação
- Morfologia
- Filtros
- Contornos
- Histogramas
- Blobs
- Fourier

---

# Funcionalidades Extra

- Upload de imagens PPM, PGM, PBM, JPG e PNG
- Visualização lado a lado (original vs resultado)
- Download da imagem processada
- Interface preparada para Streamlit Cloud
- Projeto modular e organizado para GitHub

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
│   ├── helpers.py
│   └── study_guide.py
│
├── samples/
│
├── requirements.txt
│
└── README.md
