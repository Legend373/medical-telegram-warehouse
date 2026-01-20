import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

from pathlib import Path
from src.yolo.yolo_detect import YOLODetector

# Directory containing all channel images
IMAGE_DIR = Path("../data/raw/images")
OUTPUT_CSV = Path("../data/processed/yolo_detection_results.csv")

detector = YOLODetector(model_path="yolov8n.pt", conf_threshold=0.25)
detector.detect_images(IMAGE_DIR, OUTPUT_CSV)
