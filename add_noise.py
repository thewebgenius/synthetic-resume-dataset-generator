from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from pathlib import Path
import random

CLEAN_DIR = Path("output/images/clean")
NOISY_DIR = Path("output/images/noisy")

def add_noise_and_augment():
    print("Looking for clean images in:", CLEAN_DIR.resolve())

    if not CLEAN_DIR.exists():
        print("❌ CLEAN_DIR does not exist")
        return

    image_files = list(CLEAN_DIR.glob("*.png"))
    print(f"Found {len(image_files)} images")

    if len(image_files) == 0:
        print("❌ No images found — check folder and run location")
        return

    NOISY_DIR.mkdir(parents=True, exist_ok=True)

    for img_path in image_files:
        print("Processing:", img_path.name)

        img = Image.open(img_path).convert("RGB")

        # Rotation
        angle = random.uniform(-2, 2)
        img = img.rotate(angle, expand=False, fillcolor=(255, 255, 255))

        # Blur
        if random.random() > 0.5:
            img = img.filter(ImageFilter.GaussianBlur(radius=1))

        # Noise
        arr = np.array(img).astype(np.float32)
        arr += np.random.normal(0, 10, arr.shape)
        arr = np.clip(arr, 0, 255).astype(np.uint8)
        img = Image.fromarray(arr)

        # Contrast / brightness
        img = ImageEnhance.Contrast(img).enhance(random.uniform(0.9, 1.1))
        img = ImageEnhance.Brightness(img).enhance(random.uniform(0.9, 1.1))

        out_path = NOISY_DIR / img_path.name
        img.save(out_path)

        print("Saved:", out_path.name)

if __name__ == "__main__":
    add_noise_and_augment()
