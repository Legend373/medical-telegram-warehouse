import csv
from pathlib import Path
from ultralytics import YOLO


class YOLODetector:
    def __init__(self, model_path="yolov8n.pt", conf_threshold=0.25):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold

        self.PERSON_CLASS = "person"
        self.PRODUCT_CLASSES = {
            "bottle",
            "cup",
            "bowl",
            "jar",
            "container"
        }

    def classify_image(self, detected_classes: set) -> str:
        has_person = self.PERSON_CLASS in detected_classes
        has_product = any(c in self.PRODUCT_CLASSES for c in detected_classes)

        if has_person and has_product:
            return "promotional"
        elif has_product:
            return "product_display"
        elif has_person:
            return "lifestyle"
        else:
            return "other"

    def detect_images(self, image_root: Path, output_csv: Path):
        output_csv.parent.mkdir(parents=True, exist_ok=True)

        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "message_id",
                "channel_name",
                "detected_class",
                "confidence_score",
                "image_category"
            ])

            for channel_dir in image_root.iterdir():
                if not channel_dir.is_dir():
                    continue

                channel_name = channel_dir.name

                for img_path in channel_dir.glob("*.jpg"):
                    message_id = img_path.stem

                    try:
                        results = self.model.predict(
                            source=str(img_path),
                            conf=self.conf_threshold,
                            save=False,
                            verbose=False
                        )

                        detections = []

                        for r in results:
                            if r.boxes is None:
                                continue

                            for box in r.boxes:
                                class_id = int(box.cls[0])
                                class_name = self.model.names[class_id]
                                confidence = float(box.conf[0])

                                detections.append((class_name, confidence))

                        # 🚫 Skip images with NO detections
                        if not detections:
                            continue

                        detected_classes = {d[0] for d in detections}
                        image_category = self.classify_image(detected_classes)

                        # ✅ One row per detection
                        for class_name, confidence in detections:
                            writer.writerow([
                                int(message_id),
                                channel_name,
                                class_name,
                                round(confidence, 4),
                                image_category
                            ])

                    except Exception as e:
                        print(f"⚠️ Skipping {img_path.name}: {e}")

        print(f"✅ YOLO detections written to {output_csv}")
