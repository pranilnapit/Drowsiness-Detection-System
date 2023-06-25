import cv2
import torch
import numpy as np
import pandas as pd


model1 = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Acer/FinalYearProject/yolov5/runs/train/exp/weights/last.pt', force_reload = True)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results1 = model1(frame).render()
    results1 = cv2.cvtColor(results1[0], cv2.COLOR_RGB2BGR)
    cv2.imshow('YOLO', results1)
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

