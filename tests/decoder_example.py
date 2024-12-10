from BarcodeDecoder import BarcodeDecoder
from PIL import Image
from numpy import asarray

decoder = BarcodeDecoder()
img = asarray(Image.open('data/photo_1.png'))

print(decoder.decode(img))
