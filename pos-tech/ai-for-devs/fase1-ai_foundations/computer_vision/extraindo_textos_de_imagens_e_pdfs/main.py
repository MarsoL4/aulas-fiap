import cv2

# Carregar a imagem
imagem = cv2.imread('fase1-ai_foundations/computer_vision/extraindo_textos_de_imagens_e_pdfs/imagem_com_texto.png')

# Exibir a imagem
cv2.imshow('Imagem com Texto', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()