from PIL import Image, ImageOps
from pathlib import Path
import os, os.path

imgs = []
path ="your path here"
valid_images = [".jpg", ".jpeg"]

for file in os.listdir(path):
    ext = os.path.splitext(file)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(Image.open(os.path.join(path, file)))

for image in imgs:
    temp = image.convert('RGB')
    temp = ImageOps.exif_transpose(temp)
    print(Path(image.filename).stem)
    temp.save(path + '/' + Path(image.filename).stem + '.pdf')