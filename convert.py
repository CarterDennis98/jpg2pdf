from PIL import Image
from pathlib import Path
import os, os.path

imgs = []
path ="E:/Pictures/testing"
valid_images = [".jpg", ".jpeg"]

for file in os.listdir(path):
    ext = os.path.splitext(file)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(Image.open(os.path.join(path, file)))

for image in imgs:
    temp = image.convert('RGB')
    print(Path(image.filename).stem)
    temp.save(path + '/' + Path(image.filename).stem + '.pdf')