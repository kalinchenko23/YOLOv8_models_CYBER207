from ultralytics import YOLO
import os

model = YOLO('/Users/maximkalinchenko/Desktop/Berkeley/Cyber 207/final_project/metrics/best.pt')

results=model.predict("<image_path>",save=True)