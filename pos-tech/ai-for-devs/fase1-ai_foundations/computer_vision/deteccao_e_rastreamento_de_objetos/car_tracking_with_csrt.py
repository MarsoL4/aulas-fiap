import cv2

# Criar tracker
tracker = cv2.TrackerCSRT_create()

# Abrir vídeo
video = cv2.VideoCapture("fase1-ai_foundations/computer_vision/deteccao_e_rastreamento_de_objetos/racing_cars.mp4")

# Ler primeiro frame
ok, frame = video.read()

if not ok:
    print("Erro ao abrir o vídeo.")
    exit()

# Selecionar ROI com o mouse
bbox = cv2.selectROI("Selecione o objeto", frame, False)

# Fechar janela de seleção
cv2.destroyWindow("Selecione o objeto")

# Inicializar tracker
tracker.init(frame, bbox)

while True:

    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = tracker.update(frame)

    # Desenhar bounding box
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking error", (100, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Mostrar frame
    cv2.imshow("Tracking", frame)

    # ESC para sair
    if cv2.waitKey(30) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()