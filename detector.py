import cv2
import numpy as np
from config import NUM_COLUNAS, LOW_GREEN, HIGH_GREEN, PIXEL_THRESHOLD

def detect_notes(frame, HIT_LINE_Y):
    
    altura, largura, _ = frame.shape
    largura_coluna = largura // NUM_COLUNAS

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    detected_notes = []

    for i in range(NUM_COLUNAS):

        x_start = i * largura_coluna
        x_end = x_start + largura_coluna

        area = hsv[HIT_LINE_Y-6:HIT_LINE_Y+6, x_start+10:x_end-10]

        mask = cv2.inRange(area, LOW_GREEN, HIGH_GREEN)

        pixels = cv2.countNonZero(mask)

        print(f"coluna {i} pixels:", pixels)

        cv2.imshow("mask", mask)

        if pixels > PIXEL_THRESHOLD: 
            detected_notes.append(i)


    return detected_notes