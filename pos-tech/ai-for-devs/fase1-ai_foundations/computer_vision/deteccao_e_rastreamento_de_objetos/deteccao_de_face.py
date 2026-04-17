# Importar as bibliotecas necessárias
import cv2
import numpy as np

# Carregar imagem
imagem = cv2.imread('fase1-ai_foundations/computer_vision/deteccao_e_rastreamento_de_objetos/face.png')

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem.")
else:
    # Exibir imagem
    cv2.imshow("Imagem", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Converter a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem em Escala de Cinza", imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detectar faces na imagem
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces=face_cascade.detectMultiScale ( imagem_cinza , scaleFactor= 1.1 , minNeighbors= 5 )

# Desenhar retângulos ao redor das faces detectadas
for ( x , y , w , h ) in faces :
    cv2.rectangle ( imagem , ( x , y ) , ( x+w , y+h ) , ( 255 , 0 , 0 ) , 2 )

# Exibir imagem com detecções
cv2.imshow("Imagem com Detecções", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()