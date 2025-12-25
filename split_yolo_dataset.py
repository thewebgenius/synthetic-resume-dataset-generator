import random
import shutil
from pathlib import Path

# Paths
CLEAN_IMG_DIR = Path("output/images/clean")
LABEL_DIR = Path("annotations")

YOLO_IMG_TRAIN = Path("yolo_dataset/images/train")
YOLO_IMG_VAL = Path("yolo_dataset/images/val")
YOLO_LBL_TRAIN = Path("yolo_dataset/labels/train")
YOLO_LBL_VAL = Path("yolo_dataset/labels/val")

# Create folders
YOLO_IMG_TRAIN.mkdir(parents=True, exist_ok=True)
YOLO_IMG_VAL.mkdir(parents=True, exist_ok=True)
YOLO_LBL_TRAIN.mkdir(parents=True, exist_ok=True)
YOLO_LBL_VAL.mkdir(parents=True, exist_ok=True)

# Collect images
images = sorted(CLEAN_IMG_DIR.glob("*.png"))
random.shuffle(images)

split_idx = int(0.8 * len(images))
train_imgs = images[:split_idx]
val_imgs = images[split_idx:]

def copy_pair(img_path, img_dst, lbl_dst):
    lbl_path = LABEL_DIR / f"{img_path.stem}.txt"
    if not lbl_path.exists():
        raise FileNotFoundError(f"Missing label for {img_path.name}")

    shutil.copy(img_path, img_dst / img_path.name)
    shutil.copy(lbl_path, lbl_dst / lbl_path.name)

# Copy training data
for img in train_imgs:
    copy_pair(img, YOLO_IMG_TRAIN, YOLO_LBL_TRAIN)

# Copy validation data
for img in val_imgs:
    copy_pair(img, YOLO_IMG_VAL, YOLO_LBL_VAL)

print(f"Total images      : {len(images)}")
print(f"Training images   : {len(train_imgs)}")
print(f"Validation images : {len(val_imgs)}")
print("YOLO dataset split completed successfully.")
