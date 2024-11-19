from BarcodeDecoder import BarcodeDecoder
from PIL import Image
from numpy import asarray

decoder = BarcodeDecoder()
img = Image.open('data/qr_code.png')
print(decoder.decode(asarray(img)))
