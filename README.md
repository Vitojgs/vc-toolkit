# VC Toolkit - Visão por Computador

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

O **VC Toolkit** é uma aplicação web interativa desenvolvida em Python para a disciplina de **Visão por Computador**. O objetivo principal é servir como um ambiente de testes para os algoritmos de processamento de imagem lecionados, permitindo comparar implementações manuais (estilo C/Pseudocódigo) com funções otimizadas de bibliotecas como OpenCV.

---

## Funcionalidades

A aplicação permite efetuar o upload de imagens (incluindo formatos Netpbm como **.ppm** e **.pgm**) e aplicar as seguintes operações:

* **Espaços de Cor:** Negativo, extração de canais RGB, conversão para tons de cinzento e segmentação HSV.
* **Segmentação:** Binarização por limiar (threshold) manual e global (média).
* **Operadores Morfológicos:** Dilatação, Erosão, Abertura e Fecho com kernels ajustáveis.
* **Filtros Espaciais:**
    * *Passa-Baixo:* Média, Mediana e Gaussiano.
    * *Passa-Alto / Contornos:* Sobel, Prewitt e Laplaciano.
* **Análise de Dados:** Visualização e equalização de histogramas.
* **Blobs & Etiquetagem:** Identificação e contagem de componentes conectados.
* **Domínio das Frequências:** Visualização do Espectro de Magnitude através da Transformada de Fourier (FFT).

---

## Implementação Didática

Um diferencial deste projeto é a inclusão de uma **implementação manual pixel a pixel** para funções críticas (como a binarização), permitindo validar a lógica do pseudocódigo discutido em aula frente às implementações nativas do OpenCV.

---

## 🛠️ Instalação e Execução Local

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/teu-utilizador/vc-toolkit.git](https://github.com/teu-utilizador/vc-toolkit.git)
    cd vc-toolkit
    ```

2.  **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Correr a aplicação:**
    ```bash
    streamlit run app.py
    ```

---

## Deploy

A aplicação está configurada para ser alojada no **Streamlit Community Cloud**. Basta conectar este repositório ao serviço para ter o seu toolkit online.

---

## Requisitos do Sistema

As bibliotecas necessárias estão listadas no `requirements.txt`:
* `streamlit`
* `numpy`
* `opencv-python-headless`
* `Pillow`
* `matplotlib`

---

## Autor

* **Vítor Silva** - [Teu GitHub](https://github.com/vitojgs)
