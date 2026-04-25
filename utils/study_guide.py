import streamlit as st


def show_study_guide(topic):
    """
    Guia de estudo reforçado para apoio ao teste
    de Visão por Computador.
    """

    st.header("Guia de Estudo")

    # =====================================================
    # ESPAÇOS DE COR
    # =====================================================
    if topic == "Espaços de Cor":

        st.subheader("Espaços de Cor")

        st.write("""
Objetivo:
Representar, analisar e manipular imagens em diferentes modelos de cor.

Em Visão por Computador, a escolha do espaço de cor influencia diretamente:

- segmentação
- deteção de objetos
- reconhecimento de padrões
- robustez a iluminação

Principais modelos:

- RGB (Red, Green, Blue)
- Gray (tons de cinzento)
- HSV (Hue, Saturation, Value)

Teoria importante:

RGB é um modelo aditivo de cor, muito usado em câmaras e monitores.

Gray reduz a complexidade da imagem e facilita:

- threshold
- deteção de contornos
- histogramas
- Fourier

HSV separa melhor a cor da intensidade luminosa:

H → Matiz
S → Saturação
V → Brilho

Por isso, HSV é muito melhor para segmentação por cor.

Fórmula importante:

Gray = 0.299R + 0.587G + 0.114B

Não se usa média simples porque o olho humano percebe mais intensamente o verde.

O que pode sair no teste:

- conversão RGB → Gray
- diferença entre RGB e HSV
- porque HSV é melhor para segmentação
- extração de canais RGB
- negativo da imagem
        """)

        st.info("""
Perguntas frequentes:

1. Porque não usamos média simples em RGB → Gray?

2. Qual a principal vantagem do HSV relativamente ao RGB?

3. Em que situações usamos tons de cinzento?
        """)

    # =====================================================
    # SEGMENTAÇÃO
    # =====================================================
    elif topic == "Segmentação":

        st.subheader("Segmentação")

        st.write("""
Objetivo:
Separar objetos do fundo da imagem.

A segmentação é uma das fases mais importantes porque prepara a imagem para:

- contagem de objetos
- blob analysis
- reconhecimento
- inspeção visual

Métodos principais:

- Threshold Manual
- Threshold por Média Global

Teoria importante:

Cada pixel é comparado com um valor limite chamado threshold.

Regra:

pixel >= threshold → branco (255)

pixel < threshold → preto (0)

O resultado é uma imagem binária.

Threshold automático:

T = soma dos pixels / total de pixels

Threshold manual:

valor definido pelo utilizador

Threshold global:

valor calculado automaticamente

O que pode sair no teste:

- explicar binarização
- diferença entre threshold manual e automático
- calcular threshold global
- justificar escolha do threshold
        """)

        st.warning("""
Perguntas frequentes:

1. Qual a diferença entre threshold manual e threshold global?

2. Porque a segmentação costuma ser feita após grayscale?

3. O que acontece se o threshold for demasiado alto?
        """)

    # =====================================================
    # MORFOLOGIA
    # =====================================================
    elif topic == "Morfologia":

        st.subheader("Operadores Morfológicos")

        st.write("""
Objetivo:
Modificar a forma dos objetos binários.

Estas operações são aplicadas após a binarização.

Servem para:

- remover ruído
- preencher falhas
- separar objetos
- unir regiões próximas

Principais operações:

- Dilatação → aumenta objetos
- Erosão → reduz objetos
- Abertura → erosão + dilatação
- Fecho → dilatação + erosão

Teoria importante:

Tudo depende do kernel (elemento estruturante).

Quanto maior o kernel:

- maior o efeito
- maior a alteração da forma

Opening:
remove pequenos ruídos brancos

Closing:
fecha pequenos buracos internos

O que pode sair no teste:

- diferença entre dilatação e erosão
- explicar opening e closing
- função do kernel
        """)

        st.info("""
Perguntas frequentes:

1. Quando usar abertura e quando usar fecho?

2. Porque a erosão pode separar objetos ligados?

3. Qual a influência do tamanho do kernel?
        """)

    # =====================================================
    # FILTROS
    # =====================================================
    elif topic == "Filtros":

        st.subheader("Filtros Espaciais")

        st.write("""
Objetivo:
Melhorar a imagem ou reduzir ruído.

Filtros Passa-Baixo:

- Média
- Mediana
- Gaussiano

Filtros Passa-Alto:

- realce de contornos
- deteção de detalhes

Teoria importante:

Filtro da Média:
substitui o pixel pela média da vizinhança

Filtro da Mediana:
substitui o pixel pela mediana

melhor para ruído sal e pimenta

Filtro Gaussiano:
usa pesos maiores no centro

mais natural e menos agressivo

O que pode sair no teste:

- diferença entre média e mediana
- quando usar Gaussiano
- identificar ruído sal e pimenta
        """)

        st.warning("""
Perguntas frequentes:

1. Porque a mediana preserva melhor os contornos?

2. Qual filtro é melhor para ruído impulsivo?

3. Qual a diferença entre média e Gaussiano?
        """)

    # =====================================================
    # CONTORNOS
    # =====================================================
    elif topic == "Contornos":

        st.subheader("Deteção de Contornos")

        st.write("""
Objetivo:
Detetar mudanças bruscas de intensidade.

Os contornos representam fronteiras entre objetos.

Operadores:

- Sobel
- Prewitt
- Roberts
- Laplaciano

Teoria importante:

Sobel / Prewitt / Roberts:
baseados em primeira derivada (gradiente)

Laplaciano:
baseado em segunda derivada

Fórmula importante:

Magnitude = sqrt(Gx² + Gy²)

Sobel costuma ser mais robusto ao ruído.

Laplaciano é mais sensível e realça mais os contornos.

O que pode sair no teste:

- diferença entre Sobel e Laplaciano
- primeira vs segunda derivada
- cálculo do gradiente
        """)

        st.error("""
Perguntas frequentes:

1. Porque o Laplaciano é mais sensível ao ruído?

2. Qual a diferença entre Sobel e Prewitt?

3. Quando usar Roberts?
        """)

    # =====================================================
    # HISTOGRAMAS
    # =====================================================
    elif topic == "Histogramas":

        st.subheader("Histogramas")

        st.write("""
Objetivo:
Analisar a distribuição de intensidades dos pixels.

Permite estudar:

- contraste
- brilho
- qualidade da imagem
- preparação para segmentação

Histograma Gray:
mostra quantos pixels existem em cada intensidade

0 → preto
255 → branco

Equalização de Histograma:
redistribui intensidades para melhorar contraste

Teoria importante:

Se o histograma estiver muito concentrado:

- imagem com baixo contraste

Se estiver mais distribuído:

- imagem com melhor contraste

O que pode sair no teste:

- interpretação de histogramas
- quando usar equalização
- efeito da equalização no contraste
        """)

        st.info("""
Perguntas frequentes:

1. Como identificar baixo contraste num histograma?

2. Quando a equalização não é recomendada?

3. O que acontece ao brilho após equalização?
        """)

    # =====================================================
    # BLOBS
    # =====================================================
    elif topic == "Blobs":

        st.subheader("Blobs e Etiquetagem")

        st.write("""
Objetivo:
Identificar e analisar objetos conectados.

Blob = região conectada de pixels semelhantes.

Principais conceitos:

- Blob Labelling
- Área
- Centro de Massa
- Connected Components

Teoria importante:

Cada objeto recebe uma label diferente.

Isto permite:

- contar objetos
- medir objetos
- analisar regiões
- preparar reconhecimento automático

Flood Fill:
algoritmo usado para percorrer toda a região conectada

Área:
número total de pixels do blob

Centro de Massa:
posição média do objeto

O que pode sair no teste:

- explicar blob labelling
- funcionamento do flood fill
- cálculo da área
- cálculo do centroide
        """)

        st.warning("""
Perguntas frequentes:

1. O que significa conectividade 4 e conectividade 8?

2. Como funciona o Flood Fill?

3. Porque o blob 0 costuma representar o fundo?
        """)

    # =====================================================
    # FOURIER
    # =====================================================
    elif topic == "Fourier":

        st.subheader("Domínio da Frequência")

        st.write("""
Objetivo:
Analisar a imagem no domínio da frequência.

Em vez de observar pixels diretamente,
observamos frequências.

FFT:
Fast Fourier Transform

Baixas frequências:

- áreas suaves
- regiões homogéneas

Altas frequências:

- contornos
- ruído
- detalhes finos

Teoria importante:

Passa-Baixo FFT:
remove altas frequências

resultado → suavização

Passa-Alto FFT:
remove baixas frequências

resultado → realce de contornos

Isto permite comparar:

- filtros espaciais
- filtros em frequência

O que pode sair no teste:

- explicar FFT
- diferença entre passa-baixo e passa-alto
- interpretação do espectro
        """)

        st.error("""
Perguntas frequentes:

1. Porque o centro do espectro representa baixas frequências?

2. Qual a diferença entre filtro espacial e filtro em Fourier?

3. Porque o passa-alto realça contornos?
        """)


    else:
        st.write("Selecione um tema no menu lateral.")

    # PERGUNTAS E RESPOSTAS GERAIS
    # =====================================================

    st.subheader("Perguntas e Respostas de Revisão")

    st.write("""
1. Porque não usamos média simples em RGB → Gray?

Resposta:
Porque o olho humano não percebe todas as cores com a mesma intensidade.
A componente verde tem maior influência visual, seguida da vermelha e depois da azul.
Por isso usamos a fórmula ponderada:

Gray = 0.299R + 0.587G + 0.114B

---

2. Qual a principal vantagem do HSV relativamente ao RGB?

Resposta:
No HSV conseguimos separar melhor a cor (Hue) da luminosidade (Value),
o que facilita bastante a segmentação por cor e reduz problemas causados
por variações de iluminação.

---

3. Qual a diferença entre Threshold Manual e Threshold Global?

Resposta:
No Threshold Manual o utilizador escolhe o valor do threshold.
No Threshold Global o valor é calculado automaticamente,
normalmente através da média dos pixels.

---

4. Qual a diferença entre Dilatação e Erosão?

Resposta:
Dilatação aumenta os objetos brancos e pode unir regiões próximas.
Erosão reduz os objetos brancos e pode separar objetos ligados.

---

5. Qual a diferença entre Opening e Closing?

Resposta:
Opening = erosão + dilatação
Serve para remover pequenos ruídos externos.

Closing = dilatação + erosão
Serve para fechar pequenos buracos internos.

---

6. Porque a Mediana é melhor para ruído sal e pimenta?

Resposta:
Porque a mediana elimina valores extremos (pixels muito claros ou muito escuros)
sem desfocar tanto a imagem como o filtro da média.

---

7. Qual a diferença entre Sobel e Laplaciano?

Resposta:
Sobel usa primeira derivada e calcula gradientes horizontais e verticais.
É mais robusto ao ruído.

Laplaciano usa segunda derivada e é mais sensível,
realçando mais os contornos e também mais ruído.

---

8. Quando devemos usar Equalização de Histograma?

Resposta:
Quando a imagem apresenta baixo contraste,
ou seja, quando os níveis de cinzento estão muito concentrados
numa pequena região do histograma.

---

9. O que é um Blob?

Resposta:
É uma região conectada de pixels semelhantes,
normalmente obtida após binarização.
Permite contar e medir objetos na imagem.

---

10. Porque o blob 0 representa normalmente o fundo?

Resposta:
Porque na etiquetagem de componentes conectados,
a primeira label é normalmente atribuída ao fundo da imagem,
enquanto os restantes labels representam os objetos.

---

11. O que representam as baixas frequências em Fourier?

Resposta:
Representam áreas suaves e homogéneas da imagem,
com poucas variações de intensidade.

---

12. Porque o filtro passa-alto realça contornos?

Resposta:
Porque remove as baixas frequências e mantém apenas
as altas frequências, que correspondem a mudanças bruscas
na intensidade dos pixels, ou seja, contornos e detalhes finos.
""")
