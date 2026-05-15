#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from ultralytics import YOLO


class YOLODetector:
    def __init__(self):
        # 🔥 troca pelo seu modelo treinado se tiver
        self.model = YOLO("yolov8n.pt")

    def process(self, frame):
        # =========================
        # RODA O MODELO
        # =========================
        results = self.model(frame)

        # =========================
        # DESENHA RESULTADOS
        # =========================
        annotated_frame = results[0].plot()

        return annotated_frame
