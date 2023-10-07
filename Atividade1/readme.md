# README - Explicação e Execução de Códigos

Este repositório contém dois exemplos de código em linguagens diferentes: C++ e Python. Abaixo, você encontrará uma explicação de como cada código funciona e como executá-los.

## Atividade 1: exemplo1.cpp

Este é um programa C++ que gera uma imagem PPM simples degradê. Aqui está uma explicação passo a passo do código:

1. Inclui a biblioteca `iostream`.
2. Define as dimensões da imagem (`image_width` e `image_height`) como 256x256 pixels.
3. Exibe o cabeçalho da imagem PPM, indicando o formato, largura, altura e intensidade máxima de cor.
4. Itera por todas as linhas (j) e colunas (i) da imagem.
5. Calcula os valores de vermelho (r), verde (g) e azul (b) com base nas coordenadas normalizadas (de 0 a 1) da posição atual na imagem.
6. Converte os valores de r, g e b para inteiros no intervalo de 0 a 255.
7. Imprime os valores de r, g e b no formato PPM.

### Como Executar

Para compilar e executar o código `exemplo1.cpp`, siga os passos abaixo:

1. Certifique-se de ter um compilador C++ (como g++) instalado em seu sistema.
2. Abra um terminal e navegue até o diretório onde você salvou o arquivo `exemplo1.cpp`.
3. Compile o código usando o seguinte comando:

   ```shell
   g++ exemplo1.cpp -o exemplo1

4. Isso irá gerar um arquivo executável chamado exemplo1.

    ```shell
   ./exemplo1 > imagem.ppm

5. Isso executará o programa e redirecionará a saída para um arquivo chamado imagem.ppm.


## Atividade 2: atv1.py
Este é um programa Python que cria três imagens diferentes: um círculo vermelho, um quadrado azul e um quadrado com um degradê de vermelho a azul. O código está organizado em funções para desenhar cada forma, salvar as imagens e exibi-las (opcionalmente). Aqui está uma explicação das principais partes do código:

1. circulo(): Desenha um círculo vermelho no centro de uma imagem preta.
2. quadrado(): Desenha um quadrado azul no centro de uma imagem preta.
3. degrade(): Cria um degradê de vermelho a azul em uma imagem.

### Como Executar
Para executar o código atv1.py, siga os passos abaixo:

1. Certifique-se de ter o Python e as bibliotecas OpenCV (cv2) e NumPy instalados em seu sistema.

2. Abra um terminal e navegue até o diretório onde você salvou o arquivo atv1.py.

3. Execute o programa com o seguinte comando:

    ```shell
    python atv1.py

Isso executará o programa Python, que criará as imagens e as salvará no diretório atual.

As imagens geradas serão:

* circulo_vermelho.png: Um círculo vermelho.
* quadrado_azul.png: Um quadrado azul.
* quadrado_degrade.png: Um quadrado com um degradê de vermelho a azul.

Lembre-se de que você deve ter as bibliotecas OpenCV e NumPy instaladas para que o código Python funcione corretamente. Você pode instalá-las usando o pip se ainda não estiverem instaladas.