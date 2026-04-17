import cv2

imagem = cv2.imread('fase1-ai_foundations/computer_vision/introducao_a_visao_computacional/imagem.png')

# Definir as coordenadas e a cor do retângulo
inicio = (50, 5)
fim = (220, 160)
cor = (0, 255, 0)  # Verde em RGB
espessura = 2

# Desenhar o retângulo na cópia da imagem
imagem_com_retangulo = cv2.rectangle(imagem.copy(), 
                                     inicio, fim, cor, espessura)

# Converter a imagem para RGB
imagem_com_retangulo_rgb = cv2.cvtColor(imagem_com_retangulo, 
                                        cv2.COLOR_BGR2RGB)

# Exibir a imagem com o retângulo
cv2.imshow('Imagem com Retângulo', imagem_com_retangulo_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()