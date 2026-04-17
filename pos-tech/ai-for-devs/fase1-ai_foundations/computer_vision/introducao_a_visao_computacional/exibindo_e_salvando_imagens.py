import cv2

# Carregar a imagem
img = cv2.imread('fase1-ai_foundations/computer_vision/introducao_a_visao_computacional/imagem.png')

# Converter a imagem para escala de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar bordas na imagem
edges = cv2.Canny(img_gray, 100, 200)

# Aplicar suavização com filtro gaussiano
img_blur = cv2.GaussianBlur(img, (15, 15), 0)

# Converter a imagem de BGR para RGB
img_rgb = cv2.cvtColor(img_blur, cv2.COLOR_BGR2RGB)


# Salvando a imagem suavizada em RGB
path = 'fase1-ai_foundations/computer_vision/introducao_a_visao_computacional/content/imagem_suavizada_rgb.png'
cv2.imwrite(path, img_rgb)
print("Imagem suavizada em RGB salva")

# Exibir a imagem
cv2.imshow('Imagem', img)

# Exibir as bordas detectadas
cv2.imshow('Bordas', edges)

# Exibir a imagem em escala de cinza
cv2.imshow('Imagem em Escala de Cinza', img_gray)

# Exibir a imagem suavizada
cv2.imshow('Imagem Suavizada', img_blur)

# Exibir a imagem em RGB
cv2.imshow('Imagem RGB', img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()