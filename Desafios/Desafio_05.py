import cv2
import numpy as np
from gtts import gTTS
import os

# Carrega os nomes das classes do COCO
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Carrega o modelo pré-treinado YOLOv3-tiny
net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
layer_names = net.getUnconnectedOutLayersNames()

# Função para detectar objetos na imagem
def detect_objects(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Pré-processamento da imagem
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(layer_names)

    class_ids = []
    confidences = []
    boxes = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.4:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Aplicar supressão de não-máximos
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)

    detected_objects = []
    for i in indices:
        i = i[0]
        box = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]

        detected_objects.append(label)

        x, y, w, h = box
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f"{label} ({int(confidence*100)}%)", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image, detected_objects

# Função para criar o áudio descritivo
def generate_audio_description(objects_detected, language='pt'):
    if not objects_detected:
        description = "Nenhum objeto foi detectado na imagem."
    else:
        description = "Objetos detectados na imagem: " + ", ".join(set(objects_detected)) + "."

    tts = gTTS(text=description, lang=language)
    tts.save("descricao.mp3")
    print("Áudio salvo como descricao.mp3")

# Caminho da imagem a ser analisada
image_path = "imagem.jpg"

# Execução
result_image, objects_detected = detect_objects(image_path)
cv2.imwrite("resultado.jpg", result_image)
print("Imagem com objetos destacados salva como resultado.jpg")

generate_audio_description(objects_detected)
