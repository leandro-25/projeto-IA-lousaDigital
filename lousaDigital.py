import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector  
import time  # Para gerar nomes de arquivos únicos baseados no tempo

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
video.set(3, 1280)
video.set(4, 720)

detector = HandDetector()
drawings = []  # Lista única para armazenar todos os pontos desenhados
current_color = (0, 0, 255)  # Cor atual (vermelho)
brush_thickness = 16

while True:
    check, img = video.read()
    result = detector.findHands(img, draw=True)
    hand = result[0]  
    if hand:
        lmlist = hand[0]['lmList']  
        fingers = detector.fingersUp(hand[0])  
        fingers_up_count = fingers.count(1)  

        if fingers_up_count == 1:
            x, y = lmlist[8][0], lmlist[8][1]  
            cv2.circle(img, (x, y), brush_thickness, current_color, cv2.FILLED)  
            drawings.append((x, y, current_color))  # Adiciona ponto desenhado
        elif fingers_up_count != 1 and fingers_up_count != 3: 
            drawings.append((0, 0, current_color))  # Ponto para separar o desenho
        elif fingers_up_count == 3: 
            drawings = []  # Limpa o desenho ao mostrar 3 dedos

    # Desenha apenas os pontos mais recentes
    for i in range(1, len(drawings)):
        if drawings[i][0] != 0 and drawings[i-1][0] != 0:  # Evita desenhar pontos vazios
            cv2.line(img, (drawings[i-1][0], drawings[i-1][1]), (drawings[i][0], drawings[i][1]), drawings[i][2], brush_thickness)

    imgFlip = cv2.flip(img, 1)
    cv2.imshow('Img', imgFlip)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):  # Muda a cor para vermelho
        print("vermelho")
        current_color = (0, 0, 255)  
    elif key == ord('2'):  # Muda a cor para verde
        print("verde")
        current_color = (0, 255, 0)  
    elif key == ord('3'):  # Muda a cor para azul
        print("azul")
        current_color = (255, 0, 0)
    elif key == ord('4'):  # Muda para o amarelo
        current_color = (0,255,255)
        print("amarelo")
    elif key == ord('s') or key == ord('S'):  # Salva a imagem ao apertar 'S'
        timestamp = time.strftime("%Y%m%d-%H%M%S")  #o
        filename = f"desenho_{timestamp}.png"
        cv2.imwrite(filename, imgFlip)  # Salva a imagem
        print(f"Imagem salva como {filename}")
    elif key == 27:  # Sai do loop ao apertar 'ESC'
        break

video.release()
cv2.destroyAllWindows()
