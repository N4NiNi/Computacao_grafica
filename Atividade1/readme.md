# README - Explicação e Execução de Códigos

Este repositório contém dois exemplos de código em linguagens diferentes: C++ e Python. Abaixo, você encontrará uma explicação de como cada código funciona e como executá-los.

## Exemplo 1: exemplo1.cpp

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
2. Crie um arquivo de código-fonte chamado `exemplo1.cpp` e cole o código dentro dele.
3. Abra um terminal e navegue até o diretório onde você salvou o arquivo `exemplo1.cpp`.
4. Compile o código usando o seguinte comando:

   ```shell
   g++ exemplo1.cpp -o exemplo1

1. Isso irá gerar um arquivo executável chamado exemplo1.

   ./exemplo1 > imagem.ppm

   Isso executará o programa e redirecionará a saída para um arquivo chamado imagem.ppm.


