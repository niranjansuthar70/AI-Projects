import torch
from ultralytics import YOLO 
print(torch.cuda.is_available())

model = YOLO('yolov8x')

result = model.track('D:\\learning_ai\\AI_projects\\Computer_Vision\\tennis_analysis_bkp\\dataset\\sample_input_data\\input_video.mp4',conf=0.2, save=True)
# print(result)
# print("boxes:")
# for box in result[0].boxes:
#     print(box)