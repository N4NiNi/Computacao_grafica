import cv2
import numpy as np

def circulo():
    largura = 400
    altura = 400
    imagem_circulo = np.ones((altura, largura, 3), dtype=np.uint8) * 255
    # Coordenadas do centro do círculo
    centro_x = largura // 2
    centro_y = altura // 2
    # Raio do círculo
    raio = 100
    # Cor do círculo (vermelho)
    cor_r = (0, 0, 255)
    # Desenhar o círculo
    cv2.circle(imagem_circulo, (centro_x, centro_y), raio, cor_r, -1)  # Use -1 para preencher o círculo
    # Salvar a imagem
    cv2.imwrite("circulo_vermelho.png", imagem_circulo)
    # Mostrar a imagem (opcional)
    cv2.imshow("Imagem", imagem_circulo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def quadrado():
    
    # Tamanho da imagem
    largura = 400
    altura = 400

    imagem_quadrado = np.ones((altura, largura, 3), dtype=np.uint8) * 255
    #Coordenadas quadrado
    canto_superior_esquerdo_x = (largura - 200) // 2
    canto_superior_esquerdo_y = (altura - 200) // 2

    canto_inferior_direito_x = canto_superior_esquerdo_x + 200
    canto_inferior_direito_y = canto_superior_esquerdo_y + 200
    cor_b = (255, 0, 0)

    #Desenhar quadrado
    cv2.rectangle(imagem_quadrado, (canto_superior_esquerdo_x, canto_superior_esquerdo_y),
                  (canto_inferior_direito_x, canto_inferior_direito_y), cor_b, -1)
    # Salvar a imagem
    cv2.imwrite("quadrado_azul.png", imagem_quadrado)
    cv2.imshow("Imagem", imagem_quadrado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def degrade():
    # Tam da img
    largura = 400
    altura = 400

    imagem_degrade = np.ones((altura, largura, 3), dtype=np.uint8) * 255

    n_gradients = 100

    # Cores de início e fim
    start_color = (0, 0, 255)
    end_color = (255, 0, 0) 

    # Calcular a diferença de cor entre os gradientes
    color_diff = [(end - start) / n_gradients for start, end in zip(start_color, end_color)]

        # Preencher o quadrado com gradientes
    for i in range(n_gradients):
        # Calcular a cor atual
        current_color = tuple(int(start + i * diff) for start, diff in zip(start_color, color_diff))
        
        # Calcular as coordenadas do quadrado
        x1 = int(i * largura / n_gradients)
        x2 = int((i + 1) * largura / n_gradients)
        
        # Preencher uma coluna do quadrado com a cor atual
        imagem_degrade[:, x1:x2] = current_color

    # Salvar a imagem
    cv2.imwrite("quadrado_degrade.png", imagem_degrade)
    # Exibir a imagem
    cv2.imshow('Quadrado Degrade', imagem_degrade)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

                                
def main():
    circulo()
    quadrado()
    degrade()

main()