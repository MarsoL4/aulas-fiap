import cv2

tracker = cv2.TrackerKCF_create()

video = cv2.VideoCapture("fase1-ai_foundations/computer_vision/deteccao_e_rastreamento_de_objetos/racing_cars.mp4")

ok, frame = video.read()

if not ok:
    print("Erro ao ler o vídeo")
    exit()

# Mostrar primeiro frame
cv2.imshow("Frame inicial", frame)

# Selecionar o carro com o mouse
bbox = cv2.selectROI("Frame inicial", frame, False)

# Fechar janela de seleção
cv2.destroyWindow("Frame inicial")

# Inicializar tracker
tracker.init(frame, bbox)

while True:

    ok, frame = video.read()

    if not ok:
        break

    ok, bbox = tracker.update(frame)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    else:
        cv2.putText(frame, "Tracking falhou", (100,80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(30) & 0xff == 27:
        break

video.release()
cv2.destroyAllWindows()