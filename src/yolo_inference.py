import torch
import numpy as np
import cv2
import os

class YoloDetector:
    def __init__(self, model_path="models/yolov8n.pt", device="cpu"):
        """
        Initialize YOLO model for object detection.
        """
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file {model_path} not found.")

        # 使用 Ultralytics YOLO v8
        # 若您安裝的是 ultralytics>=8.0.0，可使用:
        from ultralytics import YOLO
        self.model = YOLO(model_path)
        self.device = device

    def count_person(self, frame):
        """
        Perform inference on a single frame and count how many 'person' objects appear.
        """
        results = self.model.predict(source=frame, device=self.device)
        # YOLOv8 results會返回一個 list，每個元素都有 boxes, masks, probs 等
        # 這裡簡單處理:
        if not results:
            return 0

        boxes = results[0].boxes.cpu().numpy()  # 取第0張圖片的預測結果
        count = 0
        for box in boxes:
            # box.data.shape -> (6,) = [x1, y1, x2, y2, confidence, class_id]
            class_id = int(box.data[0, 5])
            if class_id == 0:  # 在 COCO dataset 中, class 0 通常是 'person'
                count += 1

        return count
